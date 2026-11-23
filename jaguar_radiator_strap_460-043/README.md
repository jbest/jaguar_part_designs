# Radiator tie strap 460-043 — 1959 Jaguar XK 150S (T831957DN)

A flat replacement for the radiator tie strap (stay), to be laser cut.

## Part

- **Part number:** 460-043, Moss Motors' "Radiator Tie Bracket Pair, XK150 "S"" (XK150 1958–60). Moss says the pair includes the **C13029** and **C12925** stays, plus a **C14943** bracket for the rubber bonnet-rod retainer on the L/H stay (https://mossmotors.com/jaguar-xk120-140-150/460-043-radiator-tie-bracket-pair-xk150-s). Price listed $83.10 (2026-11-22).
- The non-S XK150 uses 460-042.
- Which of C13029 / C12925 this strap is hasn't been recorded.

## Status

**v1, 2026-11-22.** v1 comes in two variants (every future version will too):
- **original**: the original part's measurements. This is the original `strap.dxf` geometry, rebuilt by script as closed polylines.
- **long**: **1/8" (0.125) longer** overall (9.000"). The slot starts the same 0.25" from its end but is also 0.125 longer (1.125"). The round hole stays 0.38" from its end, so it's 0.125 farther from the slot.

For the original variant: The rebuilt file matches the original exactly (0.000 in deviation). The original is kept in `archive/`.

The two small holes on the original part are intentionally **left out of the DXF**: Jason's car doesn't need them. They're documented below for reference, but their positions still need re-measuring.

## Geometry v1 original (inches)

Origin: x = 0 at the slot end of the strap, y = 0 on the centreline.

- Overall: **8.875 (8-7/8) × 0.76**, full-radius ends R0.38.
- Thickness: **0.14** per the sketch (original part). Stainless at SendCutSend comes in **0.125** or **0.187**; Jason is leaning towards **0.125** (2026-11-22, not final).
- Slot: **0.27 wide × 1.00 long**, on the centreline, starting **0.25 (1/4)** from the slot end (x 0.25 to 1.25).
- Hole: **Ø0.27**, on the centreline, **0.38** from the other end (x 8.495), concentric with the end radius.
- The circled numbers on the sketch are the 0.27 slot and hole widths.

## Geometry v1 long (inches)

Same as v1 original except:
- Overall: **9.000** long (8.875 + 0.125).
- Slot: **0.27 wide × 1.125 long**, still starting **0.25** from the slot end (x 0.25 to 1.375).
- Hole: Ø0.27, still **0.38** from its end (x 8.62). Slot end to hole centre is 0.125 more than the original.

## Small holes on the original part (reference only, not cut)

Probably for the C14943 bonnet-rod retainer bracket, which Moss says goes on the L/H stay.

| Item | Value | Status |
|---|---|---|
| Diameter | 0.20 (both) | Confirmed 2026-11-22 |
| First hole (nearer the slot) | centre **2.47** from the slot end of the strap | Confirmed 2026-11-22 |
| Second hole | **0.88** centre to centre from the first | Confirmed, but not known whether along the strap or straight-line |
| Sideways position of each hole | — | **To re-measure.** The sketch shows them offset to opposite sides of the centreline. |
| "1-7/16" (or 1-1/16) and "1.1" on the sketch | — | Meaning unclear; to re-measure |

When re-measured, add them to `REF_HOLES` in the script as `(x, y, dia)` and rebuild. They'll be drawn on the PDF as blue dashed circles. They are never added to the DXF. Both variants use the same x positions, measured from the slot end.

The ".65?" note near the round-hole end of the sketch is to be ignored (Jason, 2026-11-22).

## Files

| File | Purpose |
|---|---|
| `460-043_radiator_strap_v1_original.dxf` | Cut file, original measurements (8.875 long). Units are inches. 2 closed polylines with true arcs (outline and slot) and 1 circle (hole). No dimensions, no small holes. |
| `460-043_radiator_strap_v1_long.dxf` | Cut file, long variant (9.000 long, 1.125 slot). Same structure. |
| `460-043_radiator_strap_v1_original.pdf`, `..._v1_long.pdf` | 1:1 prints on **landscape** letter, with dimensions, the small-hole reference notes and a 1" check square. Print at 100% / Actual size. |
| `..._v1_original_preview.png`, `..._v1_long_preview.png` | PNG previews of the PDFs. |
| `scripts/build_460-043_radiator_strap.py` | Builds the DXF, PDF and PNG for one variant. Run from this folder: `python3 scripts/build_460-043_radiator_strap.py v1 original` and `... v1 long`. Needs `ezdxf`, `matplotlib` and `numpy`. |
| `images/IMG_9815.jpeg` | Hand sketch with measurements. |
| `archive/strap.dxf` | The original DXF (loose lines and arcs). Same geometry as v1 original. |

## Open items

- [ ] Choose which variant to order: original or long.
- [ ] Re-measure the small holes: sideways positions, whether 0.88 is along the strap or straight-line, and what the 1-7/16 / 1.1 dimension is.
- [ ] Record which stay this is (C13029 or C12925) and how many to cut.
- [ ] Confirm sheet thickness: stainless **0.125 (leaning)** or 0.187. The original is 0.14, so 0.125 is 0.015 thinner and 0.187 is 0.047 thicker.

## Change log

- **2026-11-22:** Material: stainless. SendCutSend stainless options are 0.125 and 0.187; leaning towards 0.125.
- **2026-11-22:** Added the **long** variant (+0.125 overall, slot +0.125, slot start and hole-to-end unchanged). v1 files renamed to `_v1_original`. From now on every version gets both variants.
- **v1 (2026-11-22):** Folder set up. The original `strap.dxf` was rebuilt by script as closed polylines (identical geometry) and moved to `archive/`. PDF, README and small-hole reference notes added.
