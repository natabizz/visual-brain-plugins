# Product Visual

A product's visual, built from what its audience needs to see. Companion to **Visual Brain** (the brand's look) and the **Marketing Brain** (the buyer and the brand's position), from the CXL AI Native Marketer workshop.

Most gallery tools start from frames: "a main image, a size chart, a lifestyle shot". Product Visual starts from people: who this product is for, what they need to see before they buy, what the product can truthfully show, and how competitors already show it. From that it sets the product's positioning and UVP, a visual direction (what to show and how), and only then a storyboard: every image of the product, frame by frame (its job, what is in it and from where, the text, the look, the proof, the photo in hand or what to shoot), with a brief for each.

It works wherever the product lives: a marketplace, the brand's own site, search results, social posts and ads, wholesale (a Faire listing, a line sheet, a catalog page, a trade show), or a place you name. The storyboard's logic stays the same; the channel sets the count, the rules and how the page shows it.

**Physical products only.** Product Visual is for physical products, sold to consumers (B2C), to retailers (B2B), or both. Services and software are not supported: when the brand's `business_type` or the product says service or software, the commands stop and say so.

## Commands

| Command | What it does |
|---|---|
| `/product-visual:new <product>` | From scratch: who it's for and their ranked needs, what competitors say and show, two or three positioning and UVP options, two or three visual directions shown as collages, the product where the buyer meets it next to competitors, the storyboard with a brief per frame, and what to do next with the shot list. One page in your language, in the same style as the Visual Brain page. |
| `/product-visual:gallery <product> <channel>` | The storyboard for another channel, or again after you choose another option or the brand's direction changes. |
| `/product-visual:audit <product> <channel>` | A live gallery through the buyer's eyes: what each image does, what it misses, how it reads in search and to AI. |
| `/product-visual:qa <product> <channel>` | Finished images against the briefs and the facts, before upload; a release list. |
| `/product-visual:ai-read <product> <channel>` | How AI reads the listing, from the images, with the text, and on the open web. |
| `/product-visual:review <product> <channel>` | After publication: dated results, honestly read, and one next action. |
| `/product-visual:page <product> [language]` | The product page again, in another language (for example `en` for colleagues), from the same files. |

## How it works

- **Find first, ask last.** It reads your brand files and product files, finds competing products and reviews by itself, and asks once for what only you can give: the label, the size chart, real photos. Attach them in the chat. A moodboard is welcome and never required.
- **Competitors per channel.** Each channel gets its own competitor set, found on that channel the way a buyer searches there, with its date. An Etsy gallery is compared with Etsy listings, never with Amazon's.
- **For retailers too.** With `business_type: b2b` (or `b2b2c`) in your ICP, the product's facts get a Trade block (wholesale price, MSRP, MOQ, case pack, lead time, GTIN or UPC, certifications), a Wholesale channel plans a line sheet (hero, all variants, specs and pack, price and MOQ), and the panel and the skeptic play a retail buyer: would I open the catalog, request samples, place an opening order.
- **Needs first.** Every UVP, story and frame cites a ranked need of the audience, with a quote and its source. A views check makes sure every view buyers ask to see (the back, the fastening, two sizes side by side) has a frame, or says why it went to the listing text.
- **The brand's chosen look.** When Visual Brain has run and you chose a direction (`/visual-brain:choose`), every frame follows it: its look, its cast and lead, its caption rule, and the proof frames it handed over. Mockups show only your own photos, with colored "To shoot" tiles where photos are missing.
- **True to the product.** Facts have sources; a claim without proof stays off the images. Fit, size, material and construction are never shown with a generated image, and the product itself is never redrawn.
- **Options, not orders.** Positioning and direction come as two or three options with their basis, and at least one direction tells a different story rather than rearranging the proof; one is recommended by five questions (clear at a glance, advantage visible, believable on the images, recognizable on a second meeting, producible again and again), weighted by your channel; you choose.
- **Not a repeat of yourselves.** It reads your own galleries for your other lines and products. A format you already use comes back changed, or stays with a reason, and the storyboard names at least three frames that neither a competitor's gallery nor your own shows. With two lines of the same kind, one frame tells them apart, and positioning says for whom each is.
- **Status on everything.** Every fact, claim and test result is marked confirmed, assumption, your decision or simulation, and in the files carries its evidence label ([И] source, [Д] own data, [Ц] buyer quote, [В] inference, [Г] hypothesis with its check, [Р] your decision with date, reason and rejected options, [Н] not known yet with how to get it). Every frame carries its readiness (concept, needs confirmation and what, ready to shoot, ready for production), and the page's first screen is the decision: what to say and show, what it stands on, what is not known yet, the next three actions.
- **Checked by agents that didn't write it.** An audience panel reacts to the direction boards shown blind, on your own images only (what stops them, and what answers their worry, ranked apart), a skeptical buyer attacks the plan with real objections, the strongest competitor's creative director says what it could wear, a blind shelf shows how the main image reads in search, and AI reading shows which facts the images carry. All AI simulations, and the pages say so: no stage of the plugin counts as tested on buyers.

## Install

In Claude (desktop or claude.ai): **Customize → Plugins → Add → Add marketplace → Add from a repository**, enter `natabizz/visual-brain-plugins`; or **Customize → Plugins → Add → Upload plugin** with the zip from `dist/`. In a Claude Code session:
```
/plugin marketplace add natabizz/visual-brain-plugins
/plugin install product-visual@visual-brain-plugins
```
Then, in your Marketing Brain workspace: `/product-visual:setup`, then `/product-visual:new <product>`.

Needs: the Marketing Brain's `icp.md` and `positioning-messaging.md` drafted. Recommended: Visual Brain's brand look first (`/visual-brain:brand`, then `/visual-brain:choose`).

After installing or updating, open a new chat: commands load when a chat starts.

## Privacy

Image files stay on your computer: `raw/visuals/` and the built pages, which carry the images inside them, are git-ignored. Review quotes are kept without names, emails or order numbers. Other brands' images are shown on the pages for internal review only.

## Author

Natalia Bizyukova
