# Oval washer BD542/3 — 1959 Jaguar XK 150S (T831957DN)

Flat oval (stadium-shaped) washer, to be laser cut at SendCutSend in 0.06 in (1.5 mm) stainless. File names use `BD542-3` because a `/` can't go in a file name.

## Part

- **Part number:** BD542/3, oval washer.
- **Nominal size:** 1-1/2" × 3/4" with a 1/4" hole. The design uses the nominal width and length, and a 0.27 hole (see Geometry).
- **Moss Motors listing:** plated mild steel, 1-1/2" × 3/4" with a 1/4" hole. Current price $1.25 each (2026-11-22; https://mossmotors.com/bd542-3-oval-washer-mild-steel).
- **Where it goes:** Moss shows it in *Front Body Panels & Fittings, XK150*, key 26, **qty 14**. It's also used on the XK120 under-body panels (qty 10), XK140 front body (qty 1), and E-Type Series I & II front body (qty 1).

## Status

**v1, 2026-11-22. Ready to order.** DXF and 1:1 PDF made from the hand sketch (IMG_9884), with the width set to the nominal 0.75. No true-size check planned; the sizes are close enough.

The earlier oval-washer files were not found. v1 uses new measurements.

## Geometry v1 (inches)

- Overall: 0.75 wide × 1.50 long. The sketch measured 0.76 wide; the width was set to the nominal 0.75 (decision 2026-11-22).
- Ends: full radius, R0.375. The straight sides are 0.75 long.
- Hole: Ø0.27, through, centred both ways, as measured. The sketch's digits are written over each other; Jason confirmed 0.27 on 2026-11-22. Nominal is 1/4"; 0.27 is a clearance hole for a 1/4" bolt.
- Thickness: 0.06 per the sketch. **Order in 0.06 in (1.5 mm) stainless at SendCutSend.** The DXF is a flat profile and doesn't depend on thickness.
- Material: **stainless** (decision 2026-11-22). The original / Moss part is plated mild steel.

## Files

| File | Purpose |
|---|---|
| `BD542-3_oval_washer_v1.dxf` | **Current** cut file. Units are inches. Contains 1 closed polyline with true arcs (the outline) and 1 circle (the hole). No dimensions. Origin at the washer centre. |
| `BD542-3_oval_washer_v1.pdf` | 1:1 print on letter paper, with dimensions and a 1" check square. Print at 100% / Actual size. |
| `BD542-3_oval_washer_v1_preview.png` | PNG preview of the PDF. |
| `scripts/build_BD542-3_oval_washer.py` | Builds the DXF, PDF and PNG. Run it from this folder: `python3 scripts/build_BD542-3_oval_washer.py v1`. Needs `ezdxf`, `matplotlib` and `numpy`. |
| `images/IMG_9884*` | Hand sketch with measurements. |

## Open items

- [x] Part number: BD542/3.
- [x] Quantity: **50** (the XK150 front body uses 14).
- [x] Cut or buy: **cut in stainless.** 50 for $38 (about $0.76 each), vs Moss plated mild steel at $1.25 each (2026-11-22).
- [x] Sheet thickness: **0.06 in (1.5 mm) stainless at SendCutSend**, same as the sketch (2026-11-22).
- [x] Measured vs nominal: width set to nominal 0.75 (measured 0.76). Length 1.50 and hole Ø0.27 unchanged.
- [x] True-size print check: skipped. The sizes are close enough (2026-11-22).

## Change log

- **2026-11-22:** v1 width changed from 0.76 to the nominal 0.75 (ends now R0.375); kept as v1. True-size check dropped.
- **2026-11-22:** Sheet set to 0.06 in (1.5 mm) stainless at SendCutSend.
- **2026-11-22:** Decided to cut 50 in stainless for $38; Moss price updated to $1.25.
- **2026-11-22:** Nominal size (1-1/2 × 3/4, 1/4 hole) documented.
- **2026-11-22:** Part number BD542/3 added; files and folder renamed to match. Moss fitment and material notes added.
- **v1 (2026-11-22):** First version, made from the hand sketch (0.76 wide at first). Hole set to 0.27 (confirmed).
