# Generator adjustment bracket C2286 — 1959 Jaguar XK 150S (T831957DN)

A flat replacement for the generator adjustment bracket, to be laser cut at SendCutSend.

## Status

**v2, 2026-11-21.** v1 and v2 DXF/PDF files are made. **v2 is the current design**; v1 is kept for reference. Next, print a PDF at true size and check it against the original part.

## Material thickness

**The original part is 0.19 in thick.** Standard 3/16 sheet is 0.187. A thicker sheet may be chosen at SendCutSend; if so, check bolt length and generator/bracket spacing on the car first. The DXFs are flat profiles and don't depend on thickness. This note is on both the v1 and v2 PDFs.

**Decision (2026-11-21): order in 0.187 in (4.75 mm).** SendCutSend offered 0.187 and 0.25. These are SendCutSend's nominal thicknesses; the actual sheet will vary within the mill tolerance.

## Files

| File | Purpose |
|---|---|
| `C2286_generator_bracket_v2.dxf` | **Current** cut file. Units are inches. 3 closed polylines (outline and 2 slots), no dimensions. |
| `C2286_generator_bracket_v2.pdf` | **Current** 1:1 print on letter paper with dimensions and a 1" check square. Print at 100% / Actual size. |
| `C2286_generator_bracket_v1.dxf` | v1 cut file (reference). Units are inches. It contains 3 closed polylines with true arcs (outline and 2 slots) and no dimensions. |
| `C2286_generator_bracket_v1.pdf` | 1:1 print on letter paper with dimensions and a 1" check square. Print at 100% / Actual size. |
| `C2286_generator_bracket_v1_photo_overlay.png` | The v1 outline drawn over the photo of the original on a 1" grid (IMG_9878). |
| `build_C2286_bracket.py` | Builds the DXF and PDF: `python3 build_C2286_bracket.py v1` or `... v2`. Needs `ezdxf`, `matplotlib` and `numpy`. |
| `IMG_9877*` | Hand sketch with the measurements. |
| `IMG_9878*` | Original part photographed on a 1" grid. |

## v1 geometry (inches) — base for v2

- Material: original is 0.19 thick (see Material thickness above).
- Overall size: 4.00 long × 1.29 max width.
- Left edge: straight and vertical. Both end radii are tangent to it.
- Top end: R0.39, concentric with the top end of the upper slot.
- Bottom end: R0.43, concentric with the bottom end of the lower slot.
- Upper slot: 0.34 wide × 0.79 overall, 20° from vertical. End-centre positions are (0.39, 3.61) and (0.544, 3.187), measured from the left edge (x) and the bottom of the part (y).
- Lower slot: 0.34 wide × 2.225 overall, 14° from vertical. End-centre positions are (0.43, 0.43) and (0.886, 2.259).
- Right edges: each runs parallel to its slot. The angle between them is 146°.
- Right corner: R0.59 fillet (0.5875 exact). It's sized so the max width comes out at 1.29.

## v2 changes (current design)

Same slots, ends, left edge and lower right edge as v1. Only the right corner changes:

- **Corner:** R0.43 arc concentric with the top end of the lower slot (end centre 0.886, 2.259), replacing the R0.59 fillet. Wall around that slot end is an even 0.26.
- **Upper right edge:** tilted from 20° to about 21.75° so it runs tangent from the top end (R0.39) to the corner arc. Upper slot right wall goes from 0.22 at the top to 0.23 at the bottom.
- **Max width:** 1.32 (1.316), up from 1.29. This is the minimum possible with a 0.26 wall at that spot. The extra width is at the corner, about 2.2 in up from the bottom.
- **Angle between right edges:** 144° (v1 146°, measured on original 145°).
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

The right wall of the lower slot stays 0.26 up to about 1.76 along the slot axis, measured from the bottom end centre. Above that point the fillet makes it thinner.

## Notes from checking against the original

- **Right edge angle:** v1 is 146°. Measured on the part it's 145°, and the photo reads about 147°. Decision (2026-11-21): keep 146°.
- **Photo overlay:** The outline, the ends, the max width and its height all match. Both slots look about 0.04 wider in the photo, on their left edges, which could be wear or the camera seeing the slot walls. The upper slot looks about 2° steeper. The wall beside the lower slot looks closer to 0.23.

## Open items

- [ ] Print the v2 PDF at true size and check it against the original.
- [ ] Caliper-check both slot widths mid-slot and the wall beside the lower slot.
- [x] Right edge angle: keep v1 146° (v2 is 144° as a result of the thicker corner). Both are close enough to the 145° measured. Revisit only if the printout shows a problem.
- [x] Thicken the 0.22 wall at the fillet without moving the slots: done in v2 (0.26 min, 1.32 max width).
- [ ] Check clearance on the car for v2's extra 0.03 width near the corner, about 2.2 in up from the bottom.
- [x] Sheet thickness: **0.187 in (4.75 mm)**, chosen 2026-11-21. SendCutSend options were 0.187 and 0.25; 0.187 is closest to the original 0.19 (4.83 mm).
- [ ] Decide on 0.25 vs 0.26 for the right wall of the lower slot.

## Change log

- **v2 (2026-11-21):** Corner changed to R0.43 concentric with the lower slot's top end; upper right edge re-angled to ~21.75°. Min wall 0.26, max width 1.32, right edges 144°. Thickness note added to both PDFs.
- **v1 (2026-11-21):** First version, traced from the sketch and the original. Added the R0.59 right fillet to get a 1.29 max width.
