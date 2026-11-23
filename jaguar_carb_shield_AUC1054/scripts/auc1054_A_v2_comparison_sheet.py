"""1:1 comparison sheet: AUC1054 version A outline + empty 0.1" measuring grid (US Letter)."""
import importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent          # jaguar_carb_shield_AUC1054/
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

spec = importlib.util.spec_from_file_location("a", HERE / "auc1054_A_v2.py")
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
outline, holes = a.build()

W, H = 8.5, 11.0
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
ax.set_aspect("equal")
K = dict(color="k")

ax.text(W/2, 10.35, "Jaguar XK150 starting carburettor dust shield (AUC1054): comparison sheet",
        ha="center", fontsize=11, weight="bold")
ax.text(W/2, 10.05, "PRINT AT 100% / ACTUAL SIZE (not \"Fit to page\"). Check the 1.000\" square "
        "and the grid before using.", ha="center", fontsize=8.5)

# ---------- Left: reference outline, version A, full size ----------
px, py = 1.85, 7.6           # position of the midpoint between the hole centres
minx, miny, maxx, maxy = outline.bounds
x, y = outline.exterior.xy
ax.plot([v+px for v in x], [v+py for v in y], lw=0.8, **K)
for hx, hy in holes:
    ax.add_patch(plt.Circle((hx+px, hy+py), a.HOLE_D/2, fill=False, lw=0.8))
    for d in ((-0.05, 0), (0.05, 0)):
        ax.plot([hx+px-0.05, hx+px+0.05], [hy+py]*2, lw=0.3, **K)
        ax.plot([hx+px]*2, [hy+py-0.05, hy+py+0.05], lw=0.3, **K)
# dimension lines
def dim(x1, y1, x2, y2, label, tx, ty, ha="center", va="center"):
    ax.annotate("", (x1, y1), (x2, y2), arrowprops=dict(arrowstyle="<->", lw=0.5))
    ax.text(tx, ty, label, fontsize=6.5, ha=ha, va=va)
hy = py + maxy + 0.15
dim(px-a.S/2, hy, px+a.S/2, hy, f'{a.S:.2f}" hole centres', px, hy+0.08)
ax.plot([px-a.S/2]*2, [py, hy+0.03], lw=0.3, ls=":", **K)
ax.plot([px+a.S/2]*2, [py, hy+0.03], lw=0.3, ls=":", **K)
dx = px + maxx + 0.18
nb = py - a.build.notch_r                     # bottom of notch
dim(dx, nb, dx, py-a.TIP_L, f'{a.NOTCH_TO_TIP:.2f}"\nnotch\nto tip', dx+0.06, (nb+py-a.TIP_L)/2, ha="left")
ax.plot([px, dx+0.03], [nb, nb], lw=0.3, ls=":", **K)
ax.plot([px, dx+0.03], [py-a.TIP_L]*2, lw=0.3, ls=":", **K)
by = py + miny - 0.2
dim(px+minx, by, px+maxx, by, f'{maxx-minx:.2f}" overall width', px, by-0.1)
ax.text(px, by-0.35,
        f'Holes Ø{a.HOLE_D:.3f}" (#10)\nEars Ø{2*a.EAR_R:.2f}"   Notch R{a.build.notch_r:.3f}"\n'
        f'Hole line to tip {a.TIP_L:.2f}"   Tip R{a.TIP_R:.2f}"\nOverall {maxx-minx:.2f}" × {maxy-miny:.2f}"',
        ha="center", va="top", fontsize=6.5)
ax.text(px, py + maxy + 0.55, "PROTOTYPE OUTLINE (full size)", ha="center", fontsize=8, weight="bold")

# ---------- Right: empty 0.1" grid ----------
gx0, gy0, GW, GH = 4.0, 5.6, 3.0, 3.0      # inches
n_x, n_y = round(GW*10), round(GH*10)
for i in range(n_x + 1):
    lw, c = (0.9, "0.0") if i % 10 == 0 else (0.5, "0.35") if i % 5 == 0 else (0.25, "0.6")
    ax.plot([gx0 + i/10]*2, [gy0, gy0+GH], lw=lw, color=c)
    if i % 5 == 0:
        lab = f"{i/10:g}"
        ax.text(gx0 + i/10, gy0 - 0.08, lab, ha="center", va="top", fontsize=6)
        ax.text(gx0 + i/10, gy0 + GH + 0.06, lab, ha="center", va="bottom", fontsize=6)
for j in range(n_y + 1):
    lw, c = (0.9, "0.0") if j % 10 == 0 else (0.5, "0.35") if j % 5 == 0 else (0.25, "0.6")
    ax.plot([gx0, gx0+GW], [gy0 + j/10]*2, lw=lw, color=c)
    if j % 5 == 0:
        lab = f"{j/10:g}"
        ax.text(gx0 - 0.07, gy0 + j/10, lab, ha="right", va="center", fontsize=6)
        ax.text(gx0 + GW + 0.07, gy0 + j/10, lab, ha="left", va="center", fontsize=6)
ax.text(gx0 + GW/2, gy0 + GH + 0.3, "MEASURING GRID: 0.1\" squares, heavy lines every 1\"",
        ha="center", fontsize=8, weight="bold")
ax.text(gx0 + GW/2, gy0 - 0.3, "inches", ha="center", va="top", fontsize=6.5)

# calibration square + 5" ruler
ax.add_patch(plt.Rectangle((0.75, 3.75), 1, 1, fill=False, lw=0.8))
ax.text(1.25, 4.25, '1.000"\nsquare', ha="center", va="center", fontsize=7)
fig.savefig(ROOT / "AUC1054_A_v2_comparison_sheet.pdf")
print("ok")
