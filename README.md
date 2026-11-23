# Jaguar XK 150S part designs — 1959, chassis T831957DN

Reproduction and replacement parts designed during the restoration of a 1959 Jaguar XK150 S. Most are flat sheet-metal parts drawn as DXF cut files for laser cutting (and, where needed, bending) at SendCutSend. Each part has its own folder with a detailed README: geometry, where the dimensions came from, open questions and version history.

> **Applicability:** all parts here were designed for and measured on a **1959 Jaguar XK150 S**. Many of the same part numbers were also used on other models (for example other XK150s, XK120/XK140 and E-Type), so these designs may fit those cars too. Check fit and dimensions against your own car before ordering.

## Parts

| Folder | Part | Process | Status |
|---|---|---|---|
| [`jaguar_wiring_box_C13416`](jaguar_wiring_box_C13416/) | **C13416** wiring connector shield: cover over the snap-connector block in front of the radiator | Cut + bend (7 bends), 18 ga steel assumed | Two variants, v3 and v4, differing in TOP depth (2.00" vs 1.75"). Both depths are estimated from product photos; not yet known which is closer to the original. Material, bend values and fold check still open. |
| [`jaguar_battery_supports`](jaguar_battery_supports/) | Battery box supports (no part numbers): rear (hat-section) and front (Z-section) strips under the battery, left and right boxes | Cut + bend; made long to suit both sides, trimmed and drilled on assembly | v1. Made from these dimensions in 0.074" CRS mild steel. No holes in the templates: cut to length and drill on installation. |
| [`jaguar_carb_shield_AUC1054`](jaguar_carb_shield_AUC1054/) | **AUC1054** starting-carburetor dust shield | Cut, 1 mm 5052 aluminum; ears bent by hand | Version A v2 is current. Notch-to-tip length (0.75" vs ~0.80") not confirmed against an original. |
| [`jaguar_generator_bracket_C2286`](jaguar_generator_bracket_C2286/) | **C2286** generator adjustment bracket | Cut, 0.187" sheet | v2 is current. Not yet checked at true size against an original. |
| [`jaguar_oval_washer_BD542-3`](jaguar_oval_washer_BD542-3/) | **BD542/3** oval washer, 3/4" × 1-1/2" with 1/4" hole | Cut, 0.06" (1.5 mm) stainless | v1 ready to cut. |
| [`jaguar_radiator_strap_460-043`](jaguar_radiator_strap_460-043/) | **460-043** radiator tie strap (stay) | Cut, stainless 0.125" or 0.187"; original is 0.14" | v1 in two variants: original (8-7/8") and long (+1/8", slot +1/8"). The original's two small bracket holes are not in the DXFs and are only partly measured. |
| [`jaguar_turn_signal_cover_C23310`](jaguar_turn_signal_cover_C23310/) | **C23310** turn signal switch cover: the spring-clip cap half | 3D printed (original is die-cast zinc); STEP and STL files, in millimeters | v1 draft: outline and column cutouts traced from an original main cover; depth and attachment still estimated. |

Planned improvements are listed in [TODO.md](TODO.md).

## Folder layout (per part)

- `<part>_vN.dxf`: cut file, units **inches**, drawn 1:1. The part README says which version is current.
- `<part>_vN.pdf`: full-size print template with dimensions and a 1" check square. **Print at 100% / Actual size.**
- `scripts/`: Python generators (`ezdxf`, `matplotlib`, `numpy`). The DXF and PDF come from the same geometry. **Only needed to modify and regenerate the files**; see below.
- `images/`: sketches, photos of the original, reference product photos.
- `early_trials/`, `archive/`: superseded versions and duplicates.

## Not in this repository

Hand sketches with measurements and photos taken on the car are not included. The part READMEs still list them by name, marked "not in the repository". `jaguar_carb_shield_AUC1054/scripts/auc1054_overlay_photo3_fit_check.py` needs one of those photos, so it won't run from a fresh clone.

## Running the scripts

The scripts are **only needed if the preview, template (PDF) or DXF files have to be modified and regenerated.** To order or print a part, use the files already in its folder; no Python is required.

To regenerate, install the dependencies once:

```
pip install -r requirements.txt
```

## License and reuse

The designs, drawings, scripts and documentation in this repository are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). You can copy, modify, have parts made from and share them for any purpose without asking permission.

Third-party product and listing photos in the `images/` folders are **not** covered by CC0. They belong to their owners and are included for reference only; each part README lists where they came from.

### Two requests (not legal requirements)

- **Credit the source.** If you use or share these designs, please link back to this repository: `https://github.com/jbest/jaguar_part_designs`
- **Share your feedback.** If you make a part from these files, I'd like to hear how it fit, what you changed, and any measurements from your own car, especially from other models that use the same part numbers. Please open an issue in this repository.
