# Aidan Peat portfolio (working copy)

A private working copy of [aidanpeat.com](https://aidanpeat.com/), Aidan Peat's portfolio. Tom and Aidan are using it as the starting point for a redesign they're doing together. It is a snapshot of the live site as of 11 October 2026, not the live site itself.

## Preview it

From this folder, run either of these and open http://localhost:8000:

```sh
python3 serve.py          # no install needed
npx serve -l 8000 .       # if you prefer Node
```

Use one of those rather than opening `index.html` directly. The site's script routes on the URL path (`/about`, `/cv` ...), so it needs a server that maps `/about` to `about.html`.

It is also published with GitHub Pages at https://ummmthomas.github.io/aidan-peat-portfolio/ (from `main`). Pages carry a `noindex` tag so this copy stays out of search results.

## What's in here

| Path | What it is |
| --- | --- |
| `*.html` in the root | One file per page, **generated** by `tools/build.py`. Don't edit them by hand. |
| `site-src/` | The editable source: page bodies, stylesheet, page titles and share text. See "Editing content" below. |
| `tools/` | `build.py` regenerates the HTML from `site-src/`; `report.py` regenerates the media map and placeholder checklist. |
| `docs/rebuild/` | The value-led rebuild: audit and research, templates, media map, placeholder checklist, positioning directions. |
| `assets/cargo/` | The Cargo front-end bundle (`index.js`, `index.css`) that renders the pages. |
| `assets/freight/i/<hash>/<name>` | Every image the site uses, at up to 2000px wide. |
| `assets/type/`, `assets/static/` | The Diatype font and a background texture. |
| `serve.py` | Tiny preview server. |

The live site is built on [Cargo](https://cargo.site). Everything loads from this repo except embedded videos and players (Vimeo, YouTube, SoundCloud), which still stream from those services.

## Editing content

Cargo puts the whole site's content (every page body, the stylesheet, the image lists) into one JSON blob and repeats it in every `.html` file. So edit the sources in `site-src/`, then rebuild:

```sh
python3 tools/build.py          # regenerate every .html file
python3 tools/build.py --check  # just check they're up to date
```

| Source | What it holds |
| --- | --- |
| `site-src/pages/<page>.html` | A page's body, in Cargo's HTML (`<media-item hash="...">` places an image, `<gallery-columnized>` makes a grid). |
| `site-src/site.css` | The site stylesheet. |
| `site-src/state.json` | Cargo's page list and settings. `"@site-src/..."` strings point at the files above. A new page can be a few lines: `{"id", "title", "purl", "@template": "<an existing page id>"}`. |
| `site-src/routes.json` | One entry per `.html` file: its `<title>`, description and share image. |
| `site-src/shell.html` | The HTML wrapper every page shares. |

To place an image, use its hash folder name from `assets/freight/i/`. The build adds it to the page's media list.

After filling a `[[FACT/METRIC/QUOTE: ...]]` placeholder or moving media, run `python3 tools/report.py` to refresh `docs/rebuild/03-media-map.md` and `04-placeholders.md`.

## Changes from the live site

Only what was needed to run it from a local folder:

- Asset URLs on Cargo's servers point at `assets/` instead.
- `assets/cargo/index.js` loads images from `assets/freight/` at one fixed size, instead of requesting a resized copy from Cargo's image server for each screen width.
- `"domain_active"` is set to `false` in each page's data, so the script doesn't redirect you to aidanpeat.com.
- A small inline script in each page sets `window.__SITE_BASENAME__` when the site is served from a sub-path (like GitHub Pages), and `assets/cargo/index.js` passes it to the router so page URLs still resolve.
- Each page has `<meta name="robots" content="noindex, nofollow">`.
