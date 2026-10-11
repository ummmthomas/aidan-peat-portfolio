# Case study templates

Step 3 of the value-led rebuild. Each template is built from the research in [01-audit-and-research.md](01-audit-and-research.md), section 5, and from the media that actually exists. Every page lives in `site-src/pages/` and opens as the site's existing half-width overlay. The overlay header ("Title … (Close)") and footer ("(Return to projects) … years") are kept as they were.

## Shared building blocks

All of them are plain HTML classes styled in `site-src/site.css`. They use the site's own type scale: Diatype, the `.caption` size for labels, 40% black for secondary text, and the existing hairline for rules.

| Block | Markup | What it does |
| --- | --- | --- |
| Kicker | `<div class="cs-kicker">Series · type</div>` | A grey line above the headline. On Colbert pages it links back to the series hub. |
| Value headline | `<h2 class="cs-headline">` | States the outcome, not the deliverable. |
| Standfirst | `<div class="cs-standfirst">` | One or two sentences that frame the work. |
| At-a-glance strip | `<dl class="cs-glance"><div><dt>Label</dt><dd>Value</dd></div>…</dl>` | Partner/client, year, my role, deliverables, reach. It wraps to as many columns as fit. |
| Section | `<div class="cs-section"><div class="cs-label">Label</div><p>…</p></div>` | A grey label over a short block of prose. |
| Two brands | `<div class="cs-pair"><div><h3>…</h3><p>…</p></div>…</div>` | Two columns, which stack on mobile. |
| **Impact stats** | `<div class="impact"><div class="cs-label">Impact</div><div class="impact-stat" data-value="12" data-label="markets"></div>…</div>` | The figure is written once, in `data-value`, and CSS draws it. **A stat whose value still starts with `[[` is hidden, and a strip with no real stats hides entirely**, label included. To publish a number, replace the placeholder in `data-value`. |
| Quote | `<blockquote class="cs-quote" data-quote="…" data-cite="…">` | Hidden until both the quote and its source are real. |
| Credits | `<dl class="cs-credits">` | Who did what. |
| Placeholder | `<span class="ph">[[FACT: …]]</span>` | Highlighted yellow so gaps are obvious in preview. Search the sources for `[[` to find them all. |

## A. Brand collaborations: full case study
Johnnie Walker, adidas and ASUS (`colbert-*.html`), under the series hub `pc-project.html`.

| Section | Content | Media used |
| --- | --- | --- |
| Value headline + standfirst | The outcome in one line, then "brand X brought…, Colbert brought…" | |
| At-a-glance | Partners · launched · my role · the product/set · reach | |
| Hero | The main product shot | JW: Blue Label `O3169203921`; adidas: Superstar `D3171045436`; ASUS: bundle `Y3171041900` |
| The two brands | One column per brand: what it stands for and who it's for. The audience is a `[[FACT]]` where the site doesn't say. | |
| The brand bridge | What each side kept and what changed, described from what's visible in the photos, then Aidan's own account as a `[[FACT]]` | |
| Process | A `[[FACT]]` only: there are no sketches or iterations in the media | |
| The work | The remaining shots, captioned | JW: XR21 set `J3169206855`; adidas: hoodie `S3169206095` (pending a `[[FACT]]` on whether it belongs here) |
| Impact | Markets, sell-through, launch-post engagement, press. Hidden until filled. | |
| Quote, credits, next | Testimonial (hidden), credits with role and photographer, link to the next collab | |

**The series hub** (`pc-project.html`) opens with the Colbert wordmark and a value headline for the whole partnership. It links to the four case studies, then groups the other 14 Colbert assets by what they show: exhibition campaigns (Rome, Naples, Taipei, Journey to the Lobster Planet, Pearl Lam, Macao), brands and collectables (Bentley, AS Roma, Pompeii Lobster, Lobster Pop History), books and covers (two books, Vogue Singapore, The Big Issue), and the showreel. The original bio and the gallery/collaboration lists stay at the foot, word for word, with adidas and ASUS added to the list.

## B. Exhibition: Shenzhen
`colbert-shenzhen.html`. **Scaled down from the brief:** there is one photo, so the page can't show wayfinding, print or interiors.

Value headline → at-a-glance (venue, dates, organisers, my role, scale, all from the organiser's press release except the role) → façade photo `R3171027368` → the graphic system as visible on the façade, plus a `[[FACT]]` for the rest → a link to the exhibition campaigns on the hub → impact (attendance, press, hidden until filled) → credits.

## C. Identity: NEW LANGUAGE
`new-language.html`, mid-length. The studio and its positioning problem (`[[FACT]]`) → at-a-glance → the identity system (`[[FACT]]`) → in use: the sweatshirt photo `B3169185396` and a link to the studio's Instagram → outcome stats (followers, bookings, press, hidden until filled).

## D. Music videos: Moorland, Duke Keats
`moorland-praise.html`, `duke-keats-monkey-brains.html`, mid-length. The artist's world (`[[FACT]]`) → at-a-glance → the full Vimeo embed with controls, plus a "Watch on YouTube" link → concept (`[[FACT]]`) → reach (views, press, hidden until filled) → credits. A stills strip would follow the embed, but no stills exist in the repo. Frame grabs from the videos would be existing media and could be added later.

## E. Print, merch and culture: short format
`psychic-attack.html`, `grey-area-taipei.html`, `hefty-bruises-002.html`, `radio.html`. Kicker → one-line value headline → the piece(s) → a link out where one exists → one impact strip. Psychic Attack keeps every original slideshow and its full text and specs. It now opens with both covers and the one real stat on the site: **2 of 2 editions sold out**.

## F. Personal Graphic Exploration: short format
`graphics.html`. Framed as "The lab behind the client work". The original 12 pieces and statement are unchanged, with the index triptych `A3172363619` added as a header. A new "Where it shows up" section links the visual habits to Psychic Attack, Grey Area, Hefty Bruises and the radio artwork.
