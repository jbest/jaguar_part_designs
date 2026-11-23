"""Battery box supports (rear hat section, front Z section), XK 150S.
Builds, for each support: DXF (inches, layers CUT and BEND), PDF drawing and PNG preview.
Usage (run from the project folder; files are written there):
    python3 scripts/build_battery_supports.py v1

Sizes are the ordered specs. They were measured from the original parts and entered in
SendCutSend's builder, and confirmed from the builder screenshots (scripts/measure_screenshots.py)
to within 0.005". Bend lines use the nominal values those measurements point to.
The bend radius is NOT accounted for: the measured widths of the original are used as the
flat widths between bend lines. No holes: the installer cuts to length and drills holes.
"""
import sys
import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
T = 0.074  # CRS A36/1008 mild steel (14 ga), as ordered

PARTS = {
    "rear": dict(
        title="Rear battery support (hat section)",
        L=15.5, W=2.75,
        bends=[0.375, 0.875, 1.875, 2.375],            # from the top edge of the flat blank
        names=["lip", "wall", "top", "wall", "lip"],
        # end profile: direction of each strip (dx, dy), lips out, top raised
        dirs=[(1, 0), (0, 1), (1, 0), (0, -1), (1, 0)],
        bend_dirs="Bends 1 and 4 (lip to wall) one way; bends 2 and 3 (wall to top) the other way.",
        measured="15.498 x 2.750; bend lines 0.380, 0.877, 1.879, 2.377",
    ),
    "front": dict(
        title="Front battery support (Z section)",
        L=16.5, W=2.25,
        bends=[0.625, 1.25],
        names=["narrow flange", "wall", "wide flange"],
        dirs=[(1, 0), (0, -1), (1, 0)],          # narrow flange, wall down, wide flange onward (Z)
        bend_dirs="Bends 1 and 2 go opposite ways (Z): the flanges are parallel and point opposite ways.",
        measured="16.503 x 2.252; bend lines 0.623, 1.253",
    ),
}


def strips(p):
    edges = [0.0] + p["bends"] + [p["W"]]
    return [b - a for a, b in zip(edges, edges[1:])]


def write_dxf(key, p):
    doc = ezdxf.new("R2010", setup=True)
    doc.units = ezdxf.units.IN
    doc.header["$INSUNITS"] = 1
    doc.header["$MEASUREMENT"] = 0
    doc.layers.add("CUT", color=7)
    doc.layers.add("BEND", color=1, linetype="DASHED")
    msp = doc.modelspace()
    L, W = p["L"], p["W"]
    # x along the length, y across; y = 0 at the top edge of the flat (as in the screenshots), down negative
    msp.add_lwpolyline([(0, 0), (L, 0), (L, -W), (0, -W)], close=True, dxfattribs={"layer": "CUT"})
    for b in p["bends"]:
        msp.add_line((0, -b), (L, -b), dxfattribs={"layer": "BEND", "linetype": "DASHED", "ltscale": 0.15})
    name = f"battery_support_{key}_{VERSION}.dxf"
    doc.saveas(name)
    return name


def arrow(ax, p, q, col="0.3"):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="<|-|>", lw=0.5, color=col,
                mutation_scale=6, shrinkA=0, shrinkB=0))


def write_pdf(key, p):
    L, W = p["L"], p["W"]
    S = 0.5  # flat blank drawn at half scale
    fig = plt.figure(figsize=(11, 8.5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 11); ax.set_ylim(0, 8.5); ax.axis("off"); ax.set_aspect("equal")

    ax.text(0.6, 7.95, f"XK 150S {p['title']} - {VERSION}", fontsize=14, weight="bold", va="top")
    notes = [
        f"Material (as ordered, worked well): CRS A36/1008 mild steel, {T:.3f}\" (14 ga). All bends 90°.",
        p["bend_dirs"],
        "NO HOLES and LONGER THAN NEEDED: cut to length and drill holes on installation (depends on side / installer).",
        "Measured from the original parts (likely some error). Bend radius NOT accounted for: measured widths used as flat widths.",
        f"Check: builder screenshot measures {p['measured']}.   Units: inches.",
    ]
    for i, t in enumerate(notes):
        ax.text(0.6, 7.55 - i * 0.22, t, fontsize=8.5, va="top")

    # ---- flat blank, half scale ----
    ox, oy = (11 - L * S) / 2, 5.55
    ax.text(ox, oy + 0.35, "FLAT BLANK  -  scale 1:2 (half size)", fontsize=9, weight="bold")
    ax.add_patch(Rectangle((ox, oy - W * S), L * S, W * S, fill=False, lw=0.8))
    for i, b in enumerate(p["bends"]):
        y = oy - b * S
        ax.plot([ox, ox + L * S], [y, y], color="k", lw=0.6, dashes=(5, 3))
        ax.text(ox + L * S + 0.08, y, f"bend {i + 1}", fontsize=7, va="center")
    # strip widths on the left
    edges = [0.0] + p["bends"] + [W]
    xd = ox - 0.25
    for (a, b), nm in zip(zip(edges, edges[1:]), p["names"]):
        arrow(ax, (xd, oy - a * S), (xd, oy - b * S))
        ax.text(xd - 0.06, oy - (a + b) / 2 * S, f"{b - a:.3f} {nm}", fontsize=7, ha="right", va="center")
    # overall
    yl = oy - W * S - 0.3
    arrow(ax, (ox, yl), (ox + L * S, yl))
    ax.text(ox + L * S / 2, yl - 0.08, f"{L:.3f}  (longer than needed; cut to length)", fontsize=8, ha="center", va="top")
    xw = ox + L * S + 0.8
    arrow(ax, (xw, oy), (xw, oy - W * S))
    ax.text(xw + 0.06, oy - W * S / 2, f"{W:.3f}", fontsize=8, va="center")

    # ---- end profile, full size ----
    px, py = 3.2, 1.2
    ax.text(0.6, 3.05, "END PROFILE  -  FULL SIZE (1:1), sharp corners, bend radius not shown", fontsize=9, weight="bold")
    x, y = 0.0, 0.0
    pts = [(x, y)]
    for s_, (dx, dy) in zip(strips(p), p["dirs"]):
        x, y = x + dx * s_, y + dy * s_
        pts.append((x, y))
    minx = min(q[0] for q in pts); miny = min(q[1] for q in pts)
    pts = [(px + q[0] - minx, py + q[1] - miny) for q in pts]
    lw_pt = T * 72
    ax.plot(*zip(*pts), color="0.15", lw=lw_pt, solid_joinstyle="miter", solid_capstyle="butt")
    ys = [q[1] for q in pts]; xs = [q[0] for q in pts]
    ymid, xmid = (max(ys) + min(ys)) / 2, (max(xs) + min(xs)) / 2
    for (a, b), s_, nm in zip(zip(pts, pts[1:]), strips(p), p["names"]):
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        if abs(a[1] - b[1]) < 1e-9:   # horizontal strip: label above if it's the upper level, else below
            if my >= ymid:
                ax.text(mx, my + 0.1, f"{s_:.3f} {nm}", fontsize=7, ha="center", va="bottom")
            else:
                ax.text(mx, my - 0.1, f"{s_:.3f} {nm}", fontsize=7, ha="center", va="top")
        else:                          # vertical strip: label on the outside
            if mx <= xmid:
                ax.text(mx - 0.1, my, f"{s_:.3f} {nm}", fontsize=7, ha="right", va="center")
            else:
                ax.text(mx + 0.1, my, f"{s_:.3f} {nm}", fontsize=7, ha="left", va="center")
    ax.text(px + 3.4, py + 0.4, "Lay an original's end on this profile to compare.\n"
            "Widths are flat widths between bend lines;\nthe bent part differs slightly (bend radius).",
            fontsize=7.5, va="center")

    # check square and print note
    ax.add_patch(Rectangle((9.4, 0.6), 1.0, 1.0, fill=False, lw=0.6))
    ax.text(9.9, 0.48, "1.000 in check square", fontsize=7, ha="center", va="top")
    ax.text(0.6, 0.45, "Print at 100% / Actual size, landscape. The end profile and check square are full size;\n"
            "the flat blank is half size. The DXF is full size.", fontsize=7.5, va="bottom")

    base = f"battery_support_{key}_{VERSION}"
    fig.savefig(base + ".pdf")
    fig.savefig(base + "_preview.png", dpi=110)
    plt.close(fig)
    return base


if __name__ == "__main__":
    for key, p in PARTS.items():
        d = write_dxf(key, p)
        b = write_pdf(key, p)
        print(key, d, b, "strips", [round(s, 3) for s in strips(p)])
