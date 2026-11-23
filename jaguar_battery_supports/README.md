# Battery box supports — 1959 Jaguar XK 150S (T831957DN)

Two bent sheet-metal supports that sit under the battery in the left and right battery boxes. They have **no individual part numbers**; they are part of the battery box assemblies.

To be cut and bent at SendCutSend. Each is made **longer than needed** so one design works for **both the left and right sides**. They are trimmed to length on assembly.

> **Installer's note:** these templates have **no holes** and are **longer than needed**. Each support must be **cut to length** and have its **holes drilled** on installation. The length and the hole sizes and positions depend on the side (left or right battery box) and on details only the person installing the parts will know, so they are deliberately not part of these designs.

## Status

> **Material that worked:** both supports were originally ordered in **CRS A36/1008 mild steel, 0.074"** (14 ga) from SendCutSend. This worked well for Jason's needs.

**2026-11-22:** The **rear support (hat section) has been ordered** from SendCutSend in 0.074" CRS mild steel, 15.5" × 2.75" flat. The **front support (Z section) has also been ordered**, in the same 0.074" CRS mild steel, 16.5" × 2.25" flat.

## The two supports

### Rear battery support: hat section (4 bends)
**Ordered** from SendCutSend: **CRS A36/1008 mild steel, 0.074"** (14 ga), flat blank **15.5" × 2.75"**.

A hat section: a lip each side, two walls and a flat top. 3D view in `images/rear_support_hat_3d.png`, flat blank in `images/rear_support_hat_flat.png`.

| Item | Value | Source |
|---|---|---|
| Flat blank | **15.498" × 2.750"** measured; ordered as 15.5" × 2.75" (agrees within 0.002") | Measured from the rear flat screenshot grid |
| Material | **CRS A36/1008 mild steel, 0.074"** | As ordered |
| Bend lines (flat, from the top edge) | **0.380, 0.877, 1.879, 2.377** | Measured from the rear flat screenshot grid |
| Strips between bends (flat) | **0.380 / 0.498 / 1.002 / 0.498 / 0.373** (lip / wall / top / wall / lip). Most likely nominal: 0.375 / 0.5 / 1.0 / 0.5 / 0.375 | Measured; nominal is a reading, not confirmed |
| Bends | 4, all **90°**, along the full length. The two outer bends (lip to wall) go one way and the two inner bends (wall to top) go the other, so the lips sit flat and level, pointing out, and the top is parallel to them. See the rear 3D screenshot for direction. | Jason (90°); the rear 3D screenshot |

### Front battery support: Z section (2 bends)
**Ordered** from SendCutSend: **CRS A36/1008 mild steel, 0.074"** (14 ga), flat blank **16.5" × 2.25"**.

A Z section: a narrow flange, a short wall and a wider flange, bent opposite ways. 3D view in `images/front_support_z_3d.png`, flat blank in `images/front_support_z_flat.png`.

| Item | Value | Source |
|---|---|---|
| Flat blank | **16.503" × 2.252"** measured; ordered as 16.5" × 2.25" (agrees within 0.003") | Measured from the front flat screenshot grid |
| Material | **CRS A36/1008 mild steel, 0.074"** | As ordered |
| Bend lines (flat, from the top edge) | **0.623, 1.253** | Measured from the front flat screenshot grid |
| Strips between bends (flat) | **0.623 / 0.630 / 0.999** (narrow flange / wall / wide flange). Most likely nominal: 0.625 / 0.625 / 1.0 | Measured; nominal is a reading, not confirmed |
| Bends | 2, both **90°**, along the full length, in **opposite** directions, so the two flanges are parallel and point opposite ways (Z). See the front 3D screenshot for direction. | Jason (90°); the front 3D screenshot |

### How these were measured
The screenshots are the only record of the sizes and bend positions. `scripts/measure_screenshots.py` measures them from the images alone:
- The scale comes from the faint 1" grid: the average spacing of all the grid lines (160.7 px/in in the rear flat screenshot, 157.2 px/in in the front flat screenshot). The grid line labelled 10" confirms it.
- The outline and the dashed bend lines are found as dark lines and measured against that scale.
- Precision is about ±1 px, which is about ±0.007".

The results were then compared with the ordered specs. The blank sizes agree to within 0.003".

**Where the sizes come from, and their limits:**
- The templates were made by measuring the **original parts directly**, so they likely carry some measurement error.
- The **bend radius was not accounted for.** The measured widths of the original's lip, wall, top and flange were entered as the flat strip widths between bend lines. No bend deduction was applied, so the finished bent part will differ slightly from the original (typically by a fraction of the sheet thickness per bend).
- The bend lines are where SendCutSend shows them on the flat pattern.

## Files (v1)

| File | What it is |
|---|---|
| `battery_support_rear_v1.dxf` | Rear (hat) flat blank, full size, inches. Outline on layer `CUT`, 4 bend lines on layer `BEND`. No holes. |
| `battery_support_front_v1.dxf` | Front (Z) flat blank, full size, inches. Outline on layer `CUT`, 2 bend lines on layer `BEND`. No holes. |
| `battery_support_rear_v1.pdf`, `battery_support_front_v1.pdf` | Drawing on landscape letter. The parts are too long to print full size, so the **flat blank is half size (1:2)** with dimensions. The **end profile is full size (1:1)**, to compare with an original, with a 1" check square. Print at 100% / Actual size. |
| `battery_support_rear_v1_preview.png`, `battery_support_front_v1_preview.png` | PNG previews of the PDFs. |
| `scripts/build_battery_supports.py` | Builds the DXFs, PDFs and PNGs: `python3 scripts/build_battery_supports.py v1` from this folder. Needs `ezdxf` and `matplotlib`. |
| `scripts/measure_screenshots.py` | Measures the blanks and bend lines from the builder screenshots. |

**Values used in v1:** the ordered blank sizes (rear 15.5 × 2.75, front 16.5 × 2.25), with bend lines at the nominal positions the screenshot measurements point to:
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

## Open items

- [x] Blank sizes and bend-line positions measured from the screenshot grids (2026-11-22).
- [x] Bend angles: all 90°. Directions as shown in the 3D screenshots (2026-11-22).
- [x] Bend radius: not accounted for in the templates (measured widths used as flat widths). Documented, no change planned.
- [x] Rear (hat) material: CRS A36/1008 mild steel, 0.074". Ordered 2026-11-22.
- [x] Front (Z) material: CRS A36/1008 mild steel, 0.074". Ordered 2026-11-22.
- [ ] Quantity of each (left + right, spares).
- [x] Ordered straight from SendCutSend's builder, so no DXF was needed (2026-11-22).

## Change log

- **2026-11-22:** v1 DXF, PDF and preview made for both supports (`scripts/build_battery_supports.py`), using the ordered blank sizes and nominal bend lines.
- **2026-11-22:** Documented that 0.074" CRS mild steel was the thickness originally ordered and worked well; that the templates were measured directly from the original parts (likely with some error); and that the bend radius was not accounted for.
- **2026-11-22:** Screenshots renamed by location and view: `rear_support_hat_flat/_3d.png`, `front_support_z_flat/_3d.png` (were `screenshot_00`–`03`).
- **2026-11-22:** All bends recorded as 90°, with directions as shown in the 3D screenshots.
- **2026-11-22:** Holes and final length are left to the installer by design: an installer's note was added, and the open item to record them was removed.
- **2026-11-22:** Measured both blanks and bend-line positions from the screenshot grids (`scripts/measure_screenshots.py`); checked against the ordered specs.
- **2026-11-22:** Screenshot 01/03 identified as the **front** battery support (Z section). Ordered: CRS A36/1008 mild steel 0.074", 16.5" × 2.25" flat.
- **2026-11-22:** Screenshot 00/02 identified as the **rear** battery support (hat section). Ordered: CRS A36/1008 mild steel 0.074", 15.5" × 2.75" flat.
- **2026-11-22:** Folder set up. The four screenshots were renamed (`screenshot_00`–`03`) and moved into `images/`; the macOS names had a hidden special space that the tools couldn't read. README added.
