# AUC1054 Starting Carburetor Dust Shield: Jaguar XK150S

Flat-pattern cut file for a replacement of Jaguar part **AUC1054**, the small sheet-metal dust shield on the starting (cold-start) carburetor. Two #10 screws clamp the shield on top of the small plate on the carb, one each side of the needle adjusting nut. The pointed body hangs down and partly covers the three air holes, keeping out dust and stopping a backfire from hitting the bonnet. The tip runs under the float chamber.

All dimensions are in **inches**. The DXFs are drawn full size (1:1).

## Current version

> **Version A v2, `AUC1054_A_v2.dxf`.** The closest match to the original part so far.

One dimension is uncertain:
- **Notch-to-tip length.** 0.75" in the file, measured from a near-overhead photo of an original (photo 04). A photo of a boxed original (photo 05) reads about 0.80". The bent ears may make overhead photos read slightly short. If you can measure a real part, update `NOTCH_TO_TIP` in `scripts/auc1054_A_v2.py` and regenerate, and please share the measurement.

## Ordering notes

| Item | Value |
|---|---|
| **Cut file** | `AUC1054_A_v2.dxf` |
| Material used | **5052-H32 aluminum, 1 mm (0.039")**, the thinnest SendCutSend offers in 5052 |
| Size SendCutSend should report | **1.24" × 1.19"** (1.240 × 1.185). Set units to **inches** if asked; any other size means the units were read wrong. |
| Bending | **By hand, after cutting** (see below). SendCutSend can't bend this part: it is smaller than their 0.375" × 1.5" minimum for bending. |

The original part appears to be thin plated steel (about 22 ga, 0.030"). The aluminum is slightly thicker, won't rust, and bends easily by hand.

### Before uploading
- The DXF header says inches, but also carries a metric measurement flag. Check the reported size matches the table above.
- The ring between each hole and the edge of its ear is 0.085" wide, about twice the sheet thickness. It comes from the original part. If SendCutSend flags anything, it will be this.
- The outline is a smooth polyline of about 3,600 short segments rather than true arcs. That cuts fine.

### Bending (by hand)
The original has its ears bent up out of the plane of the body, along a line roughly through the bottom of the notch. The DXF is the flat blank only. Form the bend after cutting, for example in a vise with a block. Because of the bend, the flat blank is slightly longer than the part looks from above.

## Fixed dimensions (shared by all versions)

| Feature | Value | Source |
|---|---|---|
| Hole center to center | 0.870" | Measured on the car |
| Hole diameter | 0.201" (#10 free-fit clearance, #7 drill) | Set for #10 screws |
| Ear diameter | 0.370" | Chosen by test-fitting on photos |
| Notch | Round, R0.250", centered on the hole line, tangent to both ears | Derived from the ears |
| Nut to be cleared | 0.37" max, centered between holes | Measured |
| Nut clearance | ~0.065" per side | Result of the notch size |

The notch radius is fixed by the geometry: it equals the hole spacing ÷ 2 minus the ear radius. At that radius each ear's curve flows straight into the notch as one smooth S-curve. Changing the ear size changes the notch automatically.

## A v2 dimensions
- **Notch bottom to tip:** **0.75"** (the key dimension; see the uncertainty above)
- **Hole line to tip:** 1.00" (derived)
- **Tip radius:** 0.22"
- **Overall size:** 1.24" × 1.185"
- **Fit check:** matches a near-overhead photo of an original part all the way round (`AUC1054_A_v2_length_check.png`)

## Folder layout

```
jaguar_carb_shield_AUC1054/
  README.md                            this file
  AUC1054_A_v2.dxf                     cut file (current)
  AUC1054_A_v2_prototype.pdf           1:1 print of the outline, with a 1" check square
  AUC1054_A_v2_comparison_sheet.pdf    1:1 outline beside an empty 0.1" grid, for photographing an original on
  AUC1054_A_v2_preview.png             dimensioned preview
  AUC1054_A_v2_length_check.png        A v1 vs A v2 drawn on photo 04; the basis for the A v2 length
  scripts/                             generators for the files above (see below)
  early_trials/                        superseded and experimental versions
  images/                              source photos, numbered
```

### scripts/
Run from anywhere; outputs land in the right place. Need `ezdxf`, `shapely` and `matplotlib` (and `Pillow` for the overlays).

> **The scripts are optional.** The DXF, PDF template and preview files in this folder are ready to use as they are. The scripts are only needed if those files have to be modified and regenerated.

| Script | Writes |
|---|---|
| `auc1054_A_v2.py` | `AUC1054_A_v2.dxf`, `AUC1054_A_v2_preview.png`. Edit its PARAMETERS block to change the design. |
| `auc1054_A_v2_prototype_pdf.py` | `AUC1054_A_v2_prototype.pdf` |
| `auc1054_A_v2_comparison_sheet.py` | `AUC1054_A_v2_comparison_sheet.pdf` |
| `auc1054_overlay_photo4_length_check.py` | `AUC1054_A_v2_length_check.png` |
| `auc1054_overlay_photo3_fit_check.py` | `early_trials/AUC1054_A_v1_B_fit_check.png`. Needs photo 03, which is not in the repository. |
| `auc1054_print_template.py` | `AUC1054_paper_prototypes.pdf` in the current directory, any mix of versions side by side. Example: `python3 scripts/auc1054_print_template.py "A v2:scripts/auc1054_A_v2.py" "B:early_trials/auc1054_B_parallel.py"` |

### early_trials/

| File | What it is |
|---|---|
| `AUC1054_A_v1_1.30long.dxf`, `.py`, `_preview.png` | **A v1, superseded.** Same as A v2 but hole line to tip 1.30" with an R0.15 tip (1.24" × 1.49"). About 0.3" longer than the original. |
| `AUC1054_B_parallel.dxf`, `.py`, `_preview.png` | **B, experimental.** Sides run parallel to 0.82" below the hole line, then taper to a point 1.30" from the hole line (R0.15 tip, R0.12 shoulders). Not updated to the A v2 length. |
| `AUC1054_A_v1_B_paper_prototypes.pdf` | A v1 and B side by side at 1:1, for paper test fits |
| `AUC1054_A_v1_B_fit_check.png` | A v1 and B drawn to scale on photo 03 |

### images/

| File | What it shows |
|---|---|
| `00_hand_sketch.jpg` | Hand sketch: 0.87" hole spacing, #10 screws, 22 ga (not in the repository) |
| `01_vendor_photo_AUC1054.png` | SNG Barratt product photo of the shield, strongly angled |
| `02_carb_mounting_face_disassembled.jpg` | Carb mounting face with nothing fitted (not in the repository) |
| `03_carb_assembled_top_view.jpg` | Carb assembled, from above; background for the A v1 / B fit check (not in the repository) |
| `04_original_part_overhead.webp` | Moss Motors WZX1282 kit photo: shield near overhead; the basis for the A v2 length |
| `05_original_part_in_BL_box.jpg` | Jag-Lovers forum photo: original shield in a BL box; suggests notch-to-tip ~0.80" |

#### Image sources

| File | Downloaded | Source page | Image URL |
|---|---|---|---|
| `01_vendor_photo_AUC1054.png` | 2026-11-15 | SNG Barratt, [sngbarratt.com](https://www.sngbarratt.com/) (product page not recorded) | https://cdn.sngbarratt.com/images/products/500/aa9df287-44be-44f9-a442-5fa310a1e715.png |
| `04_original_part_overhead.webp` | 2026-11-18 | Moss Motors, [WZX1282 thermo dust shield kit](https://mossmotors.com/wzx1282-thermo-dust-shield-kit) | https://mossmotors.com/media/catalog/product/W/Z/WZX1282_1.jpg |
| `05_original_part_in_BL_box.jpg` | 2026-11-18 | Jag-Lovers forum, [forums.jag-lovers.com](https://forums.jag-lovers.com/) (thread not recorded) | https://discourse-cdn.jag-lovers.com/optimized/3X/c/5/c5b66f5910d5429926f5b5135d94bd9dd917e8f6_2_1338x1000.jpeg |

## Version history
- **A v2 (2026-11-21):** Hole line to tip shortened to 1.00" (notch to tip 0.75"), tip R0.22, to match photo 04. Regenerating from the script reproduces the DXF exactly.
- **A v1 and B (2026-11-15 to 18):** A v1 (1.30" long) and B (parallel sides) developed and paper-tested. A v1 proved about 0.3" too long.
