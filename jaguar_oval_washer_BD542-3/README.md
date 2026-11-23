# Oval washer BD542/3 — 1959 Jaguar XK 150S (T831957DN)

Flat oval (stadium-shaped) washer, for laser cutting (for example at SendCutSend) in 0.06 in (1.5 mm) stainless. File names use `BD542-3` because a `/` can't go in a file name.

## Part

- **Part number:** BD542/3, oval washer.
- **Nominal size:** 1-1/2" × 3/4" with a 1/4" hole. The design uses the nominal width and length, and a 0.27 hole (see Geometry).
- **Original material:** plated mild steel, per the [Moss Motors listing](https://mossmotors.com/bd542-3-oval-washer-mild-steel).
- **Where it goes:** Moss shows it in *Front Body Panels & Fittings, XK150*, key 26, **qty 14**. It's also used on the XK120 under-body panels (qty 10), XK140 front body (qty 1), and E-Type Series I & II front body (qty 1).

## Status

**v1 is ready to cut.** Made from measurements of an original washer, with the width set to the nominal 0.75. Not checked at true size against an original; the measured and nominal sizes are within 0.01.

## Geometry v1 (inches)

- Overall: 0.75 wide × 1.50 long. The original measured 0.76 wide; the design uses the nominal 0.75.
- Ends: full radius, R0.375. The straight sides are 0.75 long.
- Hole: Ø0.27, through, centered both ways, as measured on the original. Nominal is 1/4"; 0.27 is a clearance hole for a 1/4" bolt.
- Thickness: 0.06, as measured. The design is intended for **0.06 in (1.5 mm) stainless**. The DXF is a flat profile and doesn't depend on thickness.
- Material: **stainless** in this design, for corrosion resistance. The original is plated mild steel.

## Files

| File | Purpose |
|---|---|
| `BD542-3_oval_washer_v1.dxf` | **Current** cut file. Units are inches. Contains 1 closed polyline with true arcs (the outline) and 1 circle (the hole). No dimensions. Origin at the washer center. |
| `BD542-3_oval_washer_v1.pdf` | 1:1 print on letter paper, with dimensions and a 1" check square. Print at 100% / Actual size. |
| `BD542-3_oval_washer_v1_preview.png` | PNG preview of the PDF. |
| `scripts/build_BD542-3_oval_washer.py` | Builds the DXF, PDF and PNG. Run it from this folder: `python3 scripts/build_BD542-3_oval_washer.py v1`. Needs `ezdxf`, `matplotlib` and `numpy`. |
| `images/IMG_9884*` | Hand sketch with measurements (not in the repository). |

> **The scripts are optional.** The DXF, PDF template and preview files in this folder are ready to use as they are. The scripts are only needed if those files have to be modified and regenerated.

## Version history

- **v1 (2026-11-22):** First version: 0.75 × 1.50, R0.375 ends, Ø0.27 hole.
