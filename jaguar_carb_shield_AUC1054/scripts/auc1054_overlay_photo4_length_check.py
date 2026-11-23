import sys, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent          # jaguar_carb_shield_AUC1054/
"""Photo 4 overlay: A v1 vs A v2 to scale on the original part. Writes AUC1054_A_v2_length_check.png."""
from PIL import Image, ImageDraw
def load(p):
    s=importlib.util.spec_from_file_location(p,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
L=(400,132.5); R=(647.5,70)
mx,my=(L[0]+R[0])/2,(L[1]+R[1])/2
dx,dy=R[0]-L[0],R[1]-L[1]; d=(dx*dx+dy*dy)**.5
u=(dx/d,dy/d); n=(-u[1],u[0]); s=d/0.87
def P(x,y): return (mx+s*(x*u[0]-y*n[0]), my+s*(x*u[1]-y*n[1]))
tiles=[]
for lab,tl,tr in (("A v1 (1.30)",1.30,0.15),("A v2: notch-to-tip 0.75, R0.22",1.00,0.22)):
    m=load(str(HERE / 'auc1054_A_v2.py')); m.TIP_L=tl; m.TIP_R=tr
    o,h=m.build()
    im=Image.open(ROOT / 'images' / '04_original_part_overhead.webp').convert('RGBA')
    ov=Image.new('RGBA',im.size,(0,0,0,0)); dr=ImageDraw.Draw(ov)
    dr.line([P(x,y) for x,y in o.exterior.coords],fill=(255,0,200,255),width=3)
    for hx,hy in h:
        r=m.HOLE_D/2*s; X,Y=P(hx,hy); dr.ellipse([X-r,Y-r,X+r,Y+r],outline=(0,200,255,255),width=2)
    im=Image.alpha_composite(im,ov).convert('RGB').crop((300,0,780,480))
    ImageDraw.Draw(im).text((10,455),lab,fill=(255,0,200))
    tiles.append(im)
out=Image.new('RGB',(960,480)); out.paste(tiles[0],(0,0)); out.paste(tiles[1],(480,0))
out.save(ROOT / 'AUC1054_A_v2_length_check.png')
print('px/in',round(s,1))
