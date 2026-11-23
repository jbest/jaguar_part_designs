"""1:1 PDF of AUC1054 version A outline alone (US Letter)."""
import importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent          # jaguar_carb_shield_AUC1054/
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
spec = importlib.util.spec_from_file_location("a", HERE / "auc1054_A_v2.py")
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
o, holes = a.build()
W, H = 8.5, 11.0
fig = plt.figure(figsize=(W, H)); ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off"); ax.set_aspect("equal")
minx, miny, maxx, maxy = o.bounds
px, py = W/2, 7.5
x, y = o.exterior.xy
ax.plot([v+px for v in x], [v+py for v in y], "k", lw=0.8)
for hx, hy in holes:
    ax.add_patch(plt.Circle((hx+px, hy+py), a.HOLE_D/2, fill=False, lw=0.8))
    ax.plot([hx+px-0.05, hx+px+0.05], [hy+py]*2, "k", lw=0.3)
    ax.plot([hx+px]*2, [hy+py-0.05, hy+py+0.05], "k", lw=0.3)
ax.text(W/2, 10.35, "AUC1054 starting carburettor dust shield, prototype (version A)",
        ha="center", fontsize=11, weight="bold")
ax.text(W/2, 10.05, "PRINT AT 100% / ACTUAL SIZE. Check the 1.000\" square before using.",
        ha="center", fontsize=8.5)
ax.text(px, py + miny - 0.3,
        f'Hole centres {a.S:.2f}"   Holes Ø{a.HOLE_D:.3f}" (#10)   Ears Ø{2*a.EAR_R:.2f}"   Notch R{a.build.notch_r:.3f}"\n'
        f'Notch to tip {a.NOTCH_TO_TIP:.2f}"   Hole line to tip {a.TIP_L:.2f}"   Tip R{a.TIP_R:.2f}"   '
        f'Overall {maxx-minx:.2f}" × {maxy-miny:.2f}"', ha="center", va="top", fontsize=7.5)
ax.add_patch(plt.Rectangle((0.75, 0.75), 1, 1, fill=False, lw=0.8))
ax.text(1.25, 1.25, '1.000"\nsquare', ha="center", va="center", fontsize=7)
fig.savefig(ROOT / "AUC1054_A_v2_prototype.pdf"); print("ok")
