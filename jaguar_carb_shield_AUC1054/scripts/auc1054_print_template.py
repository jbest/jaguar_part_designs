"""True-scale (1:1) printable PDF of one or more AUC1054 variants on US Letter.
Usage (from the part folder):
  python3 scripts/auc1054_print_template.py "A v2:scripts/auc1054_A_v2.py" "B:early_trials/auc1054_B_parallel.py"
Writes AUC1054_paper_prototypes.pdf in the current directory."""
import sys, importlib.util
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def load(path):
    spec = importlib.util.spec_from_file_location(path, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

variants = [a.split(":", 1) for a in sys.argv[1:]]
W, H = 8.5, 11.0
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# 1" calibration square + ruler
ax.add_patch(plt.Rectangle((0.75, 0.75), 1, 1, fill=False, lw=0.8))
ax.text(1.25, 1.25, '1.000" square\ncheck before cutting', ha="center", va="center", fontsize=7)
for i in range(0, 41):
    x = 2.25 + i * 0.125
    ax.plot([x, x], [0.75, 0.75 + (0.2 if i % 8 == 0 else 0.1 if i % 4 == 0 else 0.05)], "k", lw=0.5)
    if i % 8 == 0: ax.text(x, 0.98, f"{i//8}", ha="center", fontsize=7)
ax.plot([2.25, 7.25], [0.75, 0.75], "k", lw=0.5)

ax.text(W/2, H - 0.6, "AUC1054 starting carb dust shield — paper prototypes (print at 100% / Actual size)",
        ha="center", fontsize=10)
n = len(variants)
for i, (label, path) in enumerate(variants):
    m = load(path); o, holes = m.build()
    minx, miny, maxx, maxy = o.bounds
    cx = W * (i + 1) / (n + 1); cy = H/2 + 0.5
    ox, oy = cx - (minx+maxx)/2, cy - (miny+maxy)/2
    x, y = o.exterior.xy
    ax.plot([v+ox for v in x], [v+oy for v in y], "k", lw=0.6)
    for hx, hy in holes:
        ax.add_patch(plt.Circle((hx+ox, hy+oy), m.HOLE_D/2, fill=False, lw=0.6))
        ax.plot([hx+ox-0.04, hx+ox+0.04], [hy+oy]*2, "k", lw=0.3)
        ax.plot([hx+ox]*2, [hy+oy-0.04, hy+oy+0.04], "k", lw=0.3)
    ax.text(cx, oy+miny-0.35, f"{label}\nears Ø{2*m.EAR_R:.3f}\"  notch R{m.build.notch_r:.3f}\"\n"
            f"tip L{m.TIP_L:.2f}\" R{m.TIP_R:.3f}\"  {maxx-minx:.3f}\" × {maxy-miny:.3f}\"",
            ha="center", va="top", fontsize=7)
fig.savefig("AUC1054_paper_prototypes.pdf")
print("ok")
