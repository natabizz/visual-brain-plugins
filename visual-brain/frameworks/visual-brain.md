---
type: framework
version: 4
source: Visual Brain, Natalia Bizyukova
used_by: /visual-brain:brand, /visual-brain:choose, /visual-brain:page
tags: [visual-brain, visual-direction]
---

# Visual Brain: the brand's visual direction, built from its audience

Visual Brain shows where a brand's look can go. It sits on top of the Marketing Brain: it takes who the buyer is and where the brand stands, studies what this audience responds to and what the market already looks like, and proposes two or three visual directions that attract this audience and that competitors can't wear. Each direction is shown in pictures, on the carriers the brand actually uses (a social media grid, the site's first screen), next to how everyone else looks.

It works at brand level only. A brand without a single product photo can use it. Everything about one product (what it proves, which frames its gallery needs, whether the images are true to it) belongs to the companion plugin, Product Visual, which reads this plugin's output.

## What it is, and what it is not

| Visual Brain is | Visual Brain is not |
|---|---|
| The brand's visual direction: mood, light, how color is used, setting, casting, styling, the signature element | A brand identity: it does not design a logo, a typeface or a palette |
| The brand's own logo, colors and fonts taken as given, and shown used differently and better | A redesign of what the owner already has |
| Shown in pictures: a collage per direction and the same carrier as everyone, now and in each direction | A long written report |
| Built from the audience: what they love, where they look, what they react to, what puts them off | A list of rules invented from taste |
| Located on the market: shelf competitors, aspirational references, adjacent aesthetics | A comparison with the cheapest sellers only |
| Observations and options, each with its basis, for the owner to choose | A list of orders |
| For a brand without an identity: the chosen direction is the brief a designer starts from | A product gallery plan, a size frame, a feature callout |

## Where things live

| Path | Holds | In git? |
|---|---|---|
| `wiki/brand/visual-guide.md` | The brand's visual direction: the file Claude reads before any visual work | yes |
| `projects/visual-brain/landscape/audience.md` | The audience in pictures: vibe, what they love to see, where they look, what puts them off | yes |
| `projects/visual-brain/landscape/landscape.md` | The visual market: every brand looked at, its visual language, the map | yes |
| `projects/visual-brain/landscape/frames.md` | Index of every image looked at | yes |
| `projects/visual-brain/landscape/tests-<date>.md` | Audience panel, rival test, recognition test, the judge | yes |
| `projects/visual-brain/outputs/visual-direction.html` | The page, in the owner's language, with the images inside it | no, local only |
| `projects/visual-brain/outputs/visual-direction.src.html` | The page's source, with image paths | yes |
| `projects/visual-brain/outputs/visual-direction.<lang>.html` | The same page in another language, built by `/visual-brain:page <lang>` | no, local only |
| `projects/visual-brain/archive/` | Earlier versions of the guide, kept before a rewrite | yes |
| `raw/visuals/` | Image files: own, screens, references, boards | no, local only |

## Inputs

| Input | Required? | Where it comes from |
|---|---|---|
| `wiki/brand/icp.md` drafted | yes | Marketing Brain exercise 1 |
| `wiki/brand/positioning-messaging.md` drafted | yes | Marketing Brain exercise 2 |
| `wiki/brand/voice-guide.md` | no: the look and the voice should feel like one person when both exist | Marketing Brain exercise 3 |
| The brand's current images | no: without them, section "Where you are now" is left out | found on the brand's pages; attached in the chat |
| References the owner looks up to | no, but asked once | named in the chat; found in `raw/strategy/`, `raw/visuals/direction/` |
| The product photos: a folder on the owner's computer, or a board | no, but asked once, at the start and again before a choice is written | the owner names a folder path or pastes a board link. Every photo in it is looked at and indexed in `frames.md` by variant (color, line) and by who is in it (see "Photo folders") |
| A moodboard, reference boards (Figma, Pinterest) or a brand book | no | attached or linked in the chat; `raw/visuals/direction/`. Each frame is taken one by one (with a connected Figma tool, one screenshot per frame; without one, the owner exports the frames as images and drags them into the chat) and counts as the brand's own material, first in collages and grids, only when it is the brand's own photo or asset; any other image on a board (another brand's, a stock photo, a found image) is a reference and is marked as one. Text and fonts on them are references, never judged, unless the owner says they are final. An old brand book the owner says is out of date is not followed |
| The brand's site and its social accounts | no | found, then asked once: "Does the brand or the product have Instagram or other social accounts? Links." Only accounts the owner confirms as the brand's or the product's are the brand's "now" |

**Find first, ask last.** The command gathers everything it can from the workspace and the web before it asks. It asks once, in one short message, for what only the owner can give, and never blocks on an optional input: it goes on and marks what is missing "(limited: no X)".

**Files from the owner** come as chat attachments or pasted links, never "put it in a folder". If the session gives a file path, copy the file into `raw/visuals/` (the brand's own images to `own/`, product photos to `products/<product>/photos/`, screenshots to `screens/<source>/<date>/`, references and moodboards to `direction/`), convert HEIC to JPEG on the way (`sips -s format jpeg`), and add a row to `frames.md`. If it gives no path, look at it, add it to `frames.md` as "chat attachment, <date>", ask once to drag the file from Finder into the chat, and say which checks can't run on it until then.

**Photo folders.** When the owner names a folder (a path on the computer, its subfolders included), read the photos where they are: never move, rename or delete them. Open every image. Index each one in `frames.md` with: the variant it shows (the color as seen, or the line), who is in it (which person or animal, told apart by the marks the owner gave: eye or hair color, size), clean or with text on it, and what the owner said it is (a real photo, a retouched one, a generated draft). Copy only the frames the page uses into `raw/visuals/own/<line>/`, keeping the original file name in `frames.md`. PDF selections count only for variants with no separate photos. A folder that changed since the last run is read again before a choice is written.

**Blocked pages.** Some sites and most social networks refuse automated viewing. Then say which pages, ask for screenshots in the chat, and continue. Never describe an image you have not opened.

## The three groups on the market

Every brand looked at belongs to one group, and the page keeps the groups apart:

| Group | Who | Why it matters |
|---|---|---|
| **Shelf** | Who the buyer sees next to you: the hub's competitive alternatives and what a buyer search on the main channel returns | What you must stand out from at thumbnail size |
| **References** | Who the brand wants to stand next to: the owner's named references, premium brands in the category, brands the audience names in reviews and forums | The level of the look and what the audience already admires |
| **Adjacent** | Outside the category: aesthetics the audience follows (an interior style, a fashion label, a photographer, creator accounts) | Where a look can come from that no competitor uses yet |

Owner-named references are always collected. If a site or account can't be reached, the page says what was tried and asks for screenshots: "no frames collected" is never a silent result.

**Brands AI assistants name.** When the workspace holds a list of brands AI assistants recommend in the category (an AI visibility measurement, usually with mention counts), it is a market source of its own: it shows who a buyer meets first when they ask an assistant instead of a search box.
- If the list has the owner's own groups, keep them. Otherwise: the most named go to Shelf; brands that make the same promise go to Shelf as direct competitors; brands the owner calls the level to reach go to References; mass and marketplace brands stay on Shelf, marked "not the bar".
- Collect images only for the grouped brands, within the depth's brand count (framework, "Depth"). The long tail is listed by name with its count, never collected.
- Keep the counts and the date. A brand the owner has not checked stays tagged "from AI answers".
- An AI list is not a list of references: a brand gets into References only when the owner names it as one.
- On the page, the market section shows the most named brands with their counts, and says plainly whether the owner's references appear in AI answers at all. When they don't, say what the most named brands make easy to read (fit, sizes, exchange written as text, for example): that is what an assistant picks up, and it belongs to the site's text, not to the look.

## The audience in pictures

From `icp.md` and the hub, then research where the audience actually is:
- **Vibe:** five to eight words, each with evidence (a quote, an observed pattern in posts, a brand they name).
- **What they love to see:** recurring kinds of images in the places they spend time (the formats, settings, poses, moods that get shared and saved), with links.
- **What puts them off:** images and styles they mock, distrust or complain about, with quotes.
- **Where they look:** platforms and formats, from the ICP and from research, with what the format asks of an image (vertical, carousel, thumbnail, video cover).
- **Pains and desires a look can answer:** identity-level, not product features. "Everything in this category looks the same", "I want people to notice", "made for people like me". Product features (a size, a material) belong to Product Visual.
- **Occasions:** seasons, gifting, events that change what they want to see.

**Images of private people** (forum posts, personal social accounts) are described in words with a link, never embedded on the page. Brand and creator images may be shown as small thumbnails for internal review, with the source named.

## The visual language of a brand

For every brand on the market, and for the brand itself, the same eight lines, each from images that were opened:

| Line | What to note |
|---|---|
| Light | Studio flat, soft window, hard sun, night; contrast |
| Color | The palette as hex sampled from the images (`scripts/palette.py`), saturation, how product color relates to the background |
| Setting | Seamless studio, home, street, nature, staged set |
| Casting | Which people or animals, what type, how many, recurring or not; pose and expression; the role they play |
| Styling | Props, textiles, outfits, how much is in the frame |
| Composition | Crop, angle, eye level, negative space, how the product reads at thumbnail |
| Type and graphics | Text on images, fonts, badges, overlays |
| Mood | One line a photographer would recognize, with the frames that show it |

Then: **who it speaks to** (which part of the audience, with evidence) and **price point** (from the brand's own page, dated).

## The map

Two axes chosen from what the brands actually differ on, never from a stock template. Each axis is named by its two ends in plain words ("playful and loud" to "calm and refined"; "for everyone" to "made for one type"). Every brand is placed with a one-line reason. The map's job is to show **empty space**: a position the audience would value that no shelf brand holds. If there is no empty space, say so, and say where the least crowded position is.

## Where the brand is now

Only when the brand has images. The brand's look on the map, by the same eight lines. Then, as observations with a basis:
- **Strengths:** what already reads as the brand's own.
- **Where it lags:** what references do that the brand doesn't, and what the audience would miss.
- **Consistency:** do the brand's images read as one brand? The recognition test answers it.
- **Discrepancies:** verifiable contradictions in the brand's own materials (two different logos, a claim on an image that the brand's own files contradict). These are stated as facts, with both sources. Judge the brand's own materials by the same standard as competitors': a gap you would point out in a rival's work, point out in the brand's.
- **The site now:** when the brand has a live site, a screenshot of its first screen (a connected browser tool, or one screenshot from the owner) and up to three observations: does it follow the brand's own layout rules, does its description for search and AI match the position.
- **On the owner's boards,** look at the frames: the face, the light, the poses, what is missing for this audience. Text and fonts on them are references and are not judged unless the owner says they are final.

## Directions

Two or three visual territories, never one, and different in more than color. When the owner already has a direction (a moodboard, reference boards), build from it: its strongest part is one direction, what it lacks for this audience is another. Each direction has:
- **a name and one line** a photographer could picture;
- **three words yes and three words no**, so a stranger can tell an image in from an image out;
- **a collage:** six images, the brand's own best clean frames first (the brand's own photos from the owner's boards count as own), at most two from references or adjacent brands, marked as such; a brand with fewer than four own frames fills the rest with references, every one marked, and says so; plus the palette and one line the brand already uses, set in the brand's own font (template block "scape"). No listing infographics, badges or text-heavy frames in a collage;
- **a palette:** up to six distinct colors sampled from the direction's images (`scripts/palette.py`, "Palette for the set"), each named by its role in plain words. When the brand sells a range and the direction sets a rule per variant (a backdrop in the piece's own color, say), the palette is the set of pairs from "Every variant", never one variant's colors standing for the brand;
- **how to shoot:** three rules specific enough for a photographer or an image generator;
- **the signature:** the recognition device, or a plain "none" when the direction has none;
- **why it fits the audience:** the vibe words, loves and pains it answers, with their evidence;
- **how it differs:** where it sits on the map, and which shelf brands it moves away from;
- **what it asks for and the risk:** casting, locations, production level; what could go wrong, who it could lose;
- **the test results:** the panel's rank and words, the rival's verdict.

One is marked **recommended**, with the reason, and with what it takes from the others. A direction is a look, not a proof format: frames that prove the product (a size card, a how-to grid, a fabric close-up with text) belong to Product Visual's galleries, so a direction is never recommended for its proof frames alone. The recommendation weighs what stops the audience (the panel's "stops me" rank) and what a rival can't wear; what answers their worry is carried into "What to do next" and into Product Visual.

The owner chooses, and may combine: the look of one direction, the cast of another, proof moved to product cards. The choice is recorded as given. Until then, the visual language section is written for the recommended direction and tagged (inferred).

## Every variant: the range

When the brand sells a range (colorways, lines, flavors), a direction must hold across it, not on one variant, and the owner must be able to see that even when photos of most variants don't exist yet. For the recommended direction, and again for the chosen one, the page shows one row per variant:
- **The pair:** the product's color (sampled from a real photo of that variant with a box around the product, or taken from the product file) and the backdrop or ground the direction's rule gives it, as hex. `scripts/range.py` computes both.
- **The check at tile size:** a color heuristic, then the eye. `range.py` measures how far the product's color sits from its backdrop (CIEDE2000 15 or more, lightness gap 10 or more: working thresholds, not a standard). Below that, the product's edge tends to sink into the backdrop in a marketplace tile or a feed thumbnail. The sheet shows every pair at tile size, and the verdict on the page comes from looking at it, with the numbers as support. When the direction's rule is not a tonal backdrop (a fixed neutral, say), its own backdrop is checked with `--own`. Then it shows three more backdrops (deeper and quieter, lifted, a quiet neutral), and the page says which pass.
- **The example, in this order:** the brand's own clean photo of that variant on the rule's backdrop or close to it; the brand's own photo with only the background replaced by the rule's color (`range.py --previews`, when the cut-out library is installed; the product and whoever is in the frame untouched; captioned "preview: background replaced"); a reference showing the same device on another brand, marked; a "To shoot" tile in the backdrop's own color, with the frame described.
- **Options side by side:** for the lead variant, and for any variant that fails the check, the passing backdrops on the same real photo, next to each other, so the owner chooses by eye, not by hex. A variant that passes shows its example only: the options sheet is not repeated for it.
- **The owner's eye decides the format.** A pair the owner likes may stay for large formats (the site's hero, social, a lookbook) even when it fails the tile check: at full size the edge reads. The tile formats (a marketplace search, a small grid) then take a passing option, and the page shows both, each labeled with where it is used.

A brand with one variant gets one row and its check. A brand with no photos at all gets the pairs from its product colors, references and "To shoot" tiles: still the whole system, with what to shoot named. The previews show the idea; they are never published as product images.

## Carriers: the same thing, three ways

The page shows each direction where the buyer will meet it, next to how the category looks, so the difference is seen, not explained.

| Carrier | Columns | Built from |
|---|---|---|
| Social media grid, 3 by 3 (the brand's main network; an Instagram-style grid unless the owner names another) | As everyone (shelf images), now (only the brand's own account), each direction | Nine images per column; at most one text tile |
| Site first screen | Now (a screenshot of the live home page, when there is a site), each direction | Logo, a hero image, a band with one line and a button under the image, a row of four images |
| Another carrier the owner names (a marketplace card, a newsletter header, an insert in the parcel) | As above | Only when asked |

Rules for mockups:
- Text on a mockup is only a line the brand already uses or a fact from its product files, in the customer's language, and the note under the carrier says it is temporary. Never an invented claim, price or review.
- Follow the brand's own layout rules (where text may sit, what may cover the product). Text never covers the person, the animal or the product unless the brand's rules allow it.
- A mockup is a sketch of the direction, not a site design. The note says so.
- **Clean frames only.** Grids and site mockups take photos without text overlays, badges, infographics or screenshots of listings, and never another brand's images. When a direction has fewer clean frames than tiles, the missing tile is a color tile from the direction's palette with "To shoot:" and what exactly (in the page language): it shows the gap and becomes the shot list.
- **In hand first.** Before a tile becomes "To shoot", look through the indexed own photos for that variant and that cast member. A tile is "To shoot" only when none fits, and the shoot list says why (wrong variant, text on it, a pose against a rule, the product redrawn). A background-replaced preview may fill a tile only when the page captions it as a preview.
- **The whole range.** When the brand has several variants, the grid shows at least three of them in turn (or all it has), and the site's row of four shows more than one. Nine tiles of one variant fail VB.14.
- **After the choice,** the chosen direction's column comes right after "as everyone" and "now"; the other directions' columns move into a collapsed block "Other directions (not chosen)" under the carrier.

## What to do next

The page ends with recommendations a person can act on, for the owner and for anyone running the plugin. For the recommended direction (and again for the chosen one):
- **Actions, by priority:** up to eight, grouped "now", "next", "later". Each says what to do, why (its basis on the page: a pain, a gap, a test result, a discrepancy), and what it takes (a shoot, a fix on the site, a decision). Fixes found in "Where you are now" (a size table that disagrees with itself, text over the product, an old description for search and AI) go here.
- **The first shoot list:** the nine frames of the first social media grid and the site's hero, each with what it shows, who (which animal or person), where, light, and the need it answers. Built from what is in hand: frames already in hand are named with their file; the rest are marked "to shoot", each with the reason no photo in hand fits. Who goes in a "to shoot" frame follows the cast rule (the lead in the first frame, everyone in turn, two of different builds where size matters), never at random, and the list says why each one. The backdrop of each frame is the pair from "Every variant" that passed the check.
- **Handed to Product Visual:** the proof frames the audience asked for (size, fit, how it is used), as a short list for `/product-visual:new`.

## Depth

| Depth | When | Market | Frames per brand | Tests |
|---|---|---|---|---|
| Standard (default) | Most brands | about 10 brands: the owner-named references first, then the most named brands of an AI list, then the top of the shelf | 4 to 6 | panel, rival, recognition, judge (one pass) |
| Quick (`/visual-brain:brand quick`) | A first look, a brand with few competitors, a demo | up to 6 brands: the owner-named references and the top of the shelf | 4 | panel, rival, judge (one pass) |
| Full (`/visual-brain:brand full`) | The owner wants the wide picture | all owner-named references, the grouped brands of an AI list, the main shelf: about 15 to 20 brands | 6 to 8 | panel, rival, recognition, judge (at most two passes) |

Say the depth and a rough time at the start (standard: about half an hour to forty minutes; quick: about twenty minutes; full: about an hour), so nobody mistakes a long run for a stuck one. Owner-named references always count first; a brand cut by the depth is listed by name with the reason.

## Visual language of the chosen direction

The same eight lines as above, written as the brand's own, each with reference images:
- **Palette:** hex values sampled from the brand's assets and the direction's images, named by role (ground, product, accent, ink). Never a palette from taste. With a range, the palette is the table of pairs from "Every variant" (product, backdrop, check), plus the brand's ink.
- **Light, setting, composition, styling:** each specific enough that a photographer could plan a shoot from it.
- **Casting:** which people or animals, recurring or not, pose and expression. If the brand has its own animals or people, say how they become recognizable.
- **Type and graphics on images:** from the brand's logo and assets; how little text the look allows.
- **Signature element:** the recognition device. Up to three candidates, each run through the rival test; recommend the one a rival could not wear and keep true.
- **Use and avoid:** each with an image and a reason.
- **By format:** how the look adapts where the audience looks (marketplace thumbnail, site hero, vertical video, carousel).

## Tests

Every test is run by an agent that did not write the work, and every result says it comes from an AI simulation, not from people. Agents can't list a folder: give them file paths.

| Test | Agent | Question | Fails when |
|---|---|---|---|
| Audience panel | `visual-brain:audience-panel` | Shown the direction boards blind (numbered, no names, logos masked), as the ICP buyer: two ranks, kept apart: what stops you, and what answers your worry; what feels off, and why | The recommended direction is not first on "stops me", and the page does not say why it is still recommended |
| Rival test | `visual-brain:rival-director` | As the strongest shelf brand: could you adopt this direction tomorrow and keep it true? | A recommended direction or signature a rival could wear unchanged |
| Recognition | `visual-brain:fresh-eyes` | Only when the brand has images: 9 to 12 images from three brands, shuffled and masked: group them by brand | The brand's own images are not grouped together (the look is not consistent) |
| Judge | `visual-brain:gate-judge` | Runs the gate below on the output files alone | Any blocking check fails |

Offer the human version of the audience panel once: five people from the audience, the same boards, the same questions.

## Gate VB

| Check | Question | Type |
|---|---|---|
| VB.1 Audience-grounded | Does every direction and every visual-language line cite audience evidence (a quote, a pattern with links, a brand they name)? | Blocking |
| VB.2 Market-located | Does every direction say where it sits on the map and which shelf brands it moves away from, with images? | Blocking |
| VB.3 Not a rival's | Did the rival test run on every direction and the signature, with the result on the page? | Blocking |
| VB.4 Images, not adjectives | Does every visual-language line have a reference image, and every palette value a sampled source? | Blocking |
| VB.5 References collected | Was every owner-named reference collected, or is "could not get, tried X" on the page? | Blocking |
| VB.6 Observations, not orders | Are judgments written as observations or options with their basis, and facts (discrepancies) with both sources? | Blocking |
| VB.7 Own work judged equally | Is the brand's own material held to the same standard as competitors'? | Flag |
| VB.8 Readable | Does the page open with a short version, carry no internal codes, and end with sources? | Flag |
| VB.9 Shown on carriers | Is every direction shown on the social media grid and the site first screen, next to "as everyone" (and "now" when it exists)? | Blocking |
| VB.10 No invented copy | Is every line on a mockup the brand's own line or a fact from its files, marked temporary? | Blocking |
| VB.11 Identity left alone | Does the page leave the logo, typeface and palette design alone, and show the brand's own assets used differently? | Flag |
| VB.12 Clean carriers | Do grids and site mockups hold only clean frames of the brand, with "To shoot" tiles where frames are missing, and no other brand's images? | Blocking |
| VB.13 Actionable | Does the page end with "What to do next" (actions by priority, each with its basis) and the first shoot list? | Blocking |
| VB.14 Whole range | When the brand has several variants: does the recommended or chosen direction have a pair, a tile-size check and an example for every variant, and does the grid show at least three variants (or every variant, when the brand has fewer)? | Blocking |
| VB.15 In hand first | Does every "To shoot" tile and shoot-list frame say why no indexed own photo fits, and does the cast in it follow the cast rule? | Blocking |

A failed blocking check is rewritten from the inputs. What the inputs can't fix goes on the page under "To check and decide", in plain words.

## Writing the page

The page is a direction book: it reads like a brand presentation, one idea per screen, images large, one to three lines of text each. Template: `frameworks/direction-book-template.html`. Order: cover with the thesis and a three-line summary; the market (a wall of shelf images, three patterns, the references, three things nobody does); the audience (five vibe words with quotes, three pains); where the brand is now (its images, strong and worth a look, the site now); the directions, each recommended or chosen one with its "Every variant" rows; the carriers; the tests; the choice; what to do next and the first shoot list; sources.

- **After the choice:** the cover image comes from the chosen look; the chosen direction's section comes first, with its "Every variant" rows; the directions not chosen sit in one collapsed block "Other directions (not chosen)" (`<details class="more others">`), kept, not deleted. Placeholders on mockups (a size still to confirm, a name not yet given) are shown as placeholders, in gray brackets ("Name · [size?]"), never as final copy and never left empty.
- **Detail on demand.** Each list shows its three strongest items; the rest sit under "All observations" (a `<details>` block), so the page stays short and nothing found is lost.

- **Language.** The page is written in the language the owner writes in. The `.md` files stay in the language of the brand's customer copy. Customer quotes stay verbatim, with a short translation under them when the page language differs. Text inside mockups stays in the customer's language. `/visual-brain:page <lang>` builds the same page in another language (for colleagues, for example) from the same files, without new research.
- **Images** go in as `src="file:<path>"` in `visual-direction.src.html`; `scripts/embed.py` builds the page, storing each image once even when it appears in the collage, the grid and the site mockup. Image data is never pasted or printed in the chat.
- **Plain words.** No frame IDs, gate codes or tags on the page. Images get plain captions: brand, what it shows, where and when it was seen. Quotes are cited by platform, product and date. The `.md` files keep the IDs.
- **Observations, not orders.** "What we see", "worth a look", "options". The owner decides. Facts that contradict each other name both sources.
- **Every claim has its basis next to it:** which images, which brands, which quotes.
- **Generated images** of the brand, when used, are said to show the idea, not finished photos.
- Competitor and reference images are shown for internal review only; the footer says so.

## Talking to the owner

- **Before:** one summary of what was found and what could not be got, up to six optional questions (the photo folder, references, what must not change, wants and don't-wants, a list of brands AI assistants recommend, the brand's social accounts), then "say go". Never block on optional inputs.
- **During:** one line per stage ("Step 2 of 10: the market, 10 brands"). No running commentary on each image.
- **When you need the owner:** end the message with a line that starts **"Waiting for you:"** and the exact question, so it can't be mistaken for the end of the run.
- **After:** at most five lines and the page link. The detail lives on the page and in the files.

## Stage

| Stage | Means |
|---|---|
| **hypothesis** | Required inputs missing, or the tests not run |
| **tested** | Tests run, no blocking fail, the owner has not chosen a direction yet |
| **chosen** | The owner chose a direction; the date is in Decisions |
| **validated** | Product Visual's dated results support the direction; set only with the owner's yes, in Decisions |

## Limits

- Tests are AI simulations. They show what reads clearly and what is distinct, not what sells.
- The plugin does not publish, contact anyone, or spend on image generation without the owner's yes.
- Competitor and reference images are evidence of what they show, never material to copy.
- The plugin reads the Marketing Brain files and follows their format; it does not copy the Marketing Brain's framework text.
