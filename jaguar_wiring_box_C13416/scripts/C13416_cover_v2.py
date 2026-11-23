"""
C13416 Jaguar XK150 wiring connector shield (cover) - flat pattern v2, for SendCutSend.
Units: inches. Writes C13416_cover_v2.dxf (layers CUT and BEND) and C13416_cover_v2_preview.png.

Rebuilt 2026-11-21 from the design inputs of the original generator (cover.py, chat
"Jag wire cover template", 2026-11-13..18). Verified against the v1 DXF vertices and the
dimensions printed on the v2 template PDF.

Folded part: flat TOP, FRONT face folding down along the long edge, an END wall folding down
at each short end, a TAB on each end folding the opposite way to sit flat on the body (mounting
holes), and a FLAP on each end of the FRONT that folds inward and tucks inside the END.
Back and bottom are open.
"""
import math
import ezdxf

# ---------------- design inputs ----------------
T = 0.048          # 18 ga mild steel (assumed)
R_IN = 0.05        # inside bend radius (approx; confirm with SendCutSend bending calculator)
K = 0.38           # K-factor (approx)
HOLE_CC = 6.25     # mounting hole spacing, folded (measured on car)
HOLE_D = 0.20      # #10 clearance
D = 2.00           # TOP depth: front outer face to open back edge
H_IN = 1.125       # clearance under TOP
E = 0.50           # END outer face to hole centre (folded)
TAB_W = 0.60       # tab width (full-round end)
GAP = 0.25         # gap left under the FRONT face (wire exit)
FLAP = 0.50        # flap depth (folded)
FLAP_G1 = 0.18     # flap top edge starts this far below the front bend line (at the flap bend)
FLAP_G2 = 0.45     # ... and this far below it at the flap's free end (sloped top edge)
CLR = 0.06         # clearance between flap and END inside face
RR = 0.10          # corner relief radius, centred on the front/end bend-line intersection

# ---------------- derived ----------------
BA = math.pi / 2 * (R_IN + K * T)    # bend allowance
BD = 2 * (R_IN + T) - BA             # bend deduction (~0.089)
H_OUT = H_IN + T
LB = HOLE_CC - 2 * E                 # outer length between END faces (5.25)
Lt = LB - BD                         # TOP flat length, bend line to bend line
Dy = D - BD / 2                      # TOP flat depth from front bend line
F = (H_OUT - GAP) - BD / 2           # FRONT flat height
END = H_OUT - BD                     # END flat length between its two bends
HX = END + (E + T - BD / 2)          # END bend line to hole centre (flat)
XF = T + CLR - BD / 2                # flap bend line inset from END bend line (flat)
FL = FLAP - BD / 2                   # flap flat length
y0 = -BD / 2                         # END front edge (flat) = FRONT outer face
tr = TAB_W / 2
yc = D / 2 - BD / 2                  # tab / hole centre line

def ang(p, c):
    return math.atan2(p[1] - c[1], p[0] - c[0])

def bulge(p1, p2, c, ccw):
    a1, a2 = ang(p1, c), ang(p2, c)
    sweep = (a2 - a1) % (2 * math.pi) if ccw else -((a1 - a2) % (2 * math.pi))
    return math.tan(sweep / 4)

def tangent_pt(P, C, r, pick):
    d = math.hypot(P[0] - C[0], P[1] - C[1])
    base, off = ang(P, C), math.acos(r / d)
    cands = [(C[0] + r * math.cos(base + s * off), C[1] + r * math.sin(base + s * off)) for s in (1, -1)]
    return pick(cands)

# round corner reliefs
cL, cR = (0.0, 0.0), (Lt, 0.0)
xL_end = -math.sqrt(RR**2 - y0**2)
yL_fr = -math.sqrt(RR**2 - XF**2)
pL1, pL2 = (xL_end, y0), (XF, yL_fr)
pR1, pR2 = (Lt - XF, yL_fr), (Lt - xL_end, y0)

# tabs: straight edges tangent to the round end
CLt, CRt = (-HX, yc), (Lt + HX, yc)
tL_top = tangent_pt((-END, Dy), CLt, tr, lambda c: min(c, key=lambda p: p[0] - p[1]))
tL_bot = tangent_pt((-END, y0), CLt, tr, lambda c: min(c, key=lambda p: p[0] + p[1]))
tR_bot = (Lt - tL_bot[0], tL_bot[1])
tR_top = (Lt - tL_top[0], tL_top[1])

pts = [  # (x, y, bulge) counter-clockwise
    (XF - FL, -F, 0), (Lt - XF + FL, -F, 0), (Lt - XF + FL, -FLAP_G2, 0), (Lt - XF, -FLAP_G1, 0),
    (pR1[0], pR1[1], bulge(pR1, pR2, cR, ccw=False)),
    (pR2[0], pR2[1], 0), (Lt + END, y0, 0),
    (tR_bot[0], tR_bot[1], bulge(tR_bot, tR_top, CRt, ccw=True)),
    (tR_top[0], tR_top[1], 0),
    (Lt + END, Dy, 0), (Lt, Dy, 0), (0, Dy, 0), (-END, Dy, 0),
    (tL_top[0], tL_top[1], bulge(tL_top, tL_bot, CLt, ccw=True)),
    (tL_bot[0], tL_bot[1], 0),
    (-END, y0, 0),
    (pL1[0], pL1[1], bulge(pL1, pL2, cL, ccw=False)),
    (pL2[0], pL2[1], 0),
    (XF, -FLAP_G1, 0), (XF - FL, -FLAP_G2, 0),
]
holes = [(-HX, yc), (Lt + HX, yc)]
bends = [  # (start, end, label)
    ((RR, 0), (Lt - RR, 0), "1 front: down 90"),
    ((0, RR), (0, Dy), "2 end: down 90"),
    ((Lt, RR), (Lt, Dy), "3 end: down 90"),
    ((-END, y0), (-END, Dy), "4 tab: UP 90 (opposite)"),
    ((Lt + END, y0), (Lt + END, Dy), "5 tab: UP 90 (opposite)"),
    ((XF, -FLAP_G1), (XF, -F), "6 flap: 90 inward"),
    ((Lt - XF, -FLAP_G1), (Lt - XF, -F), "7 flap: 90 inward"),
]

def outline_xy(pts, n=32):
    out = []
    for i, (x, y, b) in enumerate(pts):
        nx, ny, _ = pts[(i + 1) % len(pts)]
        out.append((x, y))
        if b:
            sweep = 4 * math.atan(b)
            ch = math.hypot(nx - x, ny - y)
            r = ch / (2 * math.sin(abs(sweep) / 2))
            mx, my = (x + nx) / 2, (y + ny) / 2
            h = math.sqrt(max(r * r - (ch / 2) ** 2, 0))
            ux, uy = (nx - x) / ch, (ny - y) / ch
            sgn = 1 if (b > 0) == (abs(sweep) < math.pi) else -1
            cx, cy = mx - sgn * uy * h, my + sgn * ux * h
            a0 = math.atan2(y - cy, x - cx)
            for k in range(1, n):
                a = a0 + sweep * k / n
                out.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return out

def write_dxf(path="C13416_cover_v2.dxf"):
    doc = ezdxf.new("R2010", setup=True)
    doc.units = ezdxf.units.IN
    doc.header["$INSUNITS"] = 1
    doc.header["$MEASUREMENT"] = 0
    doc.layers.add("CUT", color=7)
    doc.layers.add("BEND", color=1, linetype="DASHED")
    msp = doc.modelspace()
    msp.add_lwpolyline([(x, y, 0, 0, b) for x, y, b in pts], format="xyseb", close=True,
                       dxfattribs={"layer": "CUT"})
    for x, y in holes:
        msp.add_circle((x, y), HOLE_D / 2, dxfattribs={"layer": "CUT"})
    for s, e, _ in bends:
        msp.add_line(s, e, dxfattribs={"layer": "BEND", "linetype": "DASHED", "ltscale": 0.15})
    doc.saveas(path)

def preview(path="C13416_cover_v2_preview.png"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(13, 5))
    xy = outline_xy(pts); xy.append(xy[0])
    ax.plot(*zip(*xy), color="k", lw=1)
    for x, y in holes:
        ax.add_patch(plt.Circle((x, y), HOLE_D / 2, fill=False, color="k"))
    for s, e, _ in bends:
        ax.plot([s[0], e[0]], [s[1], e[1]], color="k", lw=0.8, dashes=(5, 3))
    for (x, y), t in (((Lt / 2, Dy / 2), "TOP"), ((Lt / 2, -F / 2), "FRONT"),
                      ((-END / 2, Dy / 2), "END"), ((Lt + END / 2, Dy / 2), "END")):
        ax.text(x, y, t, ha="center", va="center", weight="bold")
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(f'C13416 cover v2 flat pattern  {Lt + 2*HX + 2*tr:.3f}" x {Dy + F:.3f}"  '
                 f'(holes {HOLE_CC}" c-c folded)')
    fig.tight_layout(); fig.savefig(path, dpi=130)

if __name__ == "__main__":
    write_dxf(); preview()
    print(f"BD={BD:.4f} Lt={Lt:.3f} END={END:.3f} Dy={Dy:.3f} F={F:.3f} FL={FL:.3f} "
          f"between flap bends={Lt-2*XF:.3f} holes flat={Lt+2*HX:.3f} hole-from-bend={HX-END:.3f} "
          f"tab tip={HX-END+tr:.3f}")
    print(f"flat overall: {Lt + 2*HX + 2*tr:.3f} x {Dy + F:.3f}")
