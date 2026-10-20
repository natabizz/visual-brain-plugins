# Visual Brain plugins

The visual layer on top of the [CXL Marketing Brain](https://github.com/conversionxl/cxl-marketing-brain). The Marketing Brain says who the brand is for and what it says; these two plugins say how it should look, next to everyone else on the shelf.

**Beta.** Tested on one brand so far. Feedback and runs on other brands are welcome.

| Plugin | What it gives you |
|---|---|
| **Visual Brain** | The brand's visual direction. It studies the audience and the visual market (shelf competitors, references, brands AI assistants name), proposes two or three directions, and shows each one on a social media grid and a site first screen next to how everyone looks. A blind audience panel and a rival test check them. After you choose, it writes the visual language, checks one backdrop per color of your range at marketplace-tile size, and builds a shoot list from the photos you already have. |
| **Product Visual** | A product's images, planned frame by frame. Who the product is for and what they need to see, its positioning and UVP, a direction in the brand's chosen look, then a storyboard with a brief per frame for a marketplace, your site, search, or social. Also audits a live gallery and checks finished images before upload. |

Each run ends with one page in your language (`/visual-brain:page en` makes an English one) and Markdown files Claude reads before any visual work.

## Before you start

- The Marketing Brain's ICP and positioning drafted (exercises 1 and 2).
- A folder with your product photos helps most. Nothing is required: missing inputs are marked, not blocking.
- Time: a standard run looks at about 10 brands, roughly half an hour to forty minutes. `/visual-brain:brand quick` is shorter, `/visual-brain:brand full` goes wider (15 to 20 brands, about an hour).

## Install

In Claude: **Settings → Plugins → Add → Add marketplace**, choose GitHub, enter `natabizz/visual-brain-plugins`, then add both plugins.

Or download the zips from `dist/` and use **Customize → Plugins → Add → Upload plugin**.

Then open a new chat in your Marketing Brain folder:

| Command | Does |
|---|---|
| `/visual-brain:brand` | The whole brand run: market, directions, tests, the page |
| `/visual-brain:choose <your choice>` | Records your choice and rebuilds the guide and page for it |
| `/visual-brain:page [language] [public]` | The page again, in another language; `public` leaves out other brands' images and your open issues |
| `/product-visual:new <product> [channel]` | A product from scratch, up to the storyboard and briefs |
| `/product-visual:gallery <product> <channel>` | The storyboard for another channel |
| `/product-visual:audit`, `qa`, `ai-read`, `review` | A live gallery, finished images, how AI reads a listing, dated results |

## Privacy

Your images stay on your computer (`raw/visuals/` is git-ignored). Customer quotes carry no names or emails. Pages show other brands' images for internal review only; use `public` before sharing a page outside your team.

## Author

Natalia Bizyukova. MIT License.
