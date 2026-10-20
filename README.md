# Visual Brain plugins

The visual layer on top of the CXL Marketing Brain. The Marketing Brain says who the brand is for and what it says; these two plugins say how it should look, next to everyone else on the shelf.

Built for brands of physical products whose buyers choose by looking: marketplaces, the brand's own site and social media. Software and services are not covered.

**Beta.** Tested on one brand so far. Feedback and runs on other brands are welcome.

| Plugin | What it gives you |
|---|---|
| **Visual Brain** | The brand's visual direction. It studies the audience and the visual market (shelf competitors, references, and the brands AI assistants recommend if you have that list), proposes two or three directions, and shows each one on a social media grid and a site first screen next to how everyone looks. A simulated audience panel, shown the directions blind, and a simulated rival creative director test them. It checks one backdrop per color of your range at marketplace-tile size, and after you choose, it writes the visual language and a shoot list built from the photos you already have. |
| **Product Visual** | A product's images, planned frame by frame. Who the product is for and what they need to see, its positioning and UVP, a direction in the brand's chosen look, then a storyboard with a brief per frame for a marketplace, your site, search, or social. Also audits a live gallery and checks finished images before upload. |

The brand run, the product run and the audit and QA checks each end with one page in your language (`/visual-brain:page en` makes an English one), plus Markdown files Claude reads before any visual work.

## Before you start

- The Marketing Brain's ICP and positioning drafted (exercises 1 and 2).
- A folder with your product photos helps most. Nothing is required: missing inputs are marked, not blocking.
- Time: a standard run looks at about 10 brands, roughly half an hour to forty minutes. `/visual-brain:brand quick` is shorter, `/visual-brain:brand full` goes wider (15 to 20 brands, about an hour).
- Built and tested on macOS; Linux works without the HEIC step. The image scripts need Python 3; setup installs the image library they use. HEIC photos are converted with the macOS `sips` tool; elsewhere, export them as JPEG first. The blind-test agents use a Claude Code field that needs version 2.1.271 or later; older versions ignore it.

## Install

In Claude: **Customize → Plugins → Add → Add marketplace → Add from a repository**, enter `natabizz/visual-brain-plugins`, then install Visual Brain and Product Visual.

In Claude Code:

```
/plugin marketplace add natabizz/visual-brain-plugins
/plugin install visual-brain@visual-brain-plugins
/plugin install product-visual@visual-brain-plugins
```

Or download the zips from `dist/` and use **Customize → Plugins → Add → Upload plugin**.

Then open a new chat in your Marketing Brain folder (commands load when a chat starts):

| Command | Does |
|---|---|
| `/visual-brain:setup` | Adds Visual Brain's files to your workspace, once. Never overwrites yours |
| `/visual-brain:brand [quick \| full]` | The whole brand run: market, directions, tests, the page |
| `/visual-brain:choose <your choice>` | Records your choice and rebuilds the guide and page for it |
| `/visual-brain:page [language] [public]` | The page again, in another language; `public` leaves out other brands' images and your open issues |
| `/product-visual:setup` | Adds Product Visual's files to your workspace, once |
| `/product-visual:new <product> [channel]` | A product from scratch, up to the storyboard and briefs |
| `/product-visual:gallery <product> <channel>` | The storyboard for another channel |
| `/product-visual:page <product> [language]` | A product's page again, in another language |
| `/product-visual:audit`, `qa`, `ai-read`, `review` | A live gallery, finished images, how AI reads a listing, dated results |

## Privacy

Your images stay on your computer: `raw/visuals/` and the built pages, which carry the images inside them, are git-ignored; the Markdown files and the pages' `.src.html` sources are tracked. Customer quotes carry no names or emails. Pages show other brands' images for internal review only. Before sharing a Visual Brain page outside your team, rebuild it with `public`; Product Visual pages show competitor cards and are for internal review.

## Author

Natalia Bizyukova. MIT License.
