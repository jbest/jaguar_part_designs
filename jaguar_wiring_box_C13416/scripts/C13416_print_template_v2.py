"""Full-size black-and-white print template for the C13416 cover (US Letter landscape).
Reads geometry from C13416_cover_v2.py in the same folder. Writes C13416_cover_v2_template.pdf.
Rebuilt 2026-11-21 to reproduce jaguar_wiring_shield_C13416.pdf (2026-11-18)."""
import os, io, contextlib, importlib.util
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cover", os.path.join(HERE, "C13416_cover_v2.py"))
with contextlib.redirect_stdout(io.StringIO()):
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT = "C13416_cover_v2_template.pdf"
W, H = 11.0, 8.5
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
K = "k"

xy = c.outline_xy(c.pts)
minx = min(p[0] for p in xy); maxx = max(p[0] for p in xy)
miny = min(p[1] for p in xy); maxy = max(p[1] for p in xy)
ox = (W - (maxx - minx)) / 2 - minx
oy = 4.55 - (maxy - miny) / 2 - miny
P = lambda x, y: (x + ox, y + oy)

xy.append(xy[0])
ax.plot([p[0] + ox for p in xy], [p[1] + oy for p in xy], color=K, lw=0.9)
for x, y in c.holes:
    ax.add_patch(plt.Circle(P(x, y), c.HOLE_D / 2, fill=False, color=K, lw=0.9))
for s, e, lab in c.bends:
    (x1, y1), (x2, y2) = P(*s), P(*e)
    ax.plot([x1, x2], [y1, y2], color=K, lw=0.9, dashes=(5, 3))

FS = 8
def hdim(x1, x2, y, text, ext_from=None):
    ax.annotate("", (x1, y), (x2, y), arrowprops=dict(arrowstyle="<->", color=K, lw=0.6, shrinkA=0, shrinkB=0))
    ax.text((x1 + x2) / 2, y + 0.04, text, ha="center", va="bottom", fontsize=FS)
    if ext_from is not None:
        for x in (x1, x2):
            ax.plot([x, x], [ext_from, y + (0.05 if y > ext_from else -0.05)], color=K, lw=0.4, ls=":")
def vdim(y1, y2, x, text, ext_from=None, side="right"):
    ax.annotate("", (x, y1), (x, y2), arrowprops=dict(arrowstyle="<->", color=K, lw=0.6, shrinkA=0, shrinkB=0))
    ha = "left" if side == "right" else "right"
    ax.text(x + (0.05 if side == "right" else -0.05), (y1 + y2) / 2, text, ha=ha, va="center", fontsize=FS)
    if ext_from is not None:
        for y in (y1, y2):
            ax.plot([ext_from, x + (0.05 if x > ext_from else -0.05)], [y, y], color=K, lw=0.4, ls=":")

Lt, END, HX, F, Dy, XF, FL = c.Lt, c.END, c.HX, c.F, c.Dy, c.XF, c.FL
top_y = oy + Dy
hdim(*[P(x, 0)[0] for x in (-HX, Lt + HX)], top_y + 0.75,
     f'Hole centers {Lt + 2*HX:.3f}" flat  ({c.HOLE_CC:.3f}" when folded)', ext_from=top_y)
hdim(P(-END, 0)[0], P(0, 0)[0], top_y + 0.3, f'{END:.3f}', ext_from=top_y)
hdim(P(0, 0)[0], P(Lt, 0)[0], top_y + 0.3, f'{Lt:.3f}', ext_from=top_y)
hdim(P(Lt, 0)[0], P(Lt + END, 0)[0], top_y + 0.3, f'{END:.3f}', ext_from=top_y)
# tab: bend to hole centre, and bend to tip (left tab)
hy0 = oy + c.y0 - 0.3
hdim(P(-HX, 0)[0], P(-END, 0)[0], hy0, '')
ax.text(P(-HX, 0)[0] - 0.05, hy0, f'{HX-END:.3f} to hole center', ha='right', va='center', fontsize=FS)
for x, y0_ in ((P(-HX, 0)[0], oy + c.yc - 0.12), (P(-END, 0)[0], oy + c.y0)):
    ax.plot([x, x], [y0_, hy0 - 0.05], color=K, lw=0.4, ls=':')
tip = -HX - c.tr
hy1 = hy0 - 0.25
hdim(P(tip, 0)[0], P(-END, 0)[0], hy1, '')
ax.text(P(tip, 0)[0] - 0.05, hy1, f'{HX - END + c.tr:.3f} to tab tip', ha='right', va='center', fontsize=FS)
for x, y0_ in ((P(tip, 0)[0], oy + c.yc - 0.05), (P(-END, 0)[0], hy0)):
    ax.plot([x, x], [y0_, hy1 - 0.05], color=K, lw=0.4, ls=':')
# front face / flaps
bot = oy - F
hdim(P(XF - FL, 0)[0], P(XF, 0)[0], bot - 0.3, f'{FL:.3f}', ext_from=bot)
hdim(P(XF, 0)[0], P(Lt - XF, 0)[0], bot - 0.3, f'{Lt - 2*XF:.3f}', ext_from=bot)
hdim(P(Lt - XF, 0)[0], P(Lt - XF + FL, 0)[0], bot - 0.3, f'{FL:.3f}', ext_from=bot)
xr = P(Lt + HX, 0)[0] + c.tr + 0.35
vdim(oy, oy + Dy, xr, f'{Dy:.3f}', ext_from=P(Lt + END, 0)[0])
vdim(oy - F, oy, xr, f'{F:.3f}', ext_from=P(Lt - XF + FL, 0)[0])
hx, hy = P(-HX, c.yc)
ax.annotate(f'Ø{c.HOLE_D:.2f}" (2×)', (hx - 0.07, hy + 0.07), (hx - 0.55, hy + 0.55),
            fontsize=FS, ha="right", arrowprops=dict(arrowstyle="-", color=K, lw=0.5))

def lab(x, y, t, fs=11, **kw):
    ax.text(*P(x, y), t, ha="center", va="center", fontsize=fs, weight="bold", **kw)
lab(Lt / 2, Dy / 2, "TOP")
lab(Lt / 2, -F / 2, "FRONT")
lab(-END / 2, Dy / 2, "END", fs=9)
lab(Lt + END / 2, Dy / 2, "END", fs=9)
lab(-END - 0.35, c.yc + 0.32, "TAB", fs=8)
lab(Lt + END + 0.35, c.yc + 0.32, "TAB", fs=8)
lab(XF - FL / 2, -F + 0.28, "FLAP", fs=7.5)
lab(Lt - XF + FL / 2, -F + 0.28, "FLAP", fs=7.5)

ax.text(W / 2, 7.75, "Jaguar Wiring Connector Shield - C13416", ha="center", va="center", fontsize=16, weight="bold")
ax.text(W / 2, 7.45, "Prototype flat pattern (full size) for reproducing the original part",
        ha="center", va="center", fontsize=10)

UP = 0.55
ax.add_patch(plt.Rectangle((0.6, 0.55 + UP), 1, 1, fill=False, color=K, lw=0.8))
ax.text(1.1, 1.62 + UP, '1" × 1" scale check', ha="center", fontsize=8)
lx = 2.0
ax.plot([lx, lx + 0.5], [1.55 + UP, 1.55 + UP], color=K, lw=0.9)
ax.text(lx + 0.6, 1.55 + UP, "Cut line", va="center", fontsize=8.5)
ax.plot([lx + 1.7, lx + 2.2], [1.55 + UP, 1.55 + UP], color=K, lw=0.9, dashes=(5, 3))
ax.text(lx + 2.3, 1.55 + UP, "Bend line (center of bend)", va="center", fontsize=8.5)
notes = [
    'PRINT AT 100% / "Actual size". Measure the square: it must be exactly 1".',
    'Fold every dashed line 90°.  FRONT, both ENDs and both FLAPs fold down/inward (same direction).',
    'Both TABs fold the opposite way, so they lie flat on the body.  FLAPs tuck inside the ENDs.',
    'Folded: TOP 5.25" × 2.00", 1.125" clearance under TOP, 0.25" gap under FRONT, open back.  All dimensions in inches (flat).',
    f'18 ga (0.048") steel assumed; flat dimensions include ≈{c.BD:.3f}" bend deduction per bend.',
]
for i, t in enumerate(notes):
    ax.text(lx, 1.25 + UP - i * 0.19, t, fontsize=8.5, va="center")
yc_ = 1.25 + UP - len(notes) * 0.19 - 0.08
ax.text(lx, yc_, "Contact: https://forums.jag-lovers.com/u/trimtab", fontsize=8.5, va="center", weight="bold",
        url="https://forums.jag-lovers.com/u/trimtab")

fig.savefig(OUT)
print("saved", OUT)
