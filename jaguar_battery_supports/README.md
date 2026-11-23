# Battery box supports — 1959 Jaguar XK 150S (T831957DN)

Two bent sheet-metal supports that sit under the battery in the left and right battery boxes. They have **no individual part numbers**; they are part of the battery box assemblies.

Made for SendCutSend cut + bend. Each is **longer than needed** so one design works for **both the left and right sides**; they are trimmed to length on assembly.

> **Installer's note:** these templates have **no holes** and are **longer than needed**. Each support must be **cut to length** and have its **holes drilled** on installation. The length and the hole sizes and positions depend on the side (left or right battery box) and on the individual car, so they are deliberately not part of these designs.

## Status

Both supports have been made from these dimensions by SendCutSend in **CRS A36/1008 mild steel, 0.074"** (14 ga), which proved a suitable material.

## The two supports

### Rear battery support: hat section (4 bends)

A hat section: a lip each side, two walls and a flat top. 3D view in `images/rear_support_hat_3d.png`, flat blank in `images/rear_support_hat_flat.png`.

| Item | Value | Source |
|---|---|---|
| Flat blank | **15.5" × 2.75"** (measured from the screenshot: 15.498" × 2.750") | SendCutSend part spec; screenshot grid |
| Material | **CRS A36/1008 mild steel, 0.074"** | Material used |
| Bend lines (flat, from the top edge) | **0.380, 0.877, 1.879, 2.377** | Measured from the rear flat screenshot grid |
| Strips between bends (flat) | **0.380 / 0.498 / 1.002 / 0.498 / 0.373** (lip / wall / top / wall / lip). Most likely nominal: 0.375 / 0.5 / 1.0 / 0.5 / 0.375 | Measured; the nominal values are a best reading, not confirmed |
| Bends | 4, all **90°**, along the full length. The two outer bends (lip to wall) go one way and the two inner bends (wall to top) go the other, so the lips sit flat and level, pointing out, and the top is parallel to them. See the rear 3D screenshot for direction. | Rear 3D screenshot |

### Front battery support: Z section (2 bends)

A Z section: a narrow flange, a short wall and a wider flange, bent opposite ways. 3D view in `images/front_support_z_3d.png`, flat blank in `images/front_support_z_flat.png`.

| Item | Value | Source |
|---|---|---|
| Flat blank | **16.5" × 2.25"** (measured from the screenshot: 16.503" × 2.252") | SendCutSend part spec; screenshot grid |
| Material | **CRS A36/1008 mild steel, 0.074"** | Material used |
| Bend lines (flat, from the top edge) | **0.623, 1.253** | Measured from the front flat screenshot grid |
| Strips between bends (flat) | **0.623 / 0.630 / 0.999** (narrow flange / wall / wide flange). Most likely nominal: 0.625 / 0.625 / 1.0 | Measured; the nominal values are a best reading, not confirmed |
| Bends | 2, both **90°**, along the full length, in **opposite** directions, so the two flanges are parallel and point opposite ways (Z). See the front 3D screenshot for direction. | Front 3D screenshot |

### Where the dimensions come from

The original parts were measured directly and the parts were set up in SendCutSend's online part builder. The four builder screenshots in `images/` are the record of those designs; the DXFs here were rebuilt from them.

**Limits:**
- Measurements of the original parts likely carry some error.
- The **bend radius was not accounted for.** The measured widths of the original's lip, wall, top and flange were used directly as the flat strip widths between bend lines. No bend deduction was applied, so the finished bent part differs slightly from the original (typically by a fraction of the sheet thickness per bend).
- The bend lines are where SendCutSend shows them on the flat pattern.

`scripts/measure_screenshots.py` measures the blanks and bend lines from the screenshots:
- The scale comes from the faint 1" grid: the average spacing of all the grid lines (160.7 px/in in the rear flat screenshot, 157.2 px/in in the front flat screenshot). The grid line labeled 10" confirms it.
- The outline and the dashed bend lines are found as dark lines and measured against that scale.
- Precision is about ±1 px, which is about ±0.007". The blank sizes agree with the SendCutSend part specs to within 0.003".

## Files (v1)

| File | What it is |
|---|---|
| `battery_support_rear_v1.dxf` | Rear (hat) flat blank, full size, inches. Outline on layer `CUT`, 4 bend lines on layer `BEND`. No holes. |
| `battery_support_front_v1.dxf` | Front (Z) flat blank, full size, inches. Outline on layer `CUT`, 2 bend lines on layer `BEND`. No holes. |
| `battery_support_rear_v1.pdf`, `battery_support_front_v1.pdf` | Drawing on landscape letter. The parts are too long to print full size, so the **flat blank is half size (1:2)** with dimensions. The **end profile is full size (1:1)**, to compare with an original, with a 1" check square. Print at 100% / Actual size. |
| `battery_support_rear_v1_preview.png`, `battery_support_front_v1_preview.png` | PNG previews of the PDFs. |
| `scripts/build_battery_supports.py` | Builds the DXFs, PDFs and PNGs: `python3 scripts/build_battery_supports.py v1` from this folder. Needs `ezdxf` and `matplotlib`. |
| `scripts/measure_screenshots.py` | Measures the blanks and bend lines from the builder screenshots. |

> **The scripts are optional.** The DXF, PDF template and preview files in this folder are ready to use as they are. The scripts are only needed if those files have to be modified and regenerated.

**Values used in v1:** the blank sizes above (rear 15.5 × 2.75, front 16.5 × 2.25), with bend lines at the nominal positions the screenshot measurements point to:
- rear: 0.375, 0.875, 1.875, 2.375 from the top edge
- front: 0.625, 1.25 from the top edge

These are within 0.005" of the measured positions, inside the ±0.007" measuring precision.

## Images (`images/`)

| File | What it shows |
|---|---|
| `rear_support_hat_flat.png` | Rear support (hat): SendCutSend flat blank with 4 bend lines |
| `front_support_z_flat.png` | Front support (Z): SendCutSend flat blank with 2 bend lines |
| `rear_support_hat_3d.png` | Rear support (hat): 3D view of the bent part |
| `front_support_z_3d.png` | Front support (Z): 3D view of the bent part |

## Version history

- **v1 (2026-11-22):** DXFs, PDFs and previews for both supports, rebuilt from the SendCutSend builder screenshots with nominal bend lines.
