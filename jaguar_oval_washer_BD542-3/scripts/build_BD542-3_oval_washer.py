"""Oval washer BD542/3, XK 150S. Builds DXF (inches), 1:1 PDF and PNG preview.
Usage: python3 build_BD542-3_oval_washer.py [v1]   (run from the project folder; files are written there)
  v1: 0.75 x 1.50 stadium (full-radius ends R0.375), 0.27 hole centred both ways.
      Width set to nominal 0.75 (sketch measured 0.76).
"""
import sys
import math
import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
NAME = f"BD542-3_oval_washer_{VERSION}"

# ---- geometry (inches), origin at washer centre ----
W, L = 0.75, 1.50          # overall width / length (sketch measured 0.76)
R = W / 2                  # full-radius ends
H = L / 2 - R              # half the straight-side length (0.37)
HOLE = 0.27                # hole diameter, centred both ways
THK = 0.06                 # material thickness (from sketch)

# outer profile, CCW, (x, y, bulge to next vertex); bulge 1 = 180 deg arc
outer = [
    (R, -H, 0),            # right side, line up
    (R, H, 1.0),           # top end arc
    (-R, H, 0),            # left side, line down
    (-R, -H, 1.0),         # bottom end arc
]

# ---- DXF ----
doc = ezdxf.new("R2010", setup=True)
doc.units = ezdxf.units.IN
doc.header["$MEASUREMENT"] = 0
msp = doc.modelspace()
msp.add_lwpolyline([(x, y, 0, 0, b) for x, y, b in outer], format="xyseb", close=True)
msp.add_circle((0, 0), HOLE / 2)
doc.saveas(f"{NAME}.dxf")

# ---- PDF, letter, true scale ----
fig = plt.figure(figsize=(8.5, 11))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 8.5); ax.set_ylim(0, 11); ax.axis("off")
ax.set_aspect("equal")
ox, oy = 4.25, 6.0         # washer centre on the page
G, RED, DIM = "black", "#C0392B", "0.3"

import numpy as np
t1 = np.linspace(0, np.pi, 181); t2 = np.linspace(np.pi, 2 * np.pi, 181)
xs = np.concatenate([R * np.cos(t1), R * np.cos(t2), [R]])
ys = np.concatenate([H + R * np.sin(t1), -H + R * np.sin(t2), [H]])
ax.plot(xs + ox, ys + oy, color=G, lw=0.6)
ax.add_patch(Circle((ox, oy), HOLE / 2, fill=False, color=RED, lw=0.6))
# centre marks
for dx, dy in [(1, 0), (0, 1)]:
    ax.plot([ox - 0.08 * dx, ox + 0.08 * dx], [oy - 0.08 * dy, oy + 0.08 * dy], color="0.5", lw=0.3)

def arrow(p, q, col=DIM):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="<|-|>", lw=0.5, color=col,
                mutation_scale=6, shrinkA=0, shrinkB=0))

# length
xL = ox + R + 0.35
arrow((xL, oy - L / 2), (xL, oy + L / 2))
for y in (oy - L / 2, oy + L / 2):
    ax.plot([ox + 0.05, xL + 0.1], [y, y], lw=0.3, color="0.5", ls=":")
ax.text(xL + 0.06, oy, f"{L:.2f}", fontsize=8, va="center")
# width
yW = oy - L / 2 - 0.35
arrow((ox - R, yW), (ox + R, yW))
for x in (ox - R, ox + R):
    ax.plot([x, x], [yW - 0.1, oy - H], lw=0.3, color="0.5", ls=":")
ax.text(ox, yW - 0.13, f"{W:.2f}", fontsize=8, ha="center", va="center")
# hole
ax.annotate(f"Ø{HOLE:.2f} thru, centred", xy=(ox - HOLE / 2 * 0.707, oy + HOLE / 2 * 0.707),
            xytext=(ox - R - 1.6, oy + 0.45), fontsize=8, color=RED,
            arrowprops=dict(arrowstyle="-|>", lw=0.5, color=RED, mutation_scale=6))
# end radius
ax.annotate(f"R{R:g} (full radius)", xy=(ox + R * 0.707, oy + H + R * 0.707),
            xytext=(ox + R + 0.25, oy + L / 2 + 0.3), fontsize=8,
            arrowprops=dict(arrowstyle="-|>", lw=0.5, color=DIM, mutation_scale=6))

notes = [
    f"XK 150S oval washer (BD542/3) - {VERSION}",
    "",
    f"Overall: {W:.2f} wide x {L:.2f} long, full-radius ends (R{R:g})",
    f"Straight sides: {2 * H:g}",
    f"Hole: {HOLE:.2f} dia, centred both ways",
    f"Thickness: {THK:.2f} in (from sketch)",
    "Units: inches",
]
for i, t in enumerate(notes):
    ax.text(0.75, 10.2 - i * 0.22, t, fontsize=11 if i == 0 else 8.5,
            weight="bold" if i == 0 else "normal", va="top")

ax.add_patch(Rectangle((5.75, 1.0), 1.0, 1.0, fill=False, lw=0.6))
ax.text(6.25, 0.85, "1.000 in check square", fontsize=7.5, ha="center", va="top")
ax.text(0.75, 1.0, "Print at 100% / Actual size (no 'fit to page').\n"
        "Measure the check square before laying the original on the print.",
        fontsize=7.5, va="bottom")
fig.savefig(f"{NAME}.pdf")
fig.savefig(f"{NAME}_preview.png", dpi=110)
print(NAME, "W", W, "L", L, "R", R, "straight", round(2 * H, 3), "hole", HOLE)
