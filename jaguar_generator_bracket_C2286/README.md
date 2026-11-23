# Generator adjustment bracket C2286 — 1959 Jaguar XK 150S (T831957DN)

A flat replacement for the generator adjustment bracket, for laser cutting (for example at SendCutSend).

## Status

**v2 is the current design.** v1 is kept for reference in `early_trials/`. v2 has not yet been checked at true size against an original part (see Open items).

## Material thickness

**The original part is 0.19 in thick.** The nearest standard sheet is **0.187 in (4.75 mm)**, which is what this design is intended for; SendCutSend also offers 0.25. If you choose a thicker sheet, check bolt length and generator/bracket spacing on the car first. The DXFs are flat profiles and don't depend on thickness. This note is on both the v1 and v2 PDFs.

## Files

| File | Purpose |
|---|---|
| `C2286_generator_bracket_v2.dxf` | **Current** cut file. Units are inches. 3 closed polylines (outline and 2 slots), no dimensions. |
| `C2286_generator_bracket_v2.pdf` | **Current** 1:1 print on letter paper with dimensions and a 1" check square. Print at 100% / Actual size. |
| `early_trials/C2286_generator_bracket_v1.dxf` | v1 cut file (reference). Units are inches. 3 closed polylines with true arcs (outline and 2 slots), no dimensions. |
| `early_trials/C2286_generator_bracket_v1.pdf` | v1 1:1 print on letter paper with dimensions and a 1" check square. Print at 100% / Actual size. |
| `early_trials/C2286_generator_bracket_v1_photo_overlay.png` | The v1 outline drawn over a photo of the original part on a 1" grid. |
| `scripts/build_C2286_bracket.py` | Builds the DXF, PDF and PNG preview. Run it from this folder: `python3 scripts/build_C2286_bracket.py v2` (or `v1`). Output goes to the current folder, so move v1 output into `early_trials/`. Needs `ezdxf`, `matplotlib` and `numpy`. |
| `images/IMG_9877*` | Hand sketch with the measurements (not in the repository). |
| `images/IMG_9878*` | Original part photographed on a 1" grid (not in the repository). |

> **The scripts are optional.** The DXF, PDF template and preview files in this folder are ready to use as they are. The scripts are only needed if those files have to be modified and regenerated.

## v1 geometry (inches), the base for v2

- Material: original is 0.19 thick (see Material thickness above).
- Overall size: 4.00 long × 1.29 max width.
- Left edge: straight and vertical. Both end radii are tangent to it.
- Top end: R0.39, concentric with the top end of the upper slot.
- Bottom end: R0.43, concentric with the bottom end of the lower slot.
- Upper slot: 0.34 wide × 0.79 overall, 20° from vertical. End-center positions are (0.39, 3.61) and (0.544, 3.187), measured from the left edge (x) and the bottom of the part (y).
- Lower slot: 0.34 wide × 2.225 overall, 14° from vertical. End-center positions are (0.43, 0.43) and (0.886, 2.259).
- Right edges: each runs parallel to its slot. The angle between them is 146°.
- Right corner: R0.59 fillet (0.5875 exact). It's sized so the max width comes out at 1.29.

## v2 changes (current design)

Same slots, ends, left edge and lower right edge as v1. Only the right corner changes, to thicken the thinnest wall (0.22 in v1) without moving the slots:

- **Corner:** R0.43 arc concentric with the top end of the lower slot (end center 0.886, 2.259), replacing the R0.59 fillet. Wall around that slot end is an even 0.26.
- **Upper right edge:** tilted from 20° to about 21.75° so it runs tangent from the top end (R0.39) to the corner arc. Upper slot right wall goes from 0.22 at the top to 0.23 at the bottom.
- **Max width:** 1.32 (1.316), up from 1.29. This is the minimum possible with a 0.26 wall at that spot. The extra width is at the corner, about 2.2 in up from the bottom.
- **Angle between right edges:** 144° (v1 146°, measured on the original 145°).
- **Minimum wall:** 0.26 at the corner (v1 0.22). The 0.22 walls at the upper slot's top end and right side are unchanged and match the original.

## Wall thicknesses in v1

| Location | Value | Measured on the original |
|---|---|---|
| Top end, along the upper slot's axis | 0.22 | 0.22 |
| Right wall of the upper slot (parallel section) | 0.22 | 0.22 |
| Right wall of the lower slot (parallel section) | 0.26 | 0.25 |
| Bottom end, along the lower slot's axis | 0.26 | 0.26 |
| Between the slots (upper slot bottom to lower slot top) | 0.65 | 0.64 |
| Thinnest point: top right of the lower slot, at the fillet | 0.22 | — |

The right wall of the lower slot stays 0.26 up to about 1.76 along the slot axis, measured from the bottom end center. Above that point the fillet makes it thinner.

## Notes from checking against the original

- **Right edge angle:** measured on the part as 145°; the photo reads about 147°. v1 uses 146°, between the two; v2's thicker corner makes it 144°. Both are within the measuring uncertainty.
- **Photo overlay:** the outline, the ends, the max width and its height all match. Both slots look about 0.04 wider in the photo, on their left edges, which could be wear or the camera seeing the slot walls. The upper slot looks about 2° steeper. The wall beside the lower slot looks closer to 0.23.

## Open items

- [ ] Print the v2 PDF at true size and check it against an original.
- [ ] Caliper-check both slot widths mid-slot and the wall beside the lower slot.
- [ ] Check clearance on the car for v2's extra 0.03 width near the corner, about 2.2 in up from the bottom.
- [ ] Right wall of the lower slot: 0.26 in the design, 0.25 measured on the original. Not yet confirmed which is right.

## Version history

- **v2 (2026-11-21):** Corner changed to R0.43 concentric with the lower slot's top end; upper right edge re-angled to ~21.75°. Min wall 0.26, max width 1.32, right edges 144°. Thickness note added to both PDFs.
- **v1 (2026-11-21):** First version, traced from measurements and a photo of the original. R0.59 right fillet gives a 1.29 max width.
