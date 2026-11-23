"""Turn signal switch cover C23310: the cap half (left side of the column).

Usage (run from the part folder): python3 scripts/build_C23310_cap.py v1
Writes to the current folder:
  C23310_cap_<ver>.step / .stl          the cap
  C23310_cap_<ver>_rim_test.stl         the cap's bottom RIM_TEST_H mm only, a
                                        quick print to check the outline
                                        against the real main cover
  C23310_cap_<ver>_preview.png
Needs cadquery, numpy and matplotlib. Shared outline, cutouts and column
values are in c23310_common.py (also used by the main cover script).

UNITS: millimeters. 25.4 mm = 1 in.

v1 DRAFT. Outline and cutouts traced from an original main cover; depth,
wall, outer rounding and the attachment blocks are estimates.
Print with the outer face down on the bed (open side up).
"""
import os
import sys
import cadquery as cq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c23310_common import *  # noqa: F401,F403

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"

# ---------------- CAP PARAMETERS (estimates, to be measured) ----------------
D = 28.5            # depth from the split face to the outer face (min ~28 to keep 2.5 mm under the wheel-end cutout)
T = 2.5             # wall thickness
R_SIDE = 11.0       # outer rounding where the top/bottom walls meet the outer face
R_END = 3.0         # outer rounding on the edges at each column end

# Attachment: placeholder blocks for spring clips, near the U-strap ears'
# open slots (main cover posts about 43 mm from the dash end, about 7 mm in
# from the top and bottom walls). Positions to be confirmed.
CLIP_Y = 43.0
CLIP_IN = 7.0               # center, in from the outer wall
CLIP_BLOCK = (9.0, 12.0)    # (X, Y) size
CLIP_TOP = -3.0             # Z of the block top
CLIP_PILOT_D = 2.5

RIM_TEST_H = 6.0            # height of the rim-test slice
# -----------------------------------------------------------------------------


def clip_blocks(body):
    for sx in (-1, 1):
        cx = sx * (W / 2 - CLIP_IN)
        h = (D - T) + CLIP_TOP + 0.5
        blk = (cq.Workplane("XY").workplane(offset=-(D - T) - 0.5)
               .center(cx, CLIP_Y).rect(*CLIP_BLOCK).extrude(h))
        hole = (cq.Workplane("XY").workplane(offset=CLIP_TOP - 8.0)
                .center(cx, CLIP_Y).circle(CLIP_PILOT_D / 2).extrude(8.0))
        body = body.union(blk).cut(hole)
    return body


if __name__ == "__main__":
    body = build_half(D, T, R_SIDE, R_END, side=-1, features=clip_blocks)
    name = f"C23310_cap_{VERSION}"
    cq.exporters.export(body, f"{name}.step")
    cq.exporters.export(body, f"{name}.stl", tolerance=0.05, angularTolerance=0.1)

    rim = body.intersect(cq.Workplane("XY").box(W + 10, L + 10, RIM_TEST_H,
                                                centered=(True, False, False))
                         .translate((0, -5, -RIM_TEST_H)))
    cq.exporters.export(rim, f"{name}_rim_test.stl", tolerance=0.05, angularTolerance=0.1)

    render([(body, (0.75, 0.75, 0.78))], f"{name}_preview.png",
           f"C23310 turn signal cover, cap half (left of column): {VERSION} DRAFT\n"
           f"Outline {W} × {L} mm (wheel end {W_WHEEL}), cutouts Ø{CUT_DASH_D} dash / "
           f"Ø{CUT_WHEEL_D} wheel from tracing; depth {D} mm and attachment estimated",
           views=[("Open side (split face)", 70, -60), ("Outer face", -60, -60),
                  ("Dash end", 5, -90), ("Wheel end", 5, 90)])
    bb = body.val().BoundingBox()
    print(name, f"bbox {bb.xlen:.1f} x {bb.ylen:.1f} x {bb.zlen:.1f} mm, "
          f"valid={body.val().isValid()}, volume {body.val().Volume():.0f} mm3; "
          f"rim test volume {rim.val().Volume():.0f} mm3")
