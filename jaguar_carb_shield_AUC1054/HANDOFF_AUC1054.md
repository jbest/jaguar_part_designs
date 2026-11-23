# Handoff: AUC1054 dust shield project (Jaguar XK150S starting carburettor)

**Purpose of this document:** hand the project to another Claude session (Claude Desktop) so it can organize the files and versions without having to rebuild the history. It records:
- which images were used and what each one told us
- how the outlines were compared against the photos
- every design decision, in order
- an inventory of every file, with its status

**Owner:** Jason Best. The part is for his 1959 Jaguar XK 150S.
**Work dates:** 2026-11-15 to 2026-11-21.
**Goal:** a flat-pattern DXF to order AUC1054 from SendCutSend.
**Companion file:** `README.md`, a short user-facing summary of the versions.

> **Update 2026-11-21 (Claude Desktop session): folder reorganized and order details decided.**
> - **Material:** 5052-H32 aluminum, 1 mm (0.039"), quantity 10, from SendCutSend.
> - **Bending:** Jason will bend the ears by hand. SendCutSend's minimum part size for bending is 0.375" × 1.5", larger than this part.
> - **Files renamed and moved.** The README's "Folder layout" section is now the current file inventory. Section 6 below records the names as they were at handoff; the mapping is in section 6.1.
> - **Correction to section 6:** the `AUC1054_A_original.dxf` that was in Jason's folder was **not** A v2. It was byte-identical to `AUC1054_A_v1_1.30long.dxf` (1.24" × 1.485"). It's now `early_trials/AUC1054_A_v1_1.30long.dxf`. The A v2-geometry copies (`AUC1054_A_original.dxf` and `AUC1054_dust_shield.dxf` inside the zip) and `auc1054.py` were duplicates and were not extracted; they remain only in `archive/AUC1054_dust_shield_handoff.zip`.
> - All scripts now use paths relative to their own location and were tested. Regenerating A v2 reproduces `AUC1054_A_v2.dxf` exactly.

---

## 1. Current status (read this first)

- **FINAL design: Version A v2.** The cut file is `AUC1054_A_v2.dxf`.
- **Open items before ordering:**
  1. **Notch-to-tip length (`NOTCH_TO_TIP`).**
     - The current value is **0.75"**, from source photo 4 (section 3).
     - Source photo 5 suggested about **0.80"**. Jason was asked whether to change it but hasn't decided.
     - He feels this dimension is the key to getting the part right.
     - A comparison sheet was made so someone with an original part can photograph it on a grid. Their measurement should settle the length.
  2. ~~**Material and thickness.**~~ **Decided 2026-11-21:** 5052-H32 aluminum, 1 mm. The original looks like thin plated steel (zinc or tin finish); Jason's sketch notes 22 ga.
  3. **The bend.**
     - The original has its ears bent up, out of the plane of the body. The bend line runs roughly through the bottom of the notch.
     - The DXF is the flat blank only, and the bend is formed by hand after cutting. **Confirmed 2026-11-21:** Jason will bend them himself.
     - Possible correction: photos taken from above make the bent part look slightly short. The true flat notch-to-tip distance may therefore be slightly more than the photo readings.
- Jason has said he may still make **minor changes** to the ear and notch end.

---

## 2. Geometry definition (version A v2)

**Coordinate frame**
- Both hole centres sit on the X axis, at (±S/2, 0). The point is at −Y. Units are inches.

**Parameters** (the PARAMETERS block in `auc1054_A_original.py`)

| Parameter | Value | Status / origin |
|---|---|---|
| `S` (hole spacing) | 0.870 | **Measured** by Jason on the car |
| `HOLE_D` | 0.201 | Set: free-fit clearance for a #10 screw (#7 drill) |
| `EAR_R` | 0.185 (0.37" ears) | Chosen by Jason after trying 0.50, 0.45, 0.40, 0.35 and 0.37 |
| `NUT_W` | 0.370 | **Measured** by Jason: the largest nut in the notch, centred between the holes. It's the needle adjusting nut. |
| `NUT_CLR` | 0.025 | Minimum clearance used as a check only. The actual clearance is about 0.065" per side. |
| `NOTCH_TO_TIP` | 0.750 | From photo 4. This is the key dimension, still to be confirmed. |
| `TIP_R` | 0.220 | From photo 4 |
| `TIP_L` | derived = (S/2 − EAR_R) + NOTCH_TO_TIP = 1.000 | Distance from the hole line to the end of the point |

**How the shape is built** (shapely, then written out with ezdxf)
1. Take the convex hull of the two ear circles and the tip circle.
2. Keep only the part below the hole line, then add the two full ear circles back on.
3. Subtract a notch circle centred at (0, 0) with radius **S/2 − EAR_R**, which is 0.250 here. That radius makes the notch tangent to both ear circles at the hole line, so each ear's curve flows straight into the notch as one smooth S-curve. Jason asked for exactly that. A larger notch cuts into the ears and leaves sharp hooks.
4. Soften the corners with a buffer of −0.02 then +0.02.
5. Write the DXF as one closed LWPOLYLINE (the outline) plus two CIRCLEs (the holes). Units are inches ($INSUNITS = 1), the format is R2010, and arcs are tessellated at 256 segments per quarter circle.

**Resulting size:** 1.240" × 1.185".

**Version B** uses the same construction, with two changes:
- A box `[-(S/2+EAR_R), -SHOULDER] .. [S/2+EAR_R, 0]` is added before the hull is taken, so the sides run parallel down to the shoulder.
- The shoulders are then rounded with `SHOULDER_R` (a −r/+r buffer).
- Values: `SHOULDER` = 0.82, `SHOULDER_R` = 0.12, `TIP_L` = 1.30, `TIP_R` = 0.15.

---

## 3. Source images

Jason supplied all of these in chat. Their paths in the cloud workspace were under `/mnt/user-data/uploads/`. In the handoff bundle they are copied into `images/` under descriptive names.

| # | Bundle name | Original name | What it shows | Used for |
|---|---|---|---|---|
| 1 | `01_vendor_photo_AUC1054.png` | jaguar_carb_shield_AUC1054.png (500×500) | A vendor or catalogue photo of the shield alone, on white, with a watermark. Shot at a strong angle (the holes look oval). | The first outline shape: two round ears, a notch, a long point. A perspective-corrected length estimate from this photo (1.70") was **wrong**. See section 4. |
| 2 | `02_carb_mounting_face_disassembled.jpg` | IMG_9848_Medium.jpeg (480×640) | The starting-carb mounting face with nothing fitted: two screw holes, a central bore with a shiny ring and a dark ring, and three large air holes below. Close to head-on. Same orientation as the model (holes at the top). | Scale from the 0.87" holes. Readings: shiny ring about 0.37"; dark ring about 0.54"; top plate about 1.2" wide with ears about 0.33"; bottom of the casting about 0.8" below the hole line. |
| 3 | `03_carb_assembled_top_view.jpg` | IMG_9851_Medium.jpeg (480×640) | The same carb assembled, seen from above: needle through the adjusting nut, small plate, two slotted screws, the three air holes, and the float chamber in the foreground. | The **main fit-check background**. Outlines were drawn to scale on it to choose the ear and notch sizes, and the length at that stage (A v1). Jason explained the tip runs **under the float chamber**. |
| 4 | `04_original_part_overhead.webp` | WZX1282_1.webp (800×800) | An original or new-old-stock shield alone, with screws, star washers and a clip, on fabric. Near overhead, holes almost round. The ears are bent and show as a shiny band. | **Set the A v2 length.** Notch to tip about 0.75" (hole line to tip about 1.00"), tip radius about 0.22". The ears, holes and notch matched the A geometry. |
| 5 | `05_original_part_in_BL_box.jpg` | c5b66f5910d5429926f5b5135d94bd9dd917e8f6_2_1338x1000.jpeg (1338×1000) | A British Leyland "Leycare" box labelled AUC 8121 (needle kit), with the needle assembly, a clip and the shield. The shield lies **flat on its body with the ears bent up**. Small and oblique. | A cross-check on length: notch to tip about **0.80"**. Not yet applied. |

---

## 4. Measurement and comparison methods

### 4.1 Scaling every photo from the hole spacing
Every photo was scaled from the **0.87" hole centre-to-centre** spacing, the only dimension measured on the real car. The method:
- Overlay a pixel grid on a crop of the photo (PIL, red lines every 20–25 px).
- Read off the pixel positions of the two hole centres.
- Pixels per inch = pixel distance between the centres ÷ 0.87.
- Measure other distances along the hole-line direction, or perpendicular to it (projection onto the unit normal).

### 4.2 Photo 1: perspective correction (abandoned)
- The holes look like ellipses, so the part is tilted toward the camera.
- I estimated the tilt from the hole aspect ratio and corrected the vertical axis. That gave hole line to tip ≈ **1.70"**.
- Jason judged it too long. Later photos confirmed it: the true value is about 1.0". The photo is too oblique and too unreliable for this kind of correction.

### 4.3 Photo 3: to-scale overlay (`work/overlay.py`)
- **Frame:** crop the image at (60, 220, 380, 540) and enlarge it 2× to 640×640.
- **Placement:** the midpoint between the holes sits at (315, 159) in the enlarged frame, at about **310 px/in**.
- **Drawing:** the outline is filled yellow with a yellow edge, and the holes are cyan circles.
- **Rotation:** none. The photo is axis-aligned with the model.
- **Used to compare:**
  - lengths 0.90", 1.10" and 1.30" (Jason picked 1.30" so the tip goes under the float chamber)
  - ears of 0.40", 0.35" and 0.37"
  - A against B
- **Output:** `AUC1054_fit_check.png`. The latest version shows A v1 against B.

### 4.4 Photo 4: rotated to-scale overlay (`work/overlay2.py`)
- **Hole centres in the original image pixels:** left (400, 132.5), right (647.5, 70). That's 255.3 px apart, giving **293.4 px/in**.
- **Rotation:** the hole line is tilted about 14° (unit vector u from L to R). The model's −Y runs along the normal n.
- **Mapping:** image = midpoint + s·(x·u − y·n).
- **Result:** the outline drawn in magenta and the holes in cyan.
  - A v1 (1.30", R0.15) overshoots the real tip by about 0.3".
  - A 1.00" outline with an R0.22 tip traces the part closely.
- **Measured directly:** the bottom of the notch sits 0.245" below the hole line, which matches R0.25. The tip end sits 1.00" below it, so notch to tip ≈ 0.75".
- **Output:** `AUC1054_length_check.png`, with A v1 and A v2 side by side.

### 4.5 Photo 5: manual measurement only
- **Grid:** crop (1010, 460, 1230, 690), enlarged 3×.
- **Hole spacing:** about 451 enlarged px, measured along the bend line. Because the spacing runs along the bend, the bend doesn't foreshorten it.
- **Notch bottom to tip:** about 417 enlarged px, projected onto the hole-line normal. That gives **0.80"**.
- **Reliability:** the photo is small and oblique, so the reading is good to about ±0.04".
- **Possible reason it reads longer than photo 4:** here the body lies flat, so the notch-to-tip run isn't foreshortened by the bend.
- **Other readings:** the ears looked about 0.32", which isn't reliable at this size. Tip radius about 0.2".

### 4.6 Checks run on every regeneration
- **Metal between each hole and the edge:** about 0.08" at the narrowest point on A v2.
- **Nut clearance:** about 0.065" per side.
- **DXF read back with ezdxf:** entity types, units and bounding box.
- **Previews:** rendered to PNG and checked by eye.

---

## 5. Decision log (chronological)

1. **Starting outline.** Traced from photo 1. Jason gave S = 0.87".
2. **Holes.** Jason said they take a #10 screw, so 0.190 became 0.201 (free fit).
3. **Notch and ears.** Jason said the notch was too big and the edge around each hole too thin. The notch must clear a 0.37" nut centred between the holes. Result: a round-bottom slot and bigger ears (0.50").
4. **Smooth curve.** Jason asked for 0.45" ears with each ear's radius continuing into the notch. The notch was made tangent to the ears (R = S/2 − EAR_R).
5. **Tip and length.** The tip radius went from 0.06 to 0.15. The length estimate from photo 1 (1.70") was too long.
6. **Photos 2 and 3.** Jason explained the assembly: the shield is clamped between the small plate and the screws, and the three air holes stay partly covered. Overlays at 0.9, 1.1 and 1.3 were compared, and **Jason chose 1.30**, with the tip under the float chamber.
7. **Ear size.** The ears went 0.40 → 0.35 → **0.37**, which Jason chose. This was frozen as **Version A** ("copy of original"), later called A v1.
8. **Version B.** Jason asked for a variant whose sides stay parallel past the three holes and then taper.
9. **Paper prototypes.** A print page with A and B side by side, printed by Jason.
10. **Comparison sheet** (2026-11-18). A 1:1 outline beside an empty grid, for someone with an original part. Jason's edits: grid 4×4.5 → **3×3**, instructions removed, ruler removed, outline labelled **"PROTOTYPE"**.
11. **Photo 4.** Showed A v1 was too long. Jason said the bend matters but the **notch-to-tip distance is the key**. A was rebuilt so the length is driven by `NOTCH_TO_TIP = 0.75`, with `TIP_R = 0.22`. This is **A v2**, and the comparison sheet was updated to label notch to tip.
12. **Photo 5.** Suggested about 0.80". Offered, but not applied.
13. **Deliverables for A v2** (2026-11-21): the prototype PDF, `AUC1054_A_v2.dxf` and the README. **A v2 was declared final.**

---

## 6. File inventory and status

**Legend:** ✅ current · 🟡 superseded or old, keep for reference · ♻️ duplicate · 🧪 experimental

### Cut files (DXF)
| File | Status | Notes |
|---|---|---|
| `AUC1054_A_v2.dxf` | ✅ **FINAL** | A v2, 1.24 × 1.185 |
| `AUC1054_A_original.dxf` | ♻️ | Same geometry as A v2 (checked). Only the DXF header bytes differ. Can be removed or renamed. |
| `AUC1054_dust_shield.dxf` | ♻️ | A byte-identical copy of `AUC1054_A_original.dxf`, written by the script's default output name. Can be removed. |
| `AUC1054_A_v1_1.30long.dxf` | 🟡 | A v1, 1.30" long, tip R0.15 |
| `AUC1054_B_parallel.dxf` | 🧪 | B, still at the old 1.30" length and R0.15 tip |

### Generator scripts (Python 3, need `ezdxf` and `shapely`, plus `matplotlib` for previews)
| File | Status | Notes |
|---|---|---|
| `auc1054_A_original.py` | ✅ | Generates A v2. Its `__main__` writes `AUC1054_dust_shield.dxf` and `AUC1054_preview.png`, so suggest renaming its outputs to `AUC1054_A_v2.*`. |
| `auc1054_A_v1_1.30long.py` | 🟡 | The A v1 generator |
| `auc1054.py` | ♻️ | Byte-identical to `auc1054_A_v1_1.30long.py`. It was the original working file. |
| `auc1054_B_parallel.py` | 🧪 | Generates B |
| `print_template.py` | ✅ tool | 1:1 multi-variant print page. Usage: `python3 print_template.py "Label:script.py" ...` |
| `comparison_sheet.py` | ✅ tool | Builds `AUC1054_A_comparison_sheet.pdf` from `auc1054_A_original.py` |
| `part_pdf.py` | ✅ tool | Builds `AUC1054_A_prototype.pdf` |
| `work/overlay.py` | tool | Photo 3 overlay. Hard-coded cloud paths: edit `src` and `sys.path`. |
| `work/overlay2.py` | tool | Photo 4 overlay. Same hard-coded paths. |

### PDFs and images
| File | Status | Notes |
|---|---|---|
| `AUC1054_A_prototype.pdf` | ✅ | A v2 outline alone at 1:1, US Letter, with a 1" square |
| `AUC1054_A_comparison_sheet.pdf` | ✅ | A v2 at 1:1 labelled PROTOTYPE, an empty 3"×3" grid in 0.1" squares, and a 1" square. For a third party to photograph an original part on. |
| `AUC1054_paper_prototypes.pdf` | 🟡 | A v1 and B side by side at 1:1. Old lengths. Regenerate with `print_template.py` if needed. |
| `AUC1054_preview.png` | ✅ | Dimensioned preview of A v2 |
| `AUC1054_B_preview.png` | 🧪 | Preview of B |
| `AUC1054_fit_check.png` | 🟡 | A v1 and B on photo 3 |
| `AUC1054_length_check.png` | ✅ | A v1 against A v2 on photo 4, which justifies the A v2 length |
| `images/01–05_*` | source | See section 3 |

### 6.1 Renames applied on 2026-11-21

| Handoff name | New location |
|---|---|
| `AUC1054_A_v2.dxf` | `AUC1054_A_v2.dxf` (unchanged) |
| `AUC1054_A_prototype.pdf` | `AUC1054_A_v2_prototype.pdf` |
| `AUC1054_A_comparison_sheet.pdf` | `AUC1054_A_v2_comparison_sheet.pdf` |
| `AUC1054_preview.png` | `AUC1054_A_v2_preview.png` |
| `AUC1054_length_check.png` | `AUC1054_A_v2_length_check.png` |
| `auc1054_A_original.py` | `scripts/auc1054_A_v2.py` |
| `part_pdf.py` | `scripts/auc1054_A_v2_prototype_pdf.py` |
| `comparison_sheet.py` | `scripts/auc1054_A_v2_comparison_sheet.py` |
| `print_template.py` | `scripts/auc1054_print_template.py` |
| `work/overlay.py` | `scripts/auc1054_overlay_photo3_fit_check.py` |
| `work/overlay2.py` | `scripts/auc1054_overlay_photo4_length_check.py` |
| `AUC1054_A_v1_1.30long.dxf` / `.py` | `early_trials/AUC1054_A_v1_1.30long.dxf` / `.py` |
| `AUC1054_B_parallel.dxf` / `.py` | `early_trials/AUC1054_B_parallel.dxf` / `.py` |
| `AUC1054_B_preview.png` | `early_trials/AUC1054_B_parallel_preview.png` |
| `AUC1054_paper_prototypes.pdf` | `early_trials/AUC1054_A_v1_B_paper_prototypes.pdf` |
| `AUC1054_fit_check.png` | `early_trials/AUC1054_A_v1_B_fit_check.png` |
| `images/01–05_*` | `images/01–05_*` (Jason's folder copies renamed to match) |
| `IMG_9850 Medium.jpeg` (not in the handoff) | `images/00_hand_sketch.jpg`: Jason's sketch, 0.87" spacing, #10, 22 ga |
| `IMG_*.HEIC`, `IMG_9850.jpeg` | `images/originals/` |
| `AUC1054_dust_shield_handoff.zip` | `archive/` |
| `auc1054.py`, `AUC1054_dust_shield.dxf`, zip's `AUC1054_A_original.dxf` | not extracted (duplicates); in the zip only |

### Suggested organization at handoff (superseded by 6.1)
```
AUC1054_dust_shield/
  README.md
  HANDOFF_AUC1054.md
  final/        AUC1054_A_v2.dxf, AUC1054_A_prototype.pdf, AUC1054_A_comparison_sheet.pdf, AUC1054_preview.png
  versions/     A_v1_1.30long/, B_parallel/   (each with its .py, .dxf and preview)
  scripts/      auc1054_A_original.py (rename to auc1054_A_v2.py), print_template.py, comparison_sheet.py, part_pdf.py, overlay*.py
  checks/       AUC1054_fit_check.png, AUC1054_length_check.png, AUC1054_paper_prototypes.pdf
  images/       01–05 source photos
```
- Delete the ♻️ duplicates.
- If you rename `auc1054_A_original.py`, update the import paths in `comparison_sheet.py` and `part_pdf.py`. Both load it by filename.

---

## 7. Ordering notes (SendCutSend)
- Upload `AUC1054_A_v2.dxf` with **units set to inches**. It should report about **1.24" × 1.19"**.
- Before ordering, settle `NOTCH_TO_TIP` (0.75 or 0.80, or a real measurement), then the material and thickness.
- After cutting, bend the ears by hand along a line roughly through the bottom of the notch, to match the original.
