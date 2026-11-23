# To do

## Templates (PDF) and previews

Update the print templates so they are consistent across all parts, then regenerate the PDFs and preview PNGs from the scripts. The DXF cut files don't need to change.

- [ ] Use one title block layout on every template: part number, part name, version and date.
- [ ] Use American spelling (for example "center", not "centre") in template text and script comments.
- [ ] Add the license: "CC0 1.0 (public domain)".
- [ ] Add a link to this repository: https://github.com/jbest/jaguar_part_designs
- [ ] Add a link to the author's Jag-Lovers forum profile (user trimtab; the C13416 template already names it). Profile URL: _to add_.
- [ ] Add a short request for feedback, pointing to the repository's issues.
- [ ] After regenerating, check that each template still prints at true size (1" check square) and that the regenerated DXFs are unchanged.

## Other

- [ ] Generator bracket C2286: add the missing v2 preview PNG (`python3 scripts/build_C2286_bracket.py v2`), as the other parts have one.
