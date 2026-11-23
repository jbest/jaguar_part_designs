"""Radiator tie strap/stay (460-043 pair), XK 150S. Builds DXF (inches), 1:1 PDF and PNG preview.
Usage (run from the project folder; files are written there):
    python3 scripts/build_460-043_radiator_strap.py v1 original
    python3 scripts/build_460-043_radiator_strap.py v1 long
  Each version has two variants:
    original: the original part's measurements.
    long:     1/8" (0.125) longer overall; the slot starts the same distance from the end
              but is also 0.125 longer. The round hole stays the same distance from its end.
  v1: same geometry as the original strap.dxf (8.875 x 0.76, R0.38 ends, 0.27 x 1.00 slot,
      0.27 hole), rebuilt as closed polylines. The two small holes of the original part are
      shown on the PDF for reference only and are NOT in the DXF.
"""
import sys
import ezdxf
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
VARIANT = sys.argv[2] if len(sys.argv) > 2 else "original"
EXTRA = {"original": 0.0, "long": 0.125}[VARIANT]   # added to overall length and slot length
NAME = f"460-043_radiator_strap_{VERSION}_{VARIANT}"
FRAC = {"original": "8-7/8", "long": "9"}[VARIANT]

# ---- geometry (inches) ----
# Origin: x = 0 at the slot end of the strap, y = 0 on the centreline.
L, W = 8.875 + EXTRA, 0.76  # overall length (original 8-7/8) and width
R = W / 2                   # full-radius ends
THK = 0.14                  # thickness, from the sketch
SW = 0.27                   # slot width
SX0, SX1 = 0.25, 1.25 + EXTRA  # slot extent along the strap (original 1.00 long, 1/4 from the end)
HOLE = 0.27                 # hole at the far end
HX = L - R                  # concentric with the end radius (0.38 from the end)

# Holes on the ORIGINAL part only (probably for the bonnet-rod retainer bracket, LH stay). Not cut.
# Each: (x from the slot end, y from the centreline (+ = top edge on the PDF), diameter)
# Known so far (2026-11-22): both 0.20 dia; first hole centre 2.47 from the slot end;
# 0.88 centre to centre between them. Sideways positions not known yet: to be re-measured.
REF_HOLE_DIA = 0.20
REF_HOLE1_X = 2.47
REF_HOLE_CC = 0.88
REF_HOLES = []               # add (x, y, dia) once re-measured; then they are drawn on the PDF

outer = [(R, -R, 0), (L - R, -R, 1.0), (L - R, R, 0), (R, R, 1.0)]
sr = SW / 2
slot = [(SX0 + sr, -sr, 0), (SX1 - sr, -sr, 1.0), (SX1 - sr, sr, 0), (SX0 + sr, sr, 1.0)]

# ---- DXF ----
doc = ezdxf.new("R2010", setup=True)
doc.units = ezdxf.units.IN
doc.header["$MEASUREMENT"] = 0
msp = doc.modelspace()
for prof in (outer, slot):
    msp.add_lwpolyline([(x, y, 0, 0, b) for x, y, b in prof], format="xyseb", close=True)
msp.add_circle((HX, 0), HOLE / 2)
doc.saveas(f"{NAME}.dxf")

# ---- PDF, letter landscape, true scale ----
def stadium(x0, x1, r, n=181):
    t1 = np.linspace(-np.pi / 2, np.pi / 2, n); t2 = np.linspace(np.pi / 2, 3 * np.pi / 2, n)
    xs = np.concatenate([x1 + r * np.cos(t1), x0 + r * np.cos(t2), [x1]])
    ys = np.concatenate([r * np.sin(t1), r * np.sin(t2), [-r]])
    return xs, ys

fig = plt.figure(figsize=(11, 8.5))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 11); ax.set_ylim(0, 8.5); ax.axis("off"); ax.set_aspect("equal")
ox, oy = 1.0, 4.4
G, RED, BLUE, DIM = "black", "#C0392B", "#2E6DB4", "0.3"

xs, ys = stadium(R, L - R, R); ax.plot(xs + ox, ys + oy, color=G, lw=0.6)
xs, ys = stadium(SX0 + sr, SX1 - sr, sr); ax.plot(xs + ox, ys + oy, color=RED, lw=0.6)
ax.add_patch(Circle((ox + HX, oy), HOLE / 2, fill=False, color=RED, lw=0.6))
for x, y, d in REF_HOLES:
    ax.add_patch(Circle((ox + x, oy + y), d / 2, fill=False, color=BLUE, lw=0.6, ls="--"))
    ax.plot([ox + x - 0.06, ox + x + 0.06], [oy + y, oy + y], color=BLUE, lw=0.3)
    ax.plot([ox + x, ox + x], [oy + y - 0.06, oy + y + 0.06], color=BLUE, lw=0.3)

def arrow(p, q, col=DIM):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="<|-|>", lw=0.5, color=col,
                mutation_scale=6, shrinkA=0, shrinkB=0))

def hdim(x0, x1, y, text, col=DIM, ext_from=None):
    arrow((ox + x0, oy + y), (ox + x1, oy + y), col)
    for x in (x0, x1):
        y0 = ext_from if ext_from is not None else 0
        ax.plot([ox + x, ox + x], [oy + y0, oy + y + (0.08 if y > 0 else -0.08)], lw=0.3, color="0.5", ls=":")
    ax.text(ox + (x0 + x1) / 2, oy + y + (0.08 if y > 0 else -0.1), text, fontsize=8,
            ha="center", va="bottom" if y > 0 else "top", color=col)

# overall length and width
hdim(0, L, -R - 0.55, f"{L:.3f} ({FRAC})")
xW = L + 0.3
arrow((ox + xW, oy - R), (ox + xW, oy + R))
ax.text(ox + xW + 0.06, oy, f"{W:.2f}", fontsize=8, va="center")
# slot
hdim(0, SX0, -R - 0.25, f"{SX0:.2f}", RED)
hdim(SX0, SX1, R + 0.25, f"slot {SX1 - SX0:.3f} x {SW:.2f} wide", RED)
# far hole
hdim(HX, L, R + 0.25, f"{L - HX:.2f}", RED)
ax.annotate(f"Ø{HOLE:.2f} (concentric with end R{R:.2f})", xy=(ox + HX - 0.1, oy + 0.1),
            xytext=(ox + HX - 2.6, oy + R + 0.6), fontsize=8, color=RED,
            arrowprops=dict(arrowstyle="-|>", lw=0.5, color=RED, mutation_scale=6))

notes = [
    f"XK 150S radiator tie strap (460-043 pair) - {VERSION} {VARIANT}",
    "",
    f"Overall: {L:.3f} ({FRAC}) x {W:.2f}, full-radius ends R{R:.2f}"
    + ("" if VARIANT == "original" else "   [long variant: original + 1/8]"),
    f"Slot: {SX1 - SX0:.3f} x {SW:.2f}, starts {SX0:.2f} (1/4) from the end, on the centreline",
    f"Hole: {HOLE:.2f} dia, {L - HX:.2f} from the other end, on the centreline",
    f"Thickness: {THK:.2f} in (from sketch)",
    "Units: inches",
]
for i, t in enumerate(notes):
    ax.text(0.75, 7.9 - i * 0.22, t, fontsize=11 if i == 0 else 8.5,
            weight="bold" if i == 0 else "normal", va="top")
ax.text(0.75, 2.9, "Original part (reference only, NOT cut, not in the DXF): two small holes, "
        f"\u00d8{REF_HOLE_DIA:.2f},\nprobably for the bonnet-rod retainer bracket (LH stay). First hole centre {REF_HOLE1_X:.2f} from the slot end; "
        f"{REF_HOLE_CC:.2f} centre to centre.\nSideways positions to be re-measured.",
        fontsize=8, color=BLUE, va="top")
if REF_HOLES:
    ax.text(0.75, 2.2, "Blue dashed holes: on the original part only (probably the bonnet-rod retainer bracket).\n"
            "NOT in the DXF; not cut.", fontsize=8, color=BLUE, va="top")

ax.add_patch(Rectangle((9.0, 0.9), 1.0, 1.0, fill=False, lw=0.6))
ax.text(9.5, 0.75, "1.000 in check square", fontsize=7.5, ha="center", va="top")
ax.text(0.75, 0.9, "Print at 100% / Actual size (no 'fit to page'), landscape.\n"
        "Measure the check square before laying the original on the print.",
        fontsize=7.5, va="bottom")
fig.savefig(f"{NAME}.pdf")
fig.savefig(f"{NAME}_preview.png", dpi=110)
print(NAME, "L", L, "W", W, "slot", SX0, SX1, SW, "hole", HX, HOLE, "ref holes", REF_HOLES)
