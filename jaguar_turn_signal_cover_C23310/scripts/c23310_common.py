"""Shared geometry for both halves of the C23310 turn signal switch cover.

Used by build_C23310_cap.py and build_C23310_main_cover.py, so the two halves
always share the same split-face outline, column cutouts and column position.

UNITS: millimeters.

Coordinate system (both halves):
  X = across the column (vertical on the car, + = up)
  Y = along the column; Y = 0 at the dash end, Y = L at the steering-wheel end
  Z = 0 on the split face. The main cover (right of the column) is on +Z,
      the cap (left of the column) on -Z.
"""
import cadquery as cq

# ---------------- SHARED PARAMETERS ----------------
# Split-face outline (from a 1:1 tracing of an original main cover)
W = 74.5            # width across the column, dash-end section
L = 59.0            # length along the column
W_WHEEL = 64.0      # width of the narrower wheel-end section
STEP_Y = 49.5       # where the outline steps in (from the dash end)
R_CORNER = 3.5      # corner radius of the outline, seen square-on (not yet applied)

# Column cutouts (from the tracing). Centers are on the main-cover side (+Z).
CUT_DASH_D = 41.0
CUT_DASH_OFFSET = 1.5
CUT_WHEEL_D = 47.5
CUT_WHEEL_OFFSET = 1.0

# Column and turn signal cancelling cam
COLUMN_OD = 38.1        # 1.5 in, measured
CAM_REACH = 6.35        # cam reaches at most 1/4 in beyond the column (estimate)
CAM_MARGIN = 1.0        # extra clearance
COLUMN_OFFSET = 1.0     # column axis, this far on the main-cover side (+Z)
# ----------------------------------------------------


def rounded_block(w, y0, y1, d, r_side, r_end, round_ends, top=0.0):
    """Block w wide (X) from y0 to y1, z from top-d to top. Rounded on the
    outer-face (bottom) edges along Y and, at the ends listed in round_ends
    ('<Y', '>Y'), on the bottom edge across that end."""
    b = (cq.Workplane("XY").box(w, y1 - y0, d, centered=(True, False, False))
         .translate((0, y0, top - d)))
    b = b.edges("|Y and <Z").fillet(r_side)
    for end in round_ends:
        if r_end > 0:
            b = b.faces(end).edges("<Z").fillet(r_end)
    return b


def outer_solid(d, r_side, r_end):
    """Solid outer shape of a half, built on the -Z side of the split face."""
    wide = rounded_block(W, 0.0, STEP_Y, d, r_side, r_end, ["<Y"])
    narrow = rounded_block(W_WHEEL, STEP_Y - 1.0, L, d, r_side, r_end, [">Y"])
    return wide.union(narrow)


def build_half(d, t, r_side, r_end, side, features=None):
    """Hollow half-cover with column cutouts and cam clearance.

    side = -1 builds the cap (stays on -Z); side = +1 builds the main cover
    (built on -Z, then mirrored to +Z). `features(body)` adds internal bosses
    etc. in the -Z build frame; anything poking outside the outer shape is
    trimmed off.
    """
    outer = outer_solid(d, r_side, r_end)
    inner = (rounded_block(W - 2 * t, t, STEP_Y - t, d - t + 1, r_side - t, 0, [], top=1.0)
             .union(rounded_block(W_WHEEL - 2 * t, STEP_Y - t - 1.0, L - t, d - t + 1,
                                  r_side - t, 0, [], top=1.0)))
    body = outer.cut(inner)
    if features is not None:
        body = features(body).intersect(outer)

    # In the -Z build frame, the main cover's column axis must be at -offset
    # (it becomes +offset after mirroring); the cap's is at +offset.
    s = 1.0 if side < 0 else -1.0
    cam_r = COLUMN_OD / 2 + CAM_REACH + CAM_MARGIN
    body = body.cut(cq.Workplane("XY").cylinder(L - 2 * t, cam_r, direct=(0, 1, 0))
                    .translate((0, L / 2, s * COLUMN_OFFSET)))

    def end_cut(dia, offset, y0, y1):
        return (cq.Workplane("XY").cylinder(y1 - y0, dia / 2, direct=(0, 1, 0))
                .translate((0, (y0 + y1) / 2, s * offset)))

    body = body.cut(end_cut(CUT_DASH_D, CUT_DASH_OFFSET, -1.0, t + 3.0))
    body = body.cut(end_cut(CUT_WHEEL_D, CUT_WHEEL_OFFSET, L - t - 3.0, L + 1.0))
    return body


def mirror_to_main_side(body):
    return body.mirror("XY")


def render(bodies, path, title, views=None):
    """Shaded multi-view preview. bodies = [(cadquery Workplane, (r,g,b)), ...]."""
    import math
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    meshes = []
    for wp, rgb in bodies:
        verts, tris = wp.val().tessellate(0.1, 0.2)
        V = np.array([(v.x, v.y, v.z) for v in verts]); V[:, 1] -= L / 2
        tri = V[np.array(tris)]
        n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
        n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
        meshes.append((tri, n, np.array(rgb)))
    allpts = np.vstack([m[0].reshape(-1, 3) for m in meshes])
    c = (allpts.max(0) + allpts.min(0)) / 2
    lim = (allpts.max(0) - allpts.min(0)).max() / 2 + 2
    views = views or [("View", 30, -60)]
    fig = plt.figure(figsize=(4.6 * len(views), 5.4))
    for i, (vt, elev, azim) in enumerate(views, 1):
        ax = fig.add_subplot(1, len(views), i, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        light = np.array([math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        for tri, n, rgb in meshes:
            shade = 0.3 + 0.7 * np.clip(np.abs(n @ light), 0, 1)
            col = np.clip(np.outer(shade, rgb), 0, 1)
            ax.add_collection3d(Poly3DCollection(tri, facecolors=np.c_[col, np.ones(len(col))],
                                                 edgecolor="none"))
        ax.set_xlim(c[0] - lim, c[0] + lim); ax.set_ylim(c[1] - lim, c[1] + lim)
        ax.set_zlim(c[2] - lim, c[2] + lim)
        ax.set_box_aspect((1, 1, 1)); ax.view_init(elev, azim); ax.set_axis_off()
        ax.set_title(vt, fontsize=11)
    fig.suptitle(title, fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=100)
    plt.close(fig)
