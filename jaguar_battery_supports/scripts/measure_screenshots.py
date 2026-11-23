"""Measure the battery-support flat blanks from SendCutSend screenshots, using the 1" grid.
Usage (from the project folder): python3 scripts/measure_screenshots.py
The grid spacing is found from the faint vertical grid lines (1" apart; the line labelled 10"
confirms the scale). Outline and dashed bend lines are found as dark rows/columns.
Precision is about +/-1 px, i.e. about +/-0.007".
"""
from PIL import Image
import numpy as np

def minima(p, thr, sep=3):
    out = []
    for i in range(1, len(p) - 1):
        if p[i] < thr and p[i] <= p[i - 1] and p[i] <= p[i + 1]:
            if out and i - out[-1] < sep:
                continue
            out.append(i)
    return out

for name, f in (("rear (hat)", "images/rear_support_hat_flat.png"), ("front (Z)", "images/front_support_z_flat.png")):
    a = np.asarray(Image.open(f).convert("L")).astype(float)
    h, w = a.shape
    col = a[:, int(w * 0.45):int(w * 0.55)].mean(axis=1)
    rows = minima(col, 160)                  # outline top/bottom + bend lines (dark)
    top, bot, bends = rows[0], rows[-1], rows[1:-1]
    band = a[top + 10:top + 50, :].mean(axis=0)
    vx = minima(band, np.median(band) - 3)   # grid lines + outline ends
    d = np.diff(vx)
    med = np.median(d[d > 100])
    pitch = d[np.abs(d - med) < 3].mean()     # px per inch, averaged over all 1" grid gaps
    ends = [x for x in vx if band[x] < np.median(band) - 40]
    left, right = ends[0], ends[-1]
    L, W = (right - left) / pitch, (bot - top) / pitch
    pos = [(y - top) / pitch for y in bends]
    segs = np.diff([0] + pos + [W])
    print(f"{name}: {f}  grid {pitch:.1f} px/in")
    print(f"  blank {L:.3f} x {W:.3f} in")
    print("  bend lines from top edge:", ", ".join(f"{p:.3f}" for p in pos))
    print("  strips:", " / ".join(f"{s:.3f}" for s in segs))
