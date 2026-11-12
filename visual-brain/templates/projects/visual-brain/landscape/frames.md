---
type: index
last_updated: ""
tags: [visual-brain, frames]
---

# Frames

Every image the Visual Brain or Product Visual has looked at, one row each. IDs: `OWN-<source>-<subject>-<nn>` for the brand's own, `CMP-<brand>-<source>-<subject>-<nn>` for shelf brands, `REF-<brand>-<source>-<subject>-<nn>` for references and adjacent. The files live in `raw/visuals/` and stay local.

The first seven columns are Visual Brain's, in the same order, so both plugins write one table. The last five carry what a photo folder needs: the variant it shows (the color as seen, or the line), who is in it (which person or animal, told apart by the marks the owner gave), clean or with text on it, provenance (real, retouched, likely generated, unclear), and the original file name when the photo is read in place or copied. If this file already exists with only the first seven columns, add the five at the end of the header; older rows keep them blank. Competitor and reference images fill them only where they apply.

| Frame ID | Brand | Group | Source URL | Seen on | What it shows | File | Variant | Who is in it | Clean or text | Provenance | Original file name |
|---|---|---|---|---|---|---|---|---|---|---|---|
