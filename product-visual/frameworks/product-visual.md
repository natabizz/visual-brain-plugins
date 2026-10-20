---
type: framework
version: 2
source: Product Visual, Natalia Bizyukova
used_by: /product-visual:new, /product-visual:gallery, /product-visual:audit, /product-visual:qa, /product-visual:ai-read, /product-visual:review, /product-visual:page, /product-visual:setup
tags: [product-visual, product-images]
---

# Product Visual: a product's look, built from what its audience needs to see

Product Visual builds the visual side of one product, from scratch or from a live listing. It starts from people, not from frames: who this product is for, what they need to see before they buy, what the product can truthfully show, and how competitors already show it. From that it sets the product's positioning and UVP, a visual direction (what to show and how), and only then a storyboard: the product's images frame by frame, each with its job, what is in it and from where, the text on it and how it looks, with a brief for each.

It reads the Marketing Brain (the buyer and the brand's position) and the Visual Brain (the brand's look and the direction the owner chose). A product built here looks like the brand and answers its own buyers.

It is not only for online stores. The product may live on a marketplace, on the brand's own site, in search results, in social posts and ads, or somewhere the owner names (a catalog, a retailer deck). The storyboard works the same way everywhere; the channel sets the count, the rules and how the page shows it.

## Commands

| Command | When | Writes |
|---|---|---|
| `/product-visual:new <product>` | A product with no gallery yet, or one to rebuild from zero | facts, audience, market, positioning, direction, the first gallery and its briefs, the product page |
| `/product-visual:gallery <product> <channel>` | Another channel, or after you choose another positioning or direction | the gallery and briefs for that channel; updates the product page |
| `/product-visual:audit <product> <channel>` | A live gallery: what each image does for the buyer | the audit and its page |
| `/product-visual:qa <product> <channel>` | Finished images, before upload | the QA, the release list, its page |
| `/product-visual:ai-read <product> <channel>` | How AI reads the listing, before and after a change | the AI reading |
| `/product-visual:review <product> <channel>` | After publication, on dated results | the results and one next action |
| `/product-visual:page <product> [language]` | The product page again, in the owner's language or another one | the page, from the files |
| `/product-visual:setup` | Once per workspace | the product folder template, the local-only image folder, a section in CLAUDE.md |

## Where things live

| Path | Holds | In git? |
|---|---|---|
| `projects/product-visual/<product>/product.md` | Facts (each with a source), inputs, the owner's direction, decisions | yes |
| `.../audience.md` | Who this product is for and what they need, ranked | yes |
| `.../market.md` | Competing products: what they say and what they show | yes |
| `.../positioning.md` | The product's positioning, UVP options, messages, allowed and not allowed claims | yes |
| `.../direction.md` | Visual direction options for the product, tests, the chosen one | yes |
| `.../gallery-<channel>.md` and `briefs/<channel>/` | The gallery plan and one brief per frame | yes |
| `.../audit-<channel>.md`, `qa-<channel>.md`, `ai-read-<channel>.md`, `results-<channel>.md`, `release-<channel>.md` | Checks and results | yes |
| `.../issues.md` | Every finding, never deleted | yes |
| `projects/product-visual/outputs/*.src.html` | The pages' sources, with image paths | yes |
| `projects/product-visual/outputs/*.html` | The built pages, with the images inside them | no, local only |
| `raw/visuals/products/<product>/` | `photos/` (real photos), `drafts/<channel>/`, `finished/<channel>/` | no, local only |
| `raw/visuals/screens/<brand>/<date>/` and `raw/visuals/boards/` | Other brands' images, boards for tests | no, local only |

The product's slug is lowercase with hyphens: `ceramic-mug`. The channel is where the product's images are seen: `amazon`, `etsy`, `walmart`, `site`, `google`, `instagram`, `ads`, or a short name for what the owner names (`catalog`).

Every image looked at gets a row in `projects/visual-brain/landscape/frames.md` (created by setup if Visual Brain is not installed): `OWN-<channel>-<product>-<nn>`, `CMP-<brand>-<channel>-<product>-<nn>`, `REF-<brand>-<source>-<subject>-<nn>`.

## Inputs

| Input | Required? | Where it comes from |
|---|---|---|
| The buyer and the brand's position | yes | `wiki/brand/icp.md`, `wiki/brand/positioning-messaging.md` |
| The brand's look and the chosen direction | no, but strongly recommended | `wiki/brand/visual-guide.md` from Visual Brain (`stage: chosen` after `/visual-brain:choose`); without it, everything that depends on it is marked "(limited: no brand look)" |
| Where the product lives | yes | the owner, asked once if the workspace doesn't say: a marketplace (which), the brand's own site, search, social or ads, or something else |
| Product facts: what it is, material as on the label, origin, measurements, sizes and how to choose, variants, price, care (only those that apply; the rest "not applicable") | yes, the essentials that apply | product files in the workspace, label photos, specs, the owner in the chat |
| Real photos of the product | no for `new` (the gallery then plans a shoot); yes for `audit` and `qa` | a folder the owner names (read in place); attached in the chat; `raw/visuals/products/<product>/photos/` |
| A moodboard or ideas | no | attached in the chat; treated as direction, tested like everything else |
| Reviews and questions | no | `raw/voc/`; the product's own pages; competitor products' reviews |

**Find first, ask last.** Gather from the workspace and the web first; ask once, in one message, for what only the owner can give. Optional inputs never block: continue and mark what depends on them "(limited: no X)".

**Files from the owner** come as chat attachments or pasted links. If the session gives a file path, copy the file into `raw/visuals/products/<product>/` (photos to `photos/`, drafts to `drafts/<channel>/`, finished images to `finished/<channel>/`, moodboards to `raw/visuals/direction/`), convert HEIC to JPEG on the way (`sips -s format jpeg`), and add a row to `frames.md`. If it gives no path, look at it, add it as "chat attachment, <date>", ask once to drag the file from Finder into the chat, and say which checks can't run on it until then (the shelf, boards, pixel checks and the page need the file itself).

**Photo folders.** When the owner names a folder (a path on the computer, its subfolders included), read the photos where they are: never move, rename or delete them. Open every image. Index each one in `projects/visual-brain/landscape/frames.md` with: the variant it shows (the color as seen, or the line), who is in it (which person or animal, told apart by the marks the owner gave), clean or with text on it, and what it is (a real photo, a retouched one, a generated draft), as the owner said or asked once. Generated drafts never stand in for real photos in proof frames. Copy only the frames the page uses into `raw/visuals/products/<product>/photos/`, keeping the original file name in `frames.md`. Near-duplicates (the same frame exported twice) count once.

**People in research.** Images of private people (review photos, forum and social posts) are described in words with a link, never saved or shown. Quotes keep no names, emails or order numbers, and are cited on the pages by platform, product and date.

**Facts have sources.** A label photo, a factory spec, a measurement the owner took, an approved document. Text on a live listing is not a source: it is one of the things being checked. A fact without a source stays blank with a question.

**Channel rules** (image count, sizes, what the main image may show) come from the channel's own current help page, saved with its URL and date, or from the owner (a screenshot when the page is behind a sign-in). Never from memory. A third-party guide may point to a rule but is tagged "(third-party: <site>, <date>)" and never decides a blocking rule alone.

**The chosen direction.** When Visual Brain has run, the product follows the direction the owner chose. Read from `visual-guide.md`:
- **The look:** the "Chosen" section and the Visual language section (backdrop, light, pose, styling, composition, type on images, palette).
- **The cast:** who may appear (named animals or people), who is the lead, and whether one may be swapped for another.
- **The caption rule:** what is written under brand images (for example "Name · size") and what only product cards carry (for example the measurements).
- **What was handed over:** "Handed to Product Visual" (or a "Product cards" section): the proof frames the audience asked for and how they look.
- **What to do next and the first shoot list:** fixes and shoots already planned at brand level, so the product's shot list joins them rather than repeating them.
- **Decisions:** every owner rule (what may never change in the product, where text may sit), followed as written.
- **The rival tests:** what the strongest competitors could copy and what they could not.

If the guide is in `format: visual-brain-2` but has no chosen direction yet, say so once: `/visual-brain:choose` first, or "go" to work on the recommended direction, tagged (inferred) everywhere it is used.

## Channels: where the product lives

| Kind | Examples | What the storyboard plans | Carrier on the page |
|---|---|---|---|
| Marketplace | Amazon, Etsy, Walmart, a category marketplace | The listing gallery: the main image, then the rest in the buyer's order | The product's card in a search next to three competitors, and its gallery |
| Own site | The brand's product page | The product page gallery and the first screen of the page | The product page's first screen (image, name, price, button) and the gallery strip |
| Search | Google Shopping, image results | The image that shows in the results, and the page it opens | The result card among three competitors for the buyer's search |
| Social and ads | An Instagram carousel, an ad set | A carousel or a set of ads, first frame first | A phone with the carousel's frames in order |
| Other | A catalog, a retailer deck, a line sheet, a printed insert | As the owner describes it | As described, only when asked |

The storyboard's logic is the same for every kind: needs first, frames in the buyer's order, one job per frame. What the channel changes: the count, its dated rules, the first frame's job (stop the scroll in a feed; win the click in a search; say what it is at a glance on a shelf), and the carrier on the page. A brand that sells through retailers only, or has no store yet, picks the place its buyers will meet the product first; the storyboard is the product's set of images for that place.

## Needs: what the audience must see

The center of the method. For this product, the audience's needs, ranked:

| Kind | What it is | Example of where it shows up |
|---|---|---|
| **Pain** | What goes wrong with products like this | "falls apart after two washes" |
| **Desire** | What they want to feel or have | "people ask where I got it" |
| **Objection** | Why they hesitate before buying | "which size, and what if it's wrong?" |
| **Trigger** | What makes them buy now | a new season, a gift, a trip |
| **Vibe** | What their world looks like and what they respond to | from the Visual Brain's audience |

Sources, in this order: the brand's own reviews and questions for this or similar products; competitor reviews and questions for this product type; forums and social posts where the audience talks; the ICP. Each need gets a count (how many sources say it), a quote, and the source IDs. Rank by how often it comes up and how much it blocks a purchase.

## Positioning and UVP

The product's place: for whom, against what, and why this one.
- **Two or three UVP options.** Each: the need it answers (from the ranked list), what the product has that makes it true (from the facts), the proof available (document, photo, review, or none), and how competitors talk about the same thing.
- One is **recommended**, with the reason. The owner chooses.
- **Messages:** the main message, and up to three supporting ones, in the voice guide's words and the vocabulary.
- **Claims:** allowed (with proof) and not allowed (no proof, or the facts say otherwise).

## Visual direction for the product

Inside the brand's look, two or three options. When the brand has a chosen direction, the look is already set: the options differ in what the product's images tell (the hero story, which proof leads, which of the cast and in what situation), not in the brand's look.

Each option:
- **The hero story:** the one idea the whole gallery tells, in one line.
- **Supporting stories:** three to five, each tied to a ranked need or the UVP.
- **How it looks:** mood, setting, casting, light, styling, color story, within the brand's visual language; where it departs from it, say why.
- **Board:** six to nine images: the product's own clean photos first, then the owner's moodboard, references and competitor products, the last two marked as such.
- **Why it fits the audience,** **how it differs** from the competing galleries (with images), **what it asks for** (shoot, casting, locations, retouching, generation), **risk.**

One is **recommended**, with the reason: what stops the audience (the panel's "stops me" rank), what answers their worry (the second rank), and what the rival can't wear. The owner chooses.

## The storyboard (the gallery)

The storyboard is the gallery planned frame by frame, before anything is shot or made. Frames come from the needs and the stories, never from a checklist of angles.
- **Count:** the number of priority needs and stories, within the channel's dated limit and the owner's number. More needs than the limit: say which go to the listing text. A frame with no need is dropped.
- **Order:** along the buyer's path on that channel: stop (the first image), understand, believe, choose, picture it in their life.
- **Each frame, one card:**

| Field | What it says |
|---|---|
| Job | Its step on the buyer's path, in a few words ("stop", "which size", "does it fit") |
| Need | The need it serves, with a buyer's quote and its source |
| In frame | What is in it: the product on the animal or person, the product alone, a detail, two sizes side by side, hands showing how, the product in a real place, what arrives in the box |
| View | From where: front, three-quarter, side, back, top, close-up of a named detail; the crop |
| Who | Which of the brand's cast, and why this one (the lead for the first frame, two different builds for a size frame) |
| Text | The exact words on or under the image, or "no text"; where they sit, by the brand's rules |
| Look | Backdrop, light and color from the chosen direction; for proof frames, the look handed over for them |
| Proof | What makes the frame true, and its source (a measurement, a label, a document, a review) |
| Image | The nearest image in hand: a real photo, a reference marked as one, or "To shoot: what exactly" |
| Route | Shoot, retouch, background only, layout |
| Copyable | Whether the strongest competitor could make the same frame tomorrow, from the rival tests ("not tested" for frames the rival didn't see); the first frame carries at least one thing it can't |

- **Views check.** From the ranked needs and the buyers' questions, list the views this product's buyer needs to see (for a bag, for example: the front and the side, the closure and the strap close up, the inside, two sizes side by side, how it is carried, the product alone). Each view is covered by a frame, or moved to the listing text with the reason (the count limit). A view nobody asks for gets no frame.
- **The cast and the caption** follow the chosen direction: only the cast it names, the lead where it says, the caption rule on brand images, and the measurements only where the handed-over proof frames put them.
- **Briefs:** one per frame, standalone: a designer, photographer or image tool can work from it without the chat.
- **What is never generated:** anything that shows fit, size, a material, a test or the product's construction. The product is never redrawn, recolored or regenerated; backgrounds and settings may be.

## What to do next

The product page ends with what to do, for the owner and for anyone running the plugin:
- **Actions, by priority:** up to six, grouped "now", "next", "later". Each says what to do, why (its basis: a need, a gap, a test, a discrepancy in the product's facts) and what it takes. A fix in the facts that buyers see today (a size chart that disagrees with itself, a claim without proof) goes first under "now".
- **The shot list:** every "to shoot" frame grouped by setup (who, where, light, backdrop), so one session covers them, and joined to the brand's first shoot list where the same setup appears.

## Tests

Each test is run by an agent that did not write the work. AI simulations are labeled as such on the page. Agents can't list a folder: give them file paths. An agent that reads images for a blind test never gets a file that holds the answers (`key.json`, the facts, the panel's correct answers).

| Test | Agent | Where | Question |
|---|---|---|---|
| Audience panel | `product-visual:audience-panel` | new | Shown the direction boards blind, two ranks kept apart: which stops you (the pull of the pictures), which answers your worry? And what puts you off? |
| Skeptical buyer | `product-visual:skeptical-buyer` | new, gallery, audit, qa | Three reasons not to buy, from real objections; which frame (or, on a positioning, which message) should have answered each |
| Rival test | `product-visual:rival-director` | new, gallery, audit, qa | Could the strongest competing product wear this direction, hero frame or image tomorrow? |
| Claim to proof | (the command) | new, gallery, audit, qa | Every visible claim, including those made by icons and scenes, against the facts |
| Blind shelf | `product-visual:fresh-eyes` | audit, qa | The main image among competing mains for the buyer's search, logos masked, at thumbnail size: what is it, who for, which would you open? (`scripts/shelf.py`) |
| AI reading | `product-visual:fresh-eyes`, `product-visual:ai-shopper` | audit, qa, ai-read | Mode A: what AI reads from the images, then images and text, scored against the facts. Mode B: the open web. Never mixed. |
| Judge | `product-visual:gate-judge` | new, gallery, audit, qa | Gate PV on the output files alone |

## Gate PV

| Check | Question | Type |
|---|---|---|
| PV.1 Needs-grounded | Does every UVP option, story and frame cite a ranked need with its source? | Blocking |
| PV.2 True to the facts | Does every message and visible claim check against a sourced fact? Is anything without proof kept off the images? | Blocking |
| PV.3 Located | Do positioning and direction say how they differ from named competing products, with images? (In an audit without positioning or direction: does the audit say how the gallery differs from the competing galleries?) | Blocking |
| PV.4 On brand | Does the direction follow `visual-guide.md`, and say why where it departs? | Blocking, or flag when there is no brand look |
| PV.5 Not a rival's | Did the rival test run on the direction and the hero frame, with the result recorded? | Blocking |
| PV.6 Honest count | Does every frame serve a need, within the channel's dated limit taken from the channel's own page or the owner? | Blocking |
| PV.7 Product fidelity | Do the images (audit, qa) show the real product: variant, color, construction, scale? | Blocking |
| PV.8 Observations, not orders | Are judgments observations or options with their basis, and discrepancies stated with both sources? | Blocking |
| PV.9 Read correctly | Is the main image read correctly on the blind shelf, and do AI readers get the facts a buyer needs to choose? (audit: observation; qa: blocking) | Blocking at qa |
| PV.10 Own work judged equally | Is the brand's own material held to the same standard as competitors'? | Flag |
| PV.11 Standalone briefs | Could a designer start from each brief alone? | Flag |
| PV.12 Readable | Short version first, no internal codes, sources at the end, overlay text legible at mobile size? | Flag |
| PV.13 Chosen look | Do the frames follow the chosen direction: its look, its cast, its caption rule and the proof frames handed over, or say why one departs? | Blocking when a direction is chosen, else flag |
| PV.14 Clean carriers | Do the mockups hold only the product's own clean photos, with "To shoot" tiles where photos are missing, and never another brand's images in the brand's own columns? Is every line on them the brand's own or a sourced fact? | Blocking |
| PV.15 Views covered | Is every view the ranked needs ask for covered by a frame, or moved to the listing text with the reason? | Blocking |

## Writing the pages

- The product page is a product book, in the same visual system as the Visual Brain direction book: one idea per screen, images large, one to three lines of text. Template: `frameworks/product-book-template.html` (new, gallery). Audit and QA pages use `frameworks/review-template.html`.
- **Language.** Pages are written in the language the owner writes in; the `.md` files stay in the language of the brand's customer copy. Customer quotes stay verbatim, with a short translation under them when the page language differs. Text inside mockups stays in the customer's language. `/product-visual:page <product> <lang>` builds the product page in another language (for example English for colleagues) from the same files.
- **Order of the product page:** cover, who it is for, competitors, positioning, the direction options, carriers, the storyboard, tests and choice, what to do next, sources.
- **Carriers.** The product page shows the product where the buyer meets it on the main channel, by its kind (Channels): a marketplace search card next to three competitors and the gallery; the own site's product page first screen and gallery strip; a search result among three competitors; a social carousel in a phone. Columns: as everyone, now (when live) and each option. Mockup text is only the product's real title, price and facts, or a line the brand already uses, marked temporary. Never an invented claim, rating or review count.
- **Clean carriers.** The brand's own columns take the product's own images only, never another brand's. The first image (search card, site hero, carousel cover) is a clean photo without badges or text over the product; the rest of a gallery mockup shows the planned frames as planned (a size card is a size card). Where a photo is missing, a color tile from the direction's palette says "To shoot:" and what exactly, in the page language. Competitors appear only in the "as everyone" column and as competitor cards.
- **The storyboard on the page:** one card per frame in order, with the image in hand (or the "To shoot" tile), and the fields Job, Need with its quote, In frame and View, Who, Text, Look, Proof, Route, and a "copyable" mark when the rival could make it. The views check sits under the cards as a short table: view, the frame that covers it, or "in the listing text" with the reason.
- **What to do next:** now, next, later with each action's basis, then the shot list grouped by setup.
- **Images** go in as `src="file:<path>"` in a `.src.html` source; `scripts/embed.py` builds the page and stores each image once (the audit and QA pages use `scripts/fill.py`). Image data is never pasted or printed in the chat. Options are shown as their separate images, not as composite boards.
- **Plain words.** No frame IDs, gate codes or tags on the pages; the `.md` files keep them. Images get plain captions.
- **Observations and options, not orders.** "What it does for the buyer", "what it misses", "worth considering", "options". Discrepancies (facts that contradict each other) are stated as facts, with both sources. The owner decides. QA is the exception: there the images are checked against briefs the owner approved, so each image is "ready", "needs work" (what exactly) or "redo" (why).
- **Basis next to every claim,** in a small gray line.
- **Short version first:** three sentences.

## Talking to the owner

- **Before:** one summary of what was found, what is missing, the few questions only the owner can answer, then "say go".
- **During:** one line per step. No running commentary.
- **When you need the owner:** end the message with **"Waiting for you:"** and the exact question.
- **After:** at most five lines and the page link.

## Stage

| Stage | Means |
|---|---|
| **hypothesis** | Essential facts missing, or the tests not run |
| **planned** | Tests run, no blocking fail; positioning and direction not chosen yet |
| **chosen** | The owner chose positioning and direction; dated in Decisions |
| **checked** | QA passed on the finished images (`/product-visual:qa` sets it) |
| **validated** | Dated results support it (`review`) |

## Limits

- Tests are AI simulations: they show what reads clearly, what is distinct and what is true, not what sells. Only dated results show what sold, and a before and after never proves cause.
- The plugin does not publish, upload, contact anyone, or spend on generation without the owner's yes.
- Competitor images are evidence, never material to copy.
