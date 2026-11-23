"""Generator adjustment bracket C2286, XK 150S. Builds DXF (inches) and 1:1 PDF.
Usage: python3 build_C2286_bracket.py v1|v2
  v1: R0.59 right fillet sized for 1.29 max width (0.22 min wall at corner)
  v2: R0.43 corner concentric with lower slot top end (0.26 min wall), 1.32 max width
"""
import sys
VERSION = sys.argv[1] if len(sys.argv) > 1 else "v2"
import math
import numpy as np
import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---- geometry (inches) ----
a1, a2 = math.radians(20), math.radians(14)          # slot angles from vertical
A, R1 = (0.39, 3.61), 0.39                           # top end centre / radius
B, R2 = (0.43, 0.43), 0.43                           # bottom end centre / radius
r = 0.17                                             # slot half-width (0.34 slots)
n1 = (math.cos(a1), math.sin(a1))
n2 = (math.cos(a2), -math.sin(a2))
d1 = (math.sin(a1), -math.cos(a1))                   # upper slot axis, downward
d2 = (math.sin(a2), math.cos(a2))                    # lower slot axis, upward
U1, U2 = A, (A[0] + 0.45 * d1[0], A[1] + 0.45 * d1[1])      # upper slot 0.79 OAL
L1, L2 = B, (B[0] + 1.885 * d2[0], B[1] + 1.885 * d2[1])    # lower slot 2.225 OAL

pt = lambda c, rad, ang: (c[0] + rad * math.cos(ang), c[1] + rad * math.sin(ang))
bulge = lambda sweep: math.tan(sweep / 4)

if VERSION == "v1":
    # fillet sized so max width = 1.29
    c1 = n1[0] * A[0] + n1[1] * A[1] + R1
    c2 = n2[0] * B[0] + n2[1] * B[1] + R2
    def fillet_centre(rf):
        det = n1[0] * n2[1] - n1[1] * n2[0]
        b1, b2 = c1 - rf, c2 - rf
        return ((b1 * n2[1] - n1[1] * b2) / det, (n1[0] * b2 - b1 * n2[0]) / det)
    lo, hi = 0.01, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if fillet_centre(mid)[0] + mid > 1.29: lo = mid
        else: hi = mid
    RF = (lo + hi) / 2
    C = fillet_centre(RF)
    th = a1                       # upper right edge normal angle
else:
    # corner arc concentric with lower slot top end, 0.26 wall
    RF = r + 0.26
    C = L2
    dx, dy = C[0] - A[0], C[1] - A[1]
    base = math.atan2(dy, dx)
    off = math.acos((R1 - RF) / math.hypot(dx, dy))
    th = base + off if math.cos(base + off) > 0 else base - off   # external tangent, right side
MAXW = C[0] + RF
ANGLE = 180 - (math.degrees(th) + 14)

# outer profile, CCW, as (x, y, bulge to next vertex)
outer = [
    (*pt(B, R2, math.pi), bulge(math.pi - a2)),          # bottom arc 180 -> 346
    (*pt(B, R2, -a2), 0),                                # line up right side
    (*pt(C, RF, -a2), bulge(th + a2)),                   # corner arc
    (*pt(C, RF, th), 0),                                 # line up to top arc
    (*pt(A, R1, th), bulge(math.pi - th)),               # top arc
    (*pt(A, R1, math.pi), 0),                            # line down left edge
]

def slot(p, q):
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    nr = ang - math.pi / 2
    return [(*pt(p, r, nr), 0), (*pt(q, r, nr), 1.0),
            (*pt(q, r, nr + math.pi), 0), (*pt(p, r, nr + math.pi), 1.0)]

profiles = [outer, slot(U1, U2), slot(L1, L2)]

# ---- DXF ----
doc = ezdxf.new("R2010", setup=True)
doc.units = ezdxf.units.IN
doc.header["$MEASUREMENT"] = 0
msp = doc.modelspace()
for prof in profiles:
    msp.add_lwpolyline([(x, y, 0, 0, b) for x, y, b in prof],
                       format="xyseb", close=True)
doc.saveas(f"C2286_generator_bracket_{VERSION}.dxf")

# ---- polyline -> dense points for plotting ----
def dense(prof, n=120):
    out = []
    for i, (x, y, b) in enumerate(prof):
        x2, y2, _ = prof[(i + 1) % len(prof)]
        if abs(b) < 1e-12:
            out += [(x, y)]
            continue
        sweep = 4 * math.atan(b)
        chord = math.hypot(x2 - x, y2 - y)
        rad = chord / (2 * math.sin(sweep / 2))
        mx, my = (x + x2) / 2, (y + y2) / 2
        h = rad * math.cos(sweep / 2)
        ux, uy = (x2 - x) / chord, (y2 - y) / chord
        cx, cy = mx - uy * h, my + ux * h
        a0 = math.atan2(y - cy, x - cx)
        for t in np.linspace(0, sweep, n, endpoint=False):
            out.append((cx + rad * math.cos(a0 + t), cy + rad * math.sin(a0 + t)))
    out.append(out[0])
    return np.array(out)

# ---- PDF, letter, true scale ----
fig = plt.figure(figsize=(8.5, 11))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 8.5); ax.set_ylim(0, 11); ax.axis("off")
ox, oy = 3.0, 3.6   # part origin on the page (inches)
for prof, col in zip(profiles, ["black", "#C0392B", "#C0392B"]):
    p = dense(prof)
    ax.plot(p[:, 0] + ox, p[:, 1] + oy, color=col, lw=0.6)

def dim(p, q, text, tx, ty, ha="left", both=False):
    P = (p[0] + ox, p[1] + oy); Q = (q[0] + ox, q[1] + oy)
    ax.annotate("", xy=Q, xytext=P, arrowprops=dict(
        arrowstyle="<|-|>" if both else "-|>", lw=0.5, color="#1D7A5A",
        shrinkA=0, shrinkB=0, mutation_scale=6))
    ax.text(tx + ox, ty + oy, text, fontsize=7, ha=ha, va="center", color="#1D7A5A")

def perp_dim(c, nvec, start, length, text, toff, ha="left"):
    p = (c[0] + start * nvec[0], c[1] + start * nvec[1])
    q = (c[0] + (start + length) * nvec[0], c[1] + (start + length) * nvec[1])
    dim(p, q, text, q[0] + toff[0], q[1] + toff[1], ha)

# overall length and width
ax.annotate("", xy=(ox - 0.35, oy + 4.0), xytext=(ox - 0.35, oy), arrowprops=dict(
    arrowstyle="<|-|>", lw=0.5, color="0.3", mutation_scale=6, shrinkA=0, shrinkB=0))
ax.plot([ox - 0.45, ox - 0.05], [oy, oy], lw=0.3, color="0.5", ls=":")
ax.plot([ox - 0.45, ox + 0.39], [oy + 4.0, oy + 4.0], lw=0.3, color="0.5", ls=":")
ax.text(ox - 0.42, oy + 2.0, "4.00", fontsize=8, ha="right", va="center")
ax.annotate("", xy=(ox + MAXW, oy - 0.35), xytext=(ox, oy - 0.35), arrowprops=dict(
    arrowstyle="<|-|>", lw=0.5, color="0.3", mutation_scale=6, shrinkA=0, shrinkB=0))
ax.plot([ox, ox], [oy - 0.45, oy + 0.43], lw=0.3, color="0.5", ls=":")
ax.plot([ox + MAXW, ox + MAXW], [oy - 0.45, oy + C[1]], lw=0.3, color="0.5", ls=":")
ax.text(ox + MAXW / 2, oy - 0.48, f"{MAXW:.2f} max", fontsize=8, ha="center", va="center")

# walls
up = (-d1[0], -d1[1])
perp_dim(U1, up, r, 0.22, "0.22", (-0.05, 0.06), "right")
perp_dim(U1, n1, r, 0.22, "0.22", (0.05, 0.0))
u2w = R1 - r - (math.cos(th) * (U2[0] - A[0]) + math.sin(th) * (U2[1] - A[1]))
perp_dim(U2, n1, r, u2w, f"{u2w:.2f}", (0.05, 0.0))
cn = (math.cos(th), math.sin(th))
perp_dim(C if VERSION == "v2" else L2, cn, r if VERSION == "v2" else r, 0.26 if VERSION == "v2" else 0.216,
         "0.26 min" if VERSION == "v2" else "0.22 min", (0.05, 0.03))
for s in (0.4, 1.5):
    c = (B[0] + s * d2[0], B[1] + s * d2[1])
    perp_dim(c, n2, r, 0.26, "0.26", (0.05, 0.0))
perp_dim(L1, (-d2[0], -d2[1]), r, 0.26, "0.26", (0.0, -0.1), "center")
# slot widths
for c, nv in [((U1[0] + U2[0]) / 2, (U1[1] + U2[1]) / 2), n1], \
             [(B[0] + 0.94 * d2[0], B[1] + 0.94 * d2[1]), n2]:
    p = (c[0] - r * nv[0], c[1] - r * nv[1]); q = (c[0] + r * nv[0], c[1] + r * nv[1])
    ax.annotate("", xy=(q[0] + ox, q[1] + oy), xytext=(p[0] + ox, p[1] + oy),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.5, color="#C0392B",
                                mutation_scale=5, shrinkA=0, shrinkB=0))
    ax.text(p[0] + ox - 0.04, p[1] + oy, "0.34", fontsize=7, ha="right", va="center", color="#C0392B")

# notes and title
notes = [
    f"XK 150S generator adjustment bracket (C2286) - {VERSION}",
    "",
    "Original part thickness: 0.19 in. Standard 3/16 sheet is 0.187;",
    "  a thicker sheet may be chosen - check bolt length and spacing on the car first.",
    "Upper slot: 0.34 x 0.79, 20 deg from vertical",
    "Lower slot: 0.34 x 2.225, 14 deg from vertical",
    "Ends: R0.39 top, R0.43 bottom",
    (f"Right fillet: R{RF:.2f} (min wall 0.22 at corner)" if VERSION == "v1"
     else f"Corner: R{RF:.2f} concentric with lower slot top end (min wall 0.26)"),
    f"Max width: {MAXW:.2f}   Angle between right edges: {ANGLE:.0f} deg",
    "Units: inches",
]
for i, t in enumerate(notes):
    ax.text(0.75, 10.2 - i * 0.22, t, fontsize=11 if i == 0 else 8.5,
            weight="bold" if i == 0 else "normal", va="top")

# 1 in check square
ax.add_patch(Rectangle((5.75, 1.0), 1.0, 1.0, fill=False, lw=0.6))
ax.text(6.25, 0.85, "1.000 in check square", fontsize=7.5, ha="center", va="top")
ax.text(0.75, 1.0, "Print at 100% / Actual size (no 'fit to page').\n"
        "Measure the check square before laying the original on the print.",
        fontsize=7.5, va="bottom")
fig.savefig(f"C2286_generator_bracket_{VERSION}.pdf")
fig.savefig(f"C2286_generator_bracket_{VERSION}_preview.png", dpi=110)
print(VERSION, "corner R", round(RF, 4), "maxw", round(MAXW, 4), "angle", round(ANGLE, 2))
