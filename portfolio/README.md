# Portfolio

Turns a finished brand run into a case study that looks like a studio made it: image-led modules 1400 px wide, with the brand's social grid, website and ad layouts in its chosen look, plus a Behance export and a PDF.

- **Reads:** `wiki/brand/icp.md`, `positioning-messaging.md`, `visual-guide.md`, Product Visual's product files, the brand's photos in `raw/visuals/own/`. Never writes to them.
- **Writes:** `projects/portfolio/<case>/case.src.html` and `map.json` (in git), the built page in `projects/portfolio/outputs/` and the exports in `raw/visuals/portfolio/<case>/` (both local-only: they carry images).
- **Command:** `/portfolio:case [case name] [brand | visual | b2b] [export]`.
- **Honesty first:** the cover carries the real status; results only with data; every number sourced; generated parts of images named; nothing published without the owner.

Needs Python 3 with Pillow, and Node with Playwright for the checks and the export.

Example: `templates/case-b2c.example.src.html` (Fabulous Fido, 2026-11-14) with `templates/map.example.json`.

The public Fabulous Fido example omits personal attribution and individual review identifiers. Its feedback text is labeled as synthesis, not a customer quotation. Keep row-level evidence in the private working map. The example is a historical layout draft; replace its data and verify image provenance before using it as a current case.
