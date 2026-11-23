import sys, importlib, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent          # jaguar_carb_shield_AUC1054/
"""Photo 3 overlay: A v1 and B outlines to scale on the assembled carb (early trial check).
Writes early_trials/AUC1054_A_v1_B_fit_check.png."""
def load(p):
    s = importlib.util.spec_from_file_location(p.stem, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
from PIL import Image, ImageDraw
import importlib
src = ROOT / 'images' / '03_carb_assembled_top_view.jpg'
# zoomed-crop frame: crop (60,220,380,460) resized x2
cx, cy, ppi = 315, 159, 310.0
tiles = []
for name in ('auc1054_A_v1_1.30long', 'auc1054_B_parallel'):
    a = load(ROOT / 'early_trials' / (name + '.py')); L = a.TIP_L
    o, holes = a.build()
    im = Image.open(src).convert('RGB').crop((60,220,380,540)).resize((640,640)).convert('RGBA')
    ov = Image.new('RGBA', im.size, (0,0,0,0)); d = ImageDraw.Draw(ov)
    pts = [(cx + x*ppi, cy - y*ppi) for x, y in o.exterior.coords]
    d.polygon(pts, fill=(255,200,0,70), outline=(255,220,0,255), width=3)
    for hx, hy in holes:
        r = a.HOLE_D/2*ppi; X, Y = cx+hx*ppi, cy-hy*ppi
        d.ellipse([X-r,Y-r,X+r,Y+r], outline=(0,255,255,255), width=2)
    im = Image.alpha_composite(im, ov).convert('RGB')
    ImageDraw.Draw(im).text((60,45), name.split('_',1)[1], fill=(255,255,0))
    tiles.append(im.crop((40,30,600,640)))
W = sum(t.width for t in tiles)
out = Image.new('RGB', (W, 610))
x = 0
for t in tiles: out.paste(t, (x, 0)); x += t.width
out.save(ROOT / 'early_trials' / 'AUC1054_A_v1_B_fit_check.png')
