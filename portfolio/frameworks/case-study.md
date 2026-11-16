# Case study: the method

A case is the showcase output of a brand run: what a client, a Behance visitor or a buyer of the service sees. The working map of the run (statuses, sources, backlog) is a separate output and stays with the team. The case reads the brains' files and never writes to them.

## Honesty rules (they outrank design)

1. **Status on the cover:** "Strategy proposed", "In testing" or "Results measured". It follows the files: an owner decision [Р] makes it chosen, a dated measurement makes it measured.
2. **Results module** only with data, a date and a source. No data: "Not measured yet" and the test plan. A simulation (AI panel, rival agent) is never presented as buyer research.
3. **Every number** has a source line under it. Brand data is labeled as the brand's own, not as a market total.
4. **About the images** block: what was photographed, what was generated (a background, a scene). Product shape, fit, size, material and color are never generated.
5. **Text on mockups** is only the brand's own lines or facts from its files, and the note says it is temporary. No invented price, review, claim, client logo or metric. A fact not yet confirmed is shown as a placeholder in brackets: "[NAME] / HEAD [__] IN".
6. **Competitor images** stay in the working page. A public case names rivals and shows the map, not their photos.
7. **Private until the owner's "ok".** The case is published as a private artifact; Behance, the site or any upload waits for the owner.
8. **Public privacy.** Keep personal names, contact details, customer or order ids and row-level source links in the private working map. If a quotation would identify a person, use an explicitly labeled synthesis without quotation marks. Never invent a testimonial. Public examples show the approved brand, not private attribution.
9. **Client-facing language:** U.S. English, the owner's voice rules (my-voice skill), no em dashes.

## Modules, B2C (default order)

| # | Module | Reads | Shows |
|---|---|---|---|
| 01 | Cover | positioning-messaging.md (key message), visual-guide.md (lead frame) | Title, one-line summary, discipline tags, status chip, the lead photo |
| 02 | Overview | profile or project file | Client, category, channels, scope, team |
| 03 | Research in numbers | icp.md, baseline | Four big numbers, each with a source line |
| 04 | Insight | icp.md "Their words" | A permitted, anonymized buyer quote or a clearly labeled synthesis; individual record ids stay in the private working map |
| 05 | Market map | visual-guide.md map table or comparison.md | The map drawn to scale from map.json, open space marked |
| 06 | Positioning | positioning-messaging.md | Key message, differentiation, three pillars (problem, answer, proof to build) |
| 07 | Visual direction | visual-guide.md | Every colorway on its ground, three shooting rules, yes / no |
| 08 | Signature | visual-guide.md "Signature element" | The element in use, with the cast or the asset it rests on |
| 09 | Craft or origin | brand files (raw/brand) | Only when the brand has a sourced story (where and how it is made) |
| 10 | **Social** | visual-guide.md, carriers | Profile grid 3x3, feed post 4:5, story 9:16 |
| 11 | **Website** | visual-guide.md, site screenshot, product files | Home first screen desktop and phone, product page top |
| 12 | **Ads and marketplace** | visual-guide.md, Product Visual gallery | Feed ad 4:5, story ad 9:16, marketplace search tile (direction vs the brand now) |
| 13 | How we will know | test plans in the brains' files | Three dated checks; Results box |
| 14 | Credits | all of the above | Team, method, about the images, sources |

Modules 10 to 12 are required. A missing frame becomes a palette tile "To shoot: what exactly", which is the shoot list. A module may be left out only with the reason written in Credits.

## Modules, B2B (services and software)

Cover; overview; the client's problem (in their words, with permission); market and alternatives; positioning; how the work runs (process, stages, what the client does); a sample deliverable (real, anonymized with permission, or marked "demo"); proof (dated measurements, cases with permission; none: "no client results yet" and the method); applications (service page, sales slides, demo frames); how we will know; credits. Never: invented client logos, testimonials, metrics or screens.

## Visual-only case

When only Visual Brain ran: cover; brief; audit of current visuals; market and map; visual change brief; directions next to the current look; the system; modules 10 to 12; pilot and checks; results; credits.

## Design rules

- The palette is sampled from the brand's own photos and logo (Visual Brain's palette.py or the frame grounds), never invented. Each chapter may sit on the ground of one colorway.
- Display type is wide and confident; body type is plain; data labels are mono. Fonts from Google Fonts with fallbacks; the brand's own fonts when the files name them.
- One idea per module. Images large. Numbers large, their source small.
- Chapter numbers are real sequence numbers. No decoration that does not encode something.
- Every module works at phone width; no sideways scroll.
- Single light look by design (a portfolio is a printed piece in spirit); set every color explicitly.

## Behance and PDF

Specs from third-party guides (check them in the Behance upload form before uploading): a module is 1400 px wide, up to 2800 px for retina; the cover is 1400 x 1050 recommended, 808 x 632 minimum. `scripts/export_behance.js` writes one JPG per `section[data-module]` at 2800 px wide and a 1400 x 1050 cover; the command assembles a PDF from the modules.
