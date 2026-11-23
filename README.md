# Jaguar XK 150S part designs — 1959, chassis T831957DN

Reproduction and replacement parts for the restoration. Most are flat sheet-metal parts drawn as DXF cut files for laser cutting (and, where needed, bending) at SendCutSend. Each part has its own folder with a detailed README: status, geometry, decisions, open items and change log.

> **Applicability:** all parts here were designed for and measured on a **1959 Jaguar XK150 S**. Many of the same part numbers were also used on other models (for example other XK150s, XK120/XK140 and E-Type), so these designs may fit those cars too. Check fit and dimensions against your own car before ordering.

## Parts

| Folder | Part | Process | Status (2026-11-22) |
|---|---|---|---|
| [`jaguar_wiring_box_C13416`](jaguar_wiring_box_C13416/) | **C13416** wiring connector shield: cover over the snap-connector block in front of the radiator | Cut + bend (7 bends), 18 ga steel assumed | v3 and a narrower v4 (TOP depth 1.75" vs 2.00") ready to print and compare. Material, bend values and SendCutSend fold check still open. |
| [`jaguar_battery_supports`](jaguar_battery_supports/) | Battery box supports (no part numbers): rear (hat-section) and front (Z-section) strips under the battery, left and right boxes | Cut + bend; made long to suit both sides, trimmed and drilled on assembly | Both ordered in 0.074" CRS mild steel: rear (hat) 15.5" × 2.75" flat, front (Z) 16.5" × 2.25" flat. No holes in the templates: cut to length and drill holes on installation. |
| [`jaguar_carb_shield_AUC1054`](jaguar_carb_shield_AUC1054/) | **AUC1054** starting-carburettor dust shield | Cut; ears bent by hand. 5052 aluminium, 1 mm, qty 10 | Version A v2 is final. Notch-to-tip length (0.75" vs ~0.80") not settled. |
| [`jaguar_generator_bracket_C2286`](jaguar_generator_bracket_C2286/) | **C2286** generator adjustment bracket | Cut, 0.187" sheet | v2 is current. True-size check against the original and a few small slot/wall decisions still open. |
| [`jaguar_oval_washer_BD542-3`](jaguar_oval_washer_BD542-3/) | **BD542/3** oval washer, 3/4" × 1-1/2" with 1/4" hole | Cut, 0.06" (1.5 mm) stainless, qty 50 | v1 ready to order. |
| [`jaguar_radiator_strap_460-043`](jaguar_radiator_strap_460-043/) | **460-043** radiator tie strap (stay) | Cut, stainless 0.125" (leaning) or 0.187"; original is 0.14" | v1 done in two variants: original (8-7/8") and long (+1/8", slot +1/8"); both without the original's two small bracket holes. Small-hole positions, which stay, quantity, variant and final thickness still open. |
| [`jaguar_turn_signal_cover_C23310`](jaguar_turn_signal_cover_C23310/) | **C23310** turn signal switch cover: the missing spring-clip cap half | Moulded plastic: needs 3D modelling/printing or purchase | Tracking only. Buy, source the cap alone, or make one. |

## Folder layout (per part)

- `<part>_vN.dxf`: cut file, units **inches**, drawn 1:1. The highest version marked "current" in the part README is the one to order.
- `<part>_vN.pdf`: full-size print template with dimensions and a 1" check square. **Print at 100% / Actual size.**
- `scripts/`: Python generators (`ezdxf`, `matplotlib`, `numpy`). The DXF and PDF come from the same geometry.
- `images/`: sketches, photos of the original, reference product photos.
- `early_trials/`, `archive/`: superseded versions and duplicates, kept instead of deleted.

The generator bracket folder predates this layout and keeps its files at the top level.

## Not in this repository

Personal photos (hand sketches with measurements and photos taken on the car) are kept in the local folders but left out of git because they carry location data. The part READMEs still list them by name. `jaguar_carb_shield_AUC1054/scripts/auc1054_overlay_photo3_fit_check.py` needs one of those photos and won't run from a fresh clone.

## Running the scripts

```
pip install -r requirements.txt
```
