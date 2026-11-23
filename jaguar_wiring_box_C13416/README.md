# C13416 Wiring Connector Shield: Jaguar XK150S

A reproduction of Jaguar part **C13416**, the sheet-metal cover over the 5-way / 10-way snap-connector block, where the front harness joins the lamp and horn wiring. It sits in front of the radiator. Coventry Auto Components sells it as part 5302, and Moss Motors sells it as C13416. Neither publishes dimensions, so this pattern was built from the mounting holes on the car and from product photos.

The flat pattern is made for **SendCutSend cut + bend**. Units are inches.

## Current versions: v3 and v4

> **Two variants, neither confirmed.** v3 and v4 differ only in the depth of the TOP, front to back: **2.00" in v3, 1.75" in v4**. Both depths are estimates from product photos, and it is still uncertain which is closer to the original part. Both are kept at the top level so their printouts can be compared, ideally against an original. The hole spacing (6.25", measured on the car) and the 5.25" length between the ENDs are the same in both.

v4 files:

| File | What it is |
|---|---|
| `C13416_cover_v4.dxf` | **v4 cut file**, TOP depth 1.75". Layers `CUT` and `BEND`, as in v3. |
| `C13416_cover_v4_template.pdf` | v4 full-size template (US Letter, landscape). Print at 100% and check the 1" square. |
| `C13416_cover_v4_preview.png` | Quick picture of the v4 flat pattern |
| `scripts/C13416_cover_v4.py`, `scripts/C13416_print_template_v4.py` | v4 generators. Run them from this folder: `python3 scripts/C13416_cover_v4.py && python3 scripts/C13416_print_template_v4.py` |

v3 files:

| File | What it is |
|---|---|
| `C13416_cover_v3.dxf` | **v3 cut file**, TOP depth 2.00". The outline and holes are on layer `CUT`; the 7 bend lines are on layer `BEND`. |
| `C13416_cover_v3_template.pdf` | Full-size black-and-white template (US Letter, landscape). It shows surface names, flat dimensions, fold instructions and the contact line. Print at 100% and check the 1" square. |
| `C13416_cover_v3_preview.png` | Quick picture of the flat pattern |
| `C13416_v3_tab_diagram.png`, `C13416_v3_relief_diagram.png` | Diagrams of the two v3 changes against v2 |
| `scripts/C13416_cover_v3.py` | Generates the DXF and preview. All design inputs are at the top. |
| `scripts/C13416_print_template_v3.py` | Generates the template PDF from the same geometry |

> **The scripts are optional.** The DXF, PDF template and preview files in this folder are ready to use as they are. The scripts are only needed if those files have to be modified and regenerated.

To change the v3 design, edit the inputs in `scripts/C13416_cover_v3.py`, then run both scripts from `scripts/`:

```
python3 C13416_cover_v3.py && python3 C13416_print_template_v3.py
```

They need `ezdxf` and `matplotlib`. The DXF and the PDF always come from the same geometry, so they can't drift apart.

### Folded part (v3; v4 differs only in TOP depth)
- **TOP:** 5.25" × 2.00" (v4: 5.25" × 1.75").
- **5.25" between the ENDs (outside to outside) is required.** The wiring passes through two holes in the body, each fitted with a rubber grommet, and the ENDs must stay clear of those grommets. Don't reduce this length.
- **Clearance under TOP:** 1.125". The block is about 1" tall, plus the clip.
- **FRONT:** folds down along the long edge. It leaves a 0.25" gap underneath for the wires to exit.
- **ENDs:** each folds down at a short end.
- **TABs:** each folds the opposite way to lie flat on the body. They are 0.60" wide with a full-round end and a Ø0.20" (#10) hole.
- **Hole spacing:** **6.25" center to center** (measured on the car). Each hole is 0.50" out from the outside of its END.
- **FLAPs:** one at each end of the FRONT, folding inward and tucking inside the ENDs with 0.06" clearance.
- **Back and bottom:** open.
- **Flat blank:** 8.937" × 2.834" (v4: 8.937" × 2.584").

### Design inputs (from `scripts/C13416_cover_v3.py`)

| Input | Value | Note |
|---|---|---|
| Material | 18 ga (0.048") mild steel | **Assumed.** Confirm when ordering. |
| Inside bend radius / K-factor | 0.05" / 0.38 | **Approximate.** Bend deduction is about 0.089" per bend. Check against SendCutSend's bending calculator for the chosen material. |
| `HOLE_CC` | 6.25" | Measured on the car |
| `HOLE_D` | 0.20" | #10 clearance |
| `D` (TOP depth) | 2.00" | Estimated from photos (v4: 1.75") |
| `H_IN` (clearance under TOP) | 1.125" | |
| `E` (END face to hole center) | 0.50" | |
| `TAB_W` | 0.60" | |
| `GAP` (under FRONT) | 0.25" | |
| `FLAP` | 0.50" deep | Top edge slopes from 0.18" to 0.45" below the front bend |
| `CLR` (flap to END) | 0.06" | |
| `RR` (corner relief) | R0.10" | Round reliefs, centerd where the front and end bend lines meet. The END side of each relief is a straight edge, tangent to the circle and running square to the END's edge. |
| `TAB_STRAIGHT` | 0.125" | The END edges run parallel this far past the tab bend before tapering to the round tab |

### Fold directions (when uploading to SendCutSend)
- Bends 1–3 (FRONT and both ENDs) and bends 6–7 (both FLAPs) all fold the **same way**: down, or inward.
- Bends 4–5 (both TABs) fold the **opposite way**, so the tabs lie flat on the body.

## Version history

### v1 (2026-11-13), in `early_trials/`
- Same overall size and hole spacing as v2.
- Corner reliefs were **square notches**.
- Each flap sat only **0.01"** from the inside of its END. SendCutSend's fold preview showed the flaps hitting the ENDs.
- The tab edges met the round end with a small inward notch.

**Files:**
- `C13416_cover_v1.dxf`: v1 cut file
- `C13416_cover_v1_print_a.pdf` and `C13416_cover_v1_print_b.pdf`: the first color (red bend line) print templates

### v2 (2026-11-13 to 11-18), in `early_trials/`
Changes from v1, made after SendCutSend's fold preview and a paper test fit:
1. **Flap bend lines:** moved 0.05" farther in from each END, for 0.06" of clearance.
2. **Flap top edges:** now start 0.18" below the top bend instead of 0.12", to clear the bend radius where the TOP meets the END.
3. **Corner reliefs:** **round** (R0.10") instead of square notches.
4. **Tab edges:** now **tangent to the round end**, so the outline is continuous with no notch.

The template was also redone in black and white:
- Bend lines are dashed instead of red, with a key.
- Surface names were added (TOP, FRONT, END, TAB, FLAP).
- Dimensions were added, including the tab's 0.504" from the bend to the hole center and 0.804" from the bend to the tip.
- It has the title "Jaguar Wiring Connector Shield - C13416", a prototype subtitle, and a Jag-Lovers forum contact (trimtab).

**Files:**
- `C13416_cover_v2.dxf`, `C13416_cover_v2_template.pdf` and `C13416_cover_v2_preview.png`
- Scripts: `scripts/C13416_cover_v2.py` and `scripts/C13416_print_template_v2.py`. These were reconstructed from the recorded v2 design inputs and verified against the v2 template: every dimension matches its label, the outline matches the template's outline, and the regenerated template is pixel-identical to the original.

### v3 (2026-11-21)
Two changes from v2, both to match the reference photos more closely:
1. **Straight run past the tab bend.** The END's top and front edges continue parallel for **0.125"** past each tab bend line (flat) before the taper starts. All the reference photos except the SNG Barratt one show this. The taper still runs tangent into the R0.30" round end. The hole position (0.504" from the bend), tab length (0.804" to the tip) and blank size are unchanged.
2. **No sharp point at the reliefs.** Where the END, TOP and FRONT meet, the relief circle used to cut back into the END and leave a sharp point. The circle now stops at its outermost point, and a straight edge tangent to it runs square down to the END's front edge. Each relief is mirrored; the FRONT side of each relief is unchanged.

The template also gained a "0.125 straight" dimension on the right tab, and the subtitle now says "v3".

### v4 (2026-11-22)
One change from v3: **TOP depth `D` reduced from 2.00" to 1.75"**, as an alternative estimate of the original's depth from the photos.
- Flat TOP and END depth: 1.706" (v3: 1.956"). Flat blank: **8.937" × 2.584"** (v3: 8.937" × 2.834").
- The tab and hole center line stays centerd on the END's depth, so it moves 0.125" closer to the front.
- Unchanged: hole spacing (6.25" folded, 8.337" flat), the 5.25" length between the ENDs, 1.125" clearance under the TOP, FRONT height, flaps, tabs (0.504" to hole center, 0.804" to tip), reliefs and the 0.125" straight run.
- Template: subtitle says "v4", and the folded-size note is computed from the inputs (TOP 5.25" × 1.75").

## Open items before ordering
- **TOP depth:** not known whether v3 (2.00") or v4 (1.75") is closer to the original. Compare printouts with an original part, or measure one, before choosing.
- **Material and thickness:** assumed 18 ga mild steel. Once chosen, update `T`, `R_IN` and `K` from SendCutSend's bending calculator and regenerate.
- **Fold check:** upload the chosen DXF and check SendCutSend's 3D fold preview. The flaps must not collide with the ENDs; this hasn't been checked since v1.
- Optional: compare the ENDs and tabs with photos of an original part.

## Images (`images/`)

| File | What it shows |
|---|---|
| `00_hand_sketch_measurements.jpeg` | Hand sketch with the measurements from the car (not in the repository) |
| `01_car_location_behind_radiator.jpeg` | Where the cover goes on the car: in front of the radiator, over the connector block (not in the repository) |
| `02_coventry_5302_cover_5300_block_5301_clip.jpg` | Coventry Auto Components: the 5302 cover with the 5300 block and 5301 clip |
| `03_cover_stainless_5303a.jpg` | Coventry Auto Components: stainless reproduction cover (file name "5303a") |
| `04_cover_black_C13416.webp` | Moss Motors: black reproduction cover product photo (file name "C13416_1") |
| `05_cover_sng_barratt.png` | SNG Barratt product photo of the cover |

### Image sources

Product photos downloaded 2026-11-02.

| File | Source page | Image URL |
|---|---|---|
| `02_coventry_5302_cover_5300_block_5301_clip.jpg` | Coventry Auto Components, [C13416 10-way connector cover](https://coventryautocomponents.co.uk/store/c13416-10-way-connector-cover) | https://coventryautocomponents.co.uk/store/image/cache/catalog/sectionfive/5300%20and%20accessories-750x750.jpg |
| `03_cover_stainless_5303a.jpg` | Coventry Auto Components, same page | https://coventryautocomponents.co.uk/store/image/cache/catalog/sectionfive/5303a-750x750.jpg |
| `04_cover_black_C13416.webp` | Moss Motors, [C13416 wiring connector cover](https://mossmotors.com/c13416-wiring-connector-cover) | https://mossmotors.com/media/catalog/product/C/1/C13416_1.jpg |
| `05_cover_sng_barratt.png` | SNG Barratt, [sngbarratt.com](https://www.sngbarratt.com/) (product page not recorded) | https://cdn.sngbarratt.com/images/products/500/e1ca7f4a-27de-470a-bb52-c287f3742a5f.png |

## Other folders
- `archive/`: an exact duplicate of the v1 DXF (`cover_flat(1).dxf`).
