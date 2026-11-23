"""
AUC1054 version A v2 (FINAL) - Starting carburettor dust shield, Jaguar XK150S
Parametric flat-pattern generator for SendCutSend (DXF, inches, 1:1).

Coordinate frame: hole centres on the X axis at (+/- S/2, 0), tip pointing -Y.
Edit the PARAMETERS block and re-run:  python3 scripts/auc1054_A_v2.py
Writes AUC1054_A_v2.dxf and AUC1054_A_v2_preview.png in the part folder.
"""
import math
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent          # jaguar_carb_shield_AUC1054/
import ezdxf
from shapely.geometry import Point, Polygon, box
from shapely.ops import unary_union

# ---------------- PARAMETERS (inches) ----------------
S        = 0.870   # hole centre-to-centre            MEASURED
HOLE_D   = 0.201   # #10 screw, free-fit clearance (#7 drill)  SET
EAR_R    = 0.185   # ear radius (0.37" ears)
NOTCH_TO_TIP = 0.750  # bottom of notch to end of point (KEY DIM)  from photo of original
TIP_R    = 0.220   # radius at the point                        from photo of original
TIP_L    = (S/2 - EAR_R) + NOTCH_TO_TIP   # hole line to end of point (derived)
NUT_W    = 0.370   # max nut size, centred between holes  MEASURED
NUT_CLR  = 0.025   # radial clearance around the nut
# -----------------------------------------------------

RES = 256  # arc segments per quarter circle (smooth polyline for the cutter)

def build():
    lh, rh = (-S/2, 0.0), (S/2, 0.0)
    ears = [Point(lh).buffer(EAR_R, RES), Point(rh).buffer(EAR_R, RES)]
    TIP_Y = TIP_L - TIP_R
    tip = Point(0, -TIP_Y).buffer(TIP_R, RES)
    body = unary_union(ears + [tip]).convex_hull

    # Ears stay fully round above the hole line and run straight into a round notch.
    lower = body.intersection(box(-5, -5, 5, 0))
    # Notch radius chosen so the notch is tangent to both ear circles at the hole
    # line: ear curve flows straight into the notch as one smooth S-curve.
    nr = S/2 - EAR_R
    assert nr >= NUT_W/2, "ears too large: notch would not clear the nut"
    shape = unary_union([lower] + ears).difference(Point(0, 0).buffer(nr, RES))
    shape = shape.buffer(-0.02, RES).buffer(0.02, RES)
    shape = Polygon(max(getattr(shape, "geoms", [shape]), key=lambda g: g.area).exterior)
    build.notch_r = nr
    return Polygon(shape.exterior), (lh, rh)

def write_dxf(outline, holes, path):
    doc = ezdxf.new("R2010", setup=True)
    doc.units = ezdxf.units.IN
    doc.header["$INSUNITS"] = 1
    msp = doc.modelspace()
    msp.add_lwpolyline(list(outline.exterior.coords)[:-1], close=True)
    for c in holes:
        msp.add_circle(c, HOLE_D / 2)
    doc.saveas(path)

def preview(outline, holes, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 7))
    x, y = outline.exterior.xy
    ax.fill(x, y, color="#c9ced3", ec="k", lw=1.2)
    for c in holes:
        ax.add_patch(plt.Circle(c, HOLE_D/2, fc="white", ec="k", lw=1.2))
    minx, miny, maxx, maxy = outline.bounds
    ax.set_aspect("equal"); ax.grid(True, lw=0.3, alpha=0.5)
    ax.set_xlim(minx - 0.25, maxx + 0.45); ax.set_ylim(miny - 0.2, maxy + 0.45)
    ax.annotate("", (-S/2, 0.43), (S/2, 0.28+0.15), arrowprops=dict(arrowstyle="<->"))
    ax.text(0, 0.46, f'{S:.3f}" C-C (measured)', ha="center")
    ax.annotate("", (maxx + 0.12, 0), (maxx + 0.12, -TIP_L), arrowprops=dict(arrowstyle="<->"))
    ax.text(maxx + 0.15, -TIP_L/2, f'{TIP_L:.2f}"', va="center")
    ax.text(0, -TIP_L + TIP_R + 0.03, f'R{TIP_R:.3f}"', ha="center", fontsize=8)
    ax.add_patch(plt.Circle((0, 0), NUT_W/2, fc="none", ec="C3", ls="--"))
    ax.text(0, -NUT_W/2 - NUT_CLR - 0.04, f'{NUT_W:.2f}" nut (dashed)\nnotch R{build.notch_r:.3f}"',
            color="C3", fontsize=8, ha="center", va="top")
    ax.text(-S/2 - 0.05, EAR_R + 0.06, f'Ø{HOLE_D:.3f}" (#10 clr)\near Ø{2*EAR_R:.2f}"',
            ha="center", va="bottom", fontsize=8)
    ax.set_title(f'AUC1054 A v2 dust shield — {maxx-minx:.3f}" × {maxy-miny:.3f}"')
    ax.set_xlabel("inches")
    fig.tight_layout(); fig.savefig(path, dpi=150)

if __name__ == "__main__":
    outline, holes = build()
    write_dxf(outline, holes, ROOT / "AUC1054_A_v2.dxf")
    preview(outline, holes, ROOT / "AUC1054_A_v2_preview.png")
    minx, miny, maxx, maxy = outline.bounds
    print(f'Bounding box: {maxx-minx:.3f}" x {maxy-miny:.3f}"')
