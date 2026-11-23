"""C23310 assembly: main cover + cap + column as separate named bodies in one STEP.

Usage (run from the part folder): python3 scripts/build_C23310_assembly.py v1
Writes C23310_assembly_<ver>.step. Opens in Fusion, Shapr3D etc. as three bodies.
UNITS: millimeters.
"""
import os
import sys
import cadquery as cq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c23310_common import *  # noqa: F401,F403
import build_C23310_cap as cap_mod
import build_C23310_main_cover as main_mod

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"

cap = build_half(cap_mod.D, cap_mod.T, cap_mod.R_SIDE, cap_mod.R_END, side=-1,
                 features=cap_mod.clip_blocks)
main = main_mod.build_main()
column = (cq.Workplane("XY").cylinder(L + 30, COLUMN_OD / 2, direct=(0, 1, 0))
          .translate((0, L / 2, COLUMN_OFFSET)))

assy = cq.Assembly(name=f"C23310_assembly_{VERSION}")
assy.add(main, name="main_cover", color=cq.Color(0.55, 0.62, 0.80))
assy.add(cap, name="cap", color=cq.Color(0.85, 0.85, 0.85))
assy.add(column, name="steering_column_1.5in", color=cq.Color(0.3, 0.3, 0.3))
assy.save(f"C23310_assembly_{VERSION}.step")
print("saved", f"C23310_assembly_{VERSION}.step")
