# Radiator tie strap 460-043 — 1959 Jaguar XK 150S (T831957DN)

A flat replacement for the radiator tie strap (stay), for laser cutting.

## Part

- **Part number:** 460-043, Moss Motors' "Radiator Tie Bracket Pair, XK150 "S"" (XK150 1958–60). Moss says the pair includes the **C13029** and **C12925** stays, plus a **C14943** bracket for the rubber bonnet-rod retainer on the L/H stay ([Moss listing](https://mossmotors.com/jaguar-xk120-140-150/460-043-radiator-tie-bracket-pair-xk150-s)).
- The non-S XK150 uses 460-042.
- Not yet determined which of C13029 / C12925 this strap is.

## Status

**v1** is provided in two variants:
- **original**: the original part's measurements, 8.875" (8-7/8) long.
- **long**: **1/8" (0.125) longer** overall (9.000"). The slot starts the same 0.25" from its end but is also 0.125 longer (1.125"). The round hole stays 0.38" from its end, so it's 0.125 farther from the slot.

The original part has two small holes for the C14943 bracket. They are **left out of the DXFs**, because not every car needs them and their positions are only partly measured. What is known is documented below.

## Geometry v1 original (inches)

Origin: x = 0 at the slot end of the strap, y = 0 on the centerline.

- Overall: **8.875 (8-7/8) × 0.76**, full-radius ends R0.38.
- Thickness: the original is **0.14**. SendCutSend's nearest stainless sheets are **0.125** (0.015 thinner) and **0.187** (0.047 thicker); either may suit.
- Slot: **0.27 wide × 1.00 long**, on the centerline, starting **0.25 (1/4)** from the slot end (x 0.25 to 1.25).
- Hole: **Ø0.27**, on the centerline, **0.38** from the other end (x 8.495), concentric with the end radius.

## Geometry v1 long (inches)

Same as v1 original except:
- Overall: **9.000** long (8.875 + 0.125).
- Slot: **0.27 wide × 1.125 long**, still starting **0.25** from the slot end (x 0.25 to 1.375).
- Hole: Ø0.27, still **0.38** from its end (x 8.62). Slot end to hole center is 0.125 more than the original.

## Small holes on the original part (reference only, not cut)

Probably for the C14943 bonnet-rod retainer bracket, which Moss says goes on the L/H stay.

| Item | Value | Status |
|---|---|---|
| Diameter | 0.20 (both) | Measured |
| First hole (nearer the slot) | center **2.47** from the slot end of the strap | Measured |
| Second hole | **0.88** center to center from the first | Measured, but not known whether along the strap or straight-line |
| Sideways position of each hole | — | **Not measured.** They appear to be offset to opposite sides of the centerline. |

Once measured, they can be added to `REF_HOLES` in the script as `(x, y, dia)`. They are then drawn on the PDF as blue dashed circles, but never added to the DXF. Both variants use the same x positions, measured from the slot end.

## Files

| File | Purpose |
|---|---|
| `460-043_radiator_strap_v1_original.dxf` | Cut file, original measurements (8.875 long). Units are inches. 2 closed polylines with true arcs (outline and slot) and 1 circle (hole). No dimensions, no small holes. |
| `460-043_radiator_strap_v1_long.dxf` | Cut file, long variant (9.000 long, 1.125 slot). Same structure. |
| `460-043_radiator_strap_v1_original.pdf`, `..._v1_long.pdf` | 1:1 prints on **landscape** letter, with dimensions, the small-hole reference notes and a 1" check square. Print at 100% / Actual size. |
| `..._v1_original_preview.png`, `..._v1_long_preview.png` | PNG previews of the PDFs. |
| `scripts/build_460-043_radiator_strap.py` | Builds the DXF, PDF and PNG for one variant. Run from this folder: `python3 scripts/build_460-043_radiator_strap.py v1 original` and `... v1 long`. Needs `ezdxf`, `matplotlib` and `numpy`. |
| `images/IMG_9815.jpeg` | Hand sketch with measurements (not in the repository). |
| `archive/strap.dxf` | An earlier DXF of the original variant, drawn as loose lines and arcs. Same geometry as v1 original (0.000 in deviation). |

> **The scripts are optional.** The DXF, PDF template and preview files in this folder are ready to use as they are. The scripts are only needed if those files have to be modified and regenerated.

## Open items

- [ ] Measure the small holes fully: sideways positions, and whether 0.88 is along the strap or straight-line.
- [ ] Determine which stay this is (C13029 or C12925).

## Version history

- **v1 (2026-11-22):** Original variant rebuilt by script as closed polylines from `archive/strap.dxf` (identical geometry), plus the long variant (+0.125 overall, slot +0.125, slot start and hole-to-end unchanged).
