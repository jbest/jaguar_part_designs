"""Turn signal switch cover C23310: the main cover (right side of the column),
modeled from the original for fit testing with the cap.

Usage (run from the part folder): python3 scripts/build_C23310_main_cover.py v1
Writes to the current folder:
  C23310_main_cover_<ver>.step / .stl
  C23310_assembly_<ver>_preview.png     main cover + cap around the column
Needs cadquery, numpy and matplotlib, and build_C23310_cap.py beside it
(the assembly uses the cap's current parameters).

UNITS: millimeters. 25.4 mm = 1 in.

v1 DRAFT. Shares the split-face outline, column cutouts and column position
with the cap (c23310_common.py), so the two halves always match at the split
face. The depth, outer rounding, stalk hole and the bosses and posts inside
are ESTIMATES from photos; the original is die-cast zinc.
Print with the outer face down on the bed (open side up).
"""
import os
import sys
import cadquery as cq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c23310_common import *  # noqa: F401,F403

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"

# ---------------- MAIN COVER PARAMETERS (estimates from photos) ----------------
D_MAIN = 45.0       # depth from the split face to the outer (right-hand) face
T_MAIN = 2.5        # wall thickness
R_SIDE_MAIN = 20.0  # outer rounding along the top and bottom (deep U profile)
R_END_MAIN = 3.0

# Turn signal stalk hole in the outer face: an oval slot
STALK_Y = 38.0      # center, from the dash end
STALK_LEN = 27.0    # long axis, across the column (X)
STALK_W = 9.0       # short axis, along the column (Y)

# Notch at the top of the dash-end column cutout (from the tracing)
NOTCH_W = 8.3
NOTCH_H = 6.0       # beyond the cutout's apex

# Inside, above and below the column, about 7 mm in from the wall:
BOSS_IN = 7.0
BOSS_Y = 29.0       # threaded bosses for the U-strap screws
BOSS_OD, BOSS_HOLE = 7.0, 3.3
POST_Y = 43.0       # plain posts
POST_D = 6.5
BOSS_TOP = 1.5      # bosses and posts stop this far below the split face
# --------------------------------------------------------------------------------


def bosses(body):
    """Bosses and posts, in the -Z build frame (mirrored to +Z later)."""
    h = D_MAIN - BOSS_TOP
    for sx in (-1, 1):
        x = sx * (W / 2 - BOSS_IN)
        boss = (cq.Workplane("XY").workplane(offset=-D_MAIN).center(x, BOSS_Y)
                .circle(BOSS_OD / 2).extrude(h))
        hole = (cq.Workplane("XY").workplane(offset=-BOSS_TOP - 15).center(x, BOSS_Y)
                .circle(BOSS_HOLE / 2).extrude(15))
        post = (cq.Workplane("XY").workplane(offset=-D_MAIN).center(x, POST_Y)
                .circle(POST_D / 2).extrude(h))
        body = body.union(boss).union(post).cut(hole)
    return body


def build_main():
    body = build_half(D_MAIN, T_MAIN, R_SIDE_MAIN, R_END_MAIN, side=+1, features=bosses)
    # Stalk hole through the outer face (bottom of the -Z build frame).
    slot = (cq.Workplane("XY").workplane(offset=-D_MAIN - 1).center(0, STALK_Y)
            .slot2D(STALK_LEN, STALK_W, angle=0).extrude(T_MAIN + 4))
    body = body.cut(slot)
    # Notch at the apex of the dash-end cutout (in the build frame the apex is
    # at z = -(offset + r)).
    apex = CUT_DASH_OFFSET + CUT_DASH_D / 2
    notch = (cq.Workplane("XZ", origin=(0, T_MAIN + 2, 0))
             .center(0, -(apex + NOTCH_H / 2 - NOTCH_W / 4))
             .slot2D(NOTCH_H + NOTCH_W / 2, NOTCH_W, angle=90).extrude(T_MAIN + 4))
    body = body.cut(notch)
    return mirror_to_main_side(body)


if __name__ == "__main__":
    import build_C23310_cap as cap_mod

    main = build_main()
    name = f"C23310_main_cover_{VERSION}"
    cq.exporters.export(main, f"{name}.step")
    cq.exporters.export(main, f"{name}.stl", tolerance=0.05, angularTolerance=0.1)

    cap = build_half(cap_mod.D, cap_mod.T, cap_mod.R_SIDE, cap_mod.R_END, side=-1,
                     features=cap_mod.clip_blocks)
    column = (cq.Workplane("XY").cylinder(L + 30, COLUMN_OD / 2, direct=(0, 1, 0))
              .translate((0, L / 2, COLUMN_OFFSET)))
    overlap = main.intersect(cap).val().Volume()
    col_main = main.intersect(column).val().Volume()
    col_cap = cap.intersect(column).val().Volume()

    render([(main, (0.55, 0.62, 0.80)), (cap, (0.85, 0.85, 0.85)), (column, (0.35, 0.35, 0.35))],
           f"C23310_assembly_{VERSION}_preview.png",
           f"C23310 turn signal cover {VERSION}: main cover (blue, right) + cap (gray, left) "
           f"around the Ø{COLUMN_OD} column\nShared outline and cutouts from the tracing; "
           f"main cover depth, stalk hole and bosses estimated from photos",
           views=[("From the left (cap side)", 15, -150), ("From the dash end", 0, -90),
                  ("From the wheel end", 0, 90), ("Main cover, from the right", 15, 30)])
    render([(main, (0.55, 0.62, 0.80))], f"{name}_preview.png",
           f"C23310 main cover (right of column): {VERSION} DRAFT for fit testing",
           views=[("Open side (split face)", -70, -60), ("Outer face (stalk hole)", 60, -60),
                  ("Dash end", 0, -90), ("Wheel end", 0, 90)])
    bb = main.val().BoundingBox()
    print(name, f"bbox {bb.xlen:.1f} x {bb.ylen:.1f} x {bb.zlen:.1f} mm, valid={main.val().isValid()}")
    print(f"overlap main/cap {overlap:.2f} mm3, main/column {col_main:.2f} mm3, cap/column {col_cap:.2f} mm3")
