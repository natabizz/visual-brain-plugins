---
description: Portfolio. Build a professional case study (Behance-style) from the brand's Marketing Brain and Visual Brain files, with social, website and ad layouts, export modules for Behance and a PDF, without publishing anything.
argument-hint: "[case name] [brand | visual | b2b] [export]"
---

# /portfolio:case

Turn a finished brand run into a case study a professional studio would show: image-led modules, 1400 px wide, with the social grid, website and ad layouts in the brand's chosen or recommended look. The case reads the brains' files and never writes to them.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/case-study.md` first. Look at `${CLAUDE_PLUGIN_ROOT}/templates/case-b2c.example.src.html` (a full B2C case, Fabulous Fido, 2026-11-14) for structure, CSS and module markup.

0. **Setup, once.** Make `projects/portfolio/` and `projects/portfolio/outputs/`. Add `projects/portfolio/outputs/*.html` to `.gitignore` if missing. Exports go to `raw/visuals/portfolio/<case>/behance/` (raw/visuals is already local-only; if not, add it).
1. **Mode.** `brand` (default): Marketing Brain and Visual Brain ran. `visual`: only Visual Brain. `b2b`: a service or software brand. Case name: the argument, or `<brand>-case`.
2. **Inputs, and stop if they are missing.** Read: `wiki/brand/icp.md`, `positioning-messaging.md`, `visual-guide.md`, the brand's choice and change records when they exist, `projects/product-visual/*/product.md` for product facts, `raw/visuals/own/` for photos. If `icp.md` or `positioning-messaging.md` is `status: template`, or `visual-guide.md` has no directions, say which brain comes first and stop. List in the chat what each module will read and what is missing.
3. **Status.** Set the cover status from the files: chosen by the owner [Р], measured, or proposed. Never higher than the files allow.
4. **Write** `projects/portfolio/<case>/case.src.html` from the example's CSS and module markup, with this brand's content: `data-img="<workspace path>"` for every image, `<!--MAP-->` where the market map goes, and `projects/portfolio/<case>/map.json` from the brand's map table (same shape as `templates/map.example.json`). Sample the palette from the brand's own photos (Visual Brain `scripts/palette.py` when installed, or the ground colors of the frames). Text in U.S. English by the owner's voice rules; every number with its source line; the mockup rules from the framework (brand lines only, placeholders in brackets, "To shoot" tiles for missing frames).
5. **Build:** `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build.py" --root . --map projects/portfolio/<case>/map.json --out projects/portfolio/outputs/<case>.html projects/portfolio/<case>/case.src.html`. Needs Pillow (Visual Brain's `plugin/ensure-pillow.sh` installs it).
6. **Check.**
   - Mechanical: `node "${CLAUDE_PLUGIN_ROOT}/scripts/qa.js" projects/portfolio/outputs/<case>.html`. Fix every FAIL and rebuild.
   - Content, line by line against the framework's honesty rules: status, results, sources, images, mockup text, competitor images. For a public copy, remove personal names, contact details, customer and order ids, and individual review identifiers; keep the traceable sources in the private working map. A synthesis must not look like a verbatim testimonial. Then one look at the rendered page (a screenshot at 1400 px and at 400 px) for clipped text, empty phones and collisions. One pass of fixes, then go on.
7. **Export** (when the argument says `export`, or the owner asks): `node "${CLAUDE_PLUGIN_ROOT}/scripts/export_behance.js" projects/portfolio/outputs/<case>.html raw/visuals/portfolio/<case>/behance`, then resize `00-behance-cover.jpg` to 1400 x 1050 and assemble `<case>.pdf` from the numbered modules with Pillow.
8. **Show:** publish the built page as a private artifact (only the owner sees it) if this session can; otherwise give the file path. Never upload to Behance, a site or a channel: say that publishing waits for the owner's "ok".

Close in three lines: where the page and the exports are, the cover status and why, what is missing (frames to shoot, facts to confirm).
