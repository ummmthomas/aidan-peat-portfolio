# Aidan Peat portfolio rebuild: audit and case-study research

Steps 1 and 2 of the value-led rebuild, written before any site edits.
Source: `ummmthomas/aidan-peat-portfolio` at `main` (07a668b), 11 October 2026.

---

## 0. Headlines (read this first)

1. **Aidan's actual role on the Colbert work is never stated.** The only first-person line is: *"During my time with Colbert, I've had the pleasure of working on a wide range of projects; high-end collectable artworks, documentaries, global exhibition advertisements, paintings, books, and football stadium animations."* The site doesn't say he designed the Johnnie Walker, Adidas or ASUS products. Every "brand bridge" section depends on a `[[FACT]]` answer from Aidan. Until then we can't write "Aidan merged the two visual languages" without risking an overclaim.
2. **The four Colbert tiles all open the same page.** Shenzhen, Johnnie Walker, Adidas and ASUS each link to `/pc-project`. That page is one grid of 21 images covering the three collabs plus about a dozen other Colbert projects (Bentley, AS Roma, Vogue Singapore, The Big Issue, books, Rome/Naples/Taipei/Macao exhibitions), followed by a showreel. This content already suggests a "Philip Colbert 2022–2026" series hub.
3. **Shenzhen has one photo.** It's a façade shot of the exhibition banners. Template B (identity, wayfinding, signage, in-situ) can't be filled from what exists. My suggestion is to make it a mid-length study inside the Colbert hub unless Aidan has more photos.
4. **Five of the twelve projects have no page on the site.** NEW LANGUAGE, both music videos, Grey Area and Hefty Bruises link straight off-site to Instagram, YouTube or Bandcamp. Each has exactly one asset: a single image, or for the music videos a muted Vimeo loop.
5. **Moorland may be Aidan himself.** The Radio page embeds a SoundCloud playlist titled "Radio sets" from `soundcloud.com/mooorland` (display name "Moorland"), and the radio blurb says the mixes are Aidan's. If Moorland is Aidan's music alias, the "Praise" video is his own release, which changes how that case study reads. → `[[FACT: is Moorland Aidan's alias / own project?]]`
6. **Housekeeping found in the audit:**
   - The CV page is still Cargo's lorem-ipsum template ("Vestibulum Euismod…", years 2030–2034). It's live and linkable.
   - Five pages (Homepage, PC Project, Radio, Graphics, Psychic Attack) use Cargo's template placeholder photo `horizontal.jpg` as their `og:image`. It's a photo of a child resting their head on a table and isn't Aidan's work.
   - No image anywhere has alt text. No page has a meta description. Every page's `<title>` is just "Aidan Peat".

---

## 1. How the site is built and where content lives

| Thing | Where | Notes |
| --- | --- | --- |
| Stack | Cargo 3 export, static | One HTML shell per route; Cargo's bundle `assets/cargo/index.js` renders everything client-side. |
| All content | `window.__PRELOADED_STATE__` JSON inside each HTML file (≈77 KB) | **Byte-identical in all 8 HTML files.** Any content edit has to be applied to all 8, or we factor the state out into one file. |
| Page bodies | `pages.byId[<id>].content`: Cargo's HTML dialect (`<gallery-columnized>`, `<media-item hash=…>`, `<column-set>`) | Pages: Top Nav, Homepage, PC Project, Radio, Graphics, Psychic Attack, About, CV, Copyright Footer, Footer (Desktop). |
| Page media libraries | `pages.byId[<id>].media[]` | Gives each asset's original size and name. A library can hold assets the page doesn't show (e.g. About). |
| Per-page meta | `<head>` of each HTML file (`og:title`, `og:url`, `og:image`, `twitter:*`) | `og:title` is "Aidan Peat" everywhere. |
| Site meta | `site.site_description` | "Graphic designer and visual artist. \nLondon, UK." |
| Images | `assets/freight/i/<hash>/<filename>` | 60 files, of which 54 are unique (6 byte-identical pairs, listed below). Stored at ≤2000 px. |
| Video / audio | External embeds only | 3 Vimeo (2 music videos, 1 Colbert showreel), 2 YouTube link targets, 1 SoundCloud playlist. Not in the repo. |
| Fonts / textures | `assets/type/` (Diatype Plus Variable + Italic), `assets/static/` (noise.png, select arrows) | Part of the visual identity. Not portfolio media. |

**Routes:** `/` (homepage grid), `/pc-project`, `/psychic-attack`, `/graphics`, `/radio`, `/about`, `/cv`, `/contact-form`. Project pages are Cargo overlays with a "(Close)" button and a "(Return to projects)" link.

---

## 2. Existing text (verbatim source material)

### Site-wide
- **Nav:** "Aidan Peat" (the word "Aidan" links home) · "About" · "Instagram" → `https://www.instagram.com/aidanspeat/` · "Email" → `/contact-form`
- **Site description:** "Graphic designer and visual artist. London, UK."
- **Footers:** "Aidan Peat © {year}" · a live clock "{day}, {month-name} {day-of-month}, {year} {hour}:{minute} {period}"
- **Favicon:** blue star in a circle (`star-2_circle.ico`)

### About (`/about`)
> Based in London
>
> A designer with a strong interest in the arts, contemporary culture, and navigating creative solutions through the power of design.
>
> Over 4 years of experience within a fast-paced artist's studio.

Column 2: "Hackney / London / UK", aidanspeat@gmail.com (links to the contact form), @aidanspeat (Instagram), and a phone number.

### Homepage captions (in the order shown)
| # | Caption (verbatim) | Link target |
| --- | --- | --- |
| 1 | Philip Colbert · 2022 - 2026 - Shenzhen Solo Exhibition | /pc-project |
| 2 | Philip Colbert · 2022 - 2026 - Johnnie Walker Collaboration | /pc-project |
| 3 | NEW LANGUAGE Contemporary Tattoo Studio · 2021 | instagram.com/newlanguage_ |
| 4 | Psychic Attack · 2021 + 2023 - 2 physical zines and  t-shirt | /psychic-attack |
| 5 | Philip Colbert · 2022 - 2026 - Adidas Collaboration | /pc-project |
| 6 | Moorland - Praise (Official Music Video) · 2025 | youtube.com/watch?v=TAcUi3VoPDA |
| 7 | Philip Colbert · 2022 - 2026 - ASUS Collaboration | /pc-project |
| 8 | Grey Area Taipei Nightclub · 2025 - Event flyer | instagram.com/greyarea_huisedidai |
| 9 | Duke Keats - Monkey Brains (Official Music Video) · 2025 | youtube.com/watch?v=Mhuew6FgQXA |
| 10 | Personal Graphic Exploration · 2019 - 2026 | /graphics |
| 11 | Hefty Bruises 002 · 2024 - Vinyl artwork | heftybruiseslabel.bandcamp.com/album/hefty-bruises-002 |
| 12 | Radio Residencies · 2021 - 2025 | /radio |

### PC Project (`/pc-project`): title "Philip Colbert", dates "2022 - 2026"
> Born in Scotland and living and working in London, Colbert is often referred to as the "godson of Andy Warhol". He has created a global following for his cartoon lobster persona and his masterful hyper-pop history paintings. His work powerfully explores the patterns of contemporary digital culture and its relationship to a deeper art historical dialogue.
>
> Colbert's work has received international acclaim in museums and galleries worldwide for his energetic new approach to painting and pop theory. Following on from early Pop painters such as Richard Hamilton, Roy Lichtenstein and James Rosenquist, Colbert's paintings cross high art themes from old master paintings and contemporary art theory with everyday symbols of mass contemporary culture, all narrated through the eyes of Colbert's cartoon Lobster alter ego. He has been championed as a contemporary pop master by art world figures such as Charles Saatchi & Simon de Pury.
>
> During my time with Colbert, I've had the pleasure of working on a wide range of projects; high-end collectable artworks, documentaries, global exhibition advertisements, paintings, books, and football stadium animations.

**Galleries include:** Saatchi Gallery, London · The Archaeological Site of Pompeii · Lightbox Gallery, Woking · The National Archaeological Museum of Naples · Whitestone Gallery, Taipei and Singapore · Pearl Lam Galleries, Shenzhen, Hong Kong and Tokyo · Karuizawa New Art Museum, Japan · The Page Gallery, Seoul

**Collaborations include:** Johnnie Walker · Casetify · AS Roma · Bentley · Vogue Singapore · Vogue Korea · Team GB · Conran shop · Borough Yards · The Big Issue

(Adidas and ASUS appear on the homepage but **not** in this list. Casetify, Vogue Korea, Team GB, Conran Shop and Borough Yards are in the list but have **no media**.)

### Psychic Attack (`/psychic-attack`): "2021 + 2023"
> Psychic Attack is a personal project of documentation and graphic research, birthed in 2021, as a result of the first COVID lockdown.
>
> The first edition documented years of personally archived magazines and newspapers on UFO sightings and extraterrestrial beings.
>
> Psychic Attack 2 followed themes of Satan, witchcraft, heaven, and God.
>
> For the second edition, I also locally screenprinted t-shirts with a friend, using graphics from the zine.

Specs column: "A5 size / 40 pages / Staple bound / Printed at home / Both editions sold out."

### Personal Graphic Exploration (`/graphics`): "2019 - 2026"
> I regularly invest time outside of work into experimenting with my personal artistic style - incoporating my passion for found-imagery and archival research.

(The typo "incoporating" is in the original.)

### Radio Residencies (`/radio`): "2021 - 2025"
> Monthly mixes for a number of online radio platforms, including London-based platforms Voices Radio and RTM Radio.

Embed: SoundCloud playlist "Radio" by **Moorland** (`soundcloud.com/mooorland/sets/radio-sets`).

### CV (`/cv`)
All of it is Cargo template lorem ipsum. Nothing on it is real.

---

## 3. Media inventory

Notation: `ID` is the first 10 characters of the Cargo hash folder. Full path is `assets/freight/i/<hash>/<filename>`. Dimensions are the Cargo originals, with the repo copy size in brackets where it differs. **Shown on** means where the live site currently displays the asset. All 60 files, 3 Vimeo videos and 1 SoundCloud embed are listed. Duplicates are marked ⧉.

Asset kinds: **product** (studio product shot) · **in-situ** (in the world) · **campaign** (styled advertising or lookbook) · **print** (printed object photographed) · **artwork** (flat digital artwork) · **cover** (magazine or book cover) · **video** · **portrait** · **site** (site furniture).

### A. Philip Colbert 2022–2026 (one page today, `/pc-project`)

| ID | File | Kind | Size | What it shows | Shown on | Likely sub-project |
| --- | --- | --- | --- | --- | --- | --- |
| O316920392 ⧉ V316917104 | Johnnie-Walker-Blue-Label--.jpg | product / campaign | 2000×1331 | Blue Label gift box covered in blue, with Mr. Lobster sitting on a full moon among clouds, next to the bottle, on a blue set. Box reads "Philip Colbert". | pc-project; homepage tile 2 (dup) | **Johnnie Walker** |
| J316920685 | Johnnie-Walker-XR--GWP.jpg | product / campaign | 2000×1333 | XR21 gift box (crowned lobster, gold/peach botanical pattern, "Philip Colbert Edition"), bottle, XR-branded glass on a gold lobster-shaped stand, warm set. "GWP" in the filename may mean gift-with-purchase (inferred). | pc-project | **Johnnie Walker** |
| D317104543 ⧉ D317106065 | imageQC28957483_2000_6.jpeg | product | 2000×1644 | adidas Superstar pair with lobster and "Save the Lobster" all-over print. | pc-project; homepage tile 5 (dup) | **Adidas** |
| S316920609 | 2309_ADV_46156.jpg | campaign / lookbook | 1333×2000 | Model in a grey hoodie with a Colbert lobster-and-sneaker chest graphic. No brand mark visible. | pc-project | Adidas? `[[FACT: which collab is the hoodie?]]` |
| Y317104190 ⧉ S317105900 | Vivobook-13-Slate-OLED-Philip-Colbert-Edition_scenario-photo_06.jpg | product / campaign | 2000×1333 | ASUS Vivobook 13 Slate OLED Philip Colbert Edition bundle: printed box, sleeve, tablet, lobster stylus-holder figure, shoelaces, sticker sheets, cable, on a red/blue/yellow set. | pc-project; homepage tile 7 (dup) | **ASUS** |
| R317102736 ⧉ R317105738 | JOY_5788-edit_2000.jpg | in-situ | 2000×1333 | Building façade with large banners: "PHILIP COLBERT – THE MYTH OF THE LOBSTER PLANET – 2023 SOLO EXHIBITION – 06.17–10.15", Chinese title 龙虾创世, vertical flag banners, "DESIGN ENABLES" signage at ground level. | pc-project; homepage tile 1 (dup) | **Shenzhen** |
| U317105448 | PC_Inflated_Logo_2024_Black.png | artwork (logo) | 3876×2237 (2000×1154) | Colbert's "inflated" bubble-letter wordmark, black on transparent. It renders as a black block on some viewers. | pc-project (first image) | Hub header |
| S316920469 | 4.jpg | in-situ | 2000×1333 | Bentley showroom corner with large Colbert lobster/character window graphics. | pc-project | Bentley (hub) |
| L316920484 | 6.jpg | in-situ | 2000×1333 | Bentley convertible wrapped in Colbert characters, in front of "PHILIP COLBERT – JOURNEY TO THE LOBSTER PLANET – TAIPEI" exhibition signage. | pc-project | Bentley / Taipei exhibition (hub) |
| N317104093 | Cover_Issue48_VogueSG_Jan_Digital_V1.jpg | cover | 1600×2000 | Vogue Singapore issue 48 (January) digital cover, "The Art Issue", Yerin Ha posed with Colbert lobster sculptures. | pc-project | Vogue Singapore (hub) |
| Y317104177 | IMG_8922.jpg | in-situ | 2000×1333 | Rome: open-top tour bus wrapped in "THE LOBSTER EMPIRE – PHILIP COLBERT – 06 OCT – 08 JAN 2022/2023" in front of Castel Sant'Angelo, with passers-by. | pc-project | Exhibition advertising (hub) |
| O317105016 | Pompeii-Lobster_Resin_33x25x19cm_2026_PC2422_1.jpg | product | 2000×1333 | "Pompeii Lobster" resin collectible beside its black box, which carries a line illustration of Pompeii. | pc-project | Collectibles (hub) |
| G317104847 | AS-ROMA-X-Philip-Colbert-…-2023-PC-1605-with-box-01_2000.jpg | product | 2000×1333 | AS Roma × Philip Colbert 15 cm vinyl lobster in the Roma kit, beside a red/gold box. | pc-project | AS Roma (hub) |
| R316920870 | The-Lobster-Pop-History-Mini-Red_…_2025_PC-2090_04.jpg | product | 2000×1333 | "Lobster Pop History Mini Red" vinyl figure (Hieronymus Bosch / Fernand Léger tee) beside a sticker-bombed box. | pc-project | Collectibles (hub) |
| Z316920380 | IR4_1758.jpg | in-situ | 2000×1331 | Naples National Archaeological Museum (MANN) entrance with banners "House of the Lobster – Philip Colbert". | pc-project | Exhibition graphics (hub) |
| Q316922017 | Room-1-2.jpg | in-situ | 2000×1334 | Gallery: chrome stacked-lobster sculpture next to a title wall "JOURNEY TO THE LOBSTER PLANET – PHILIP COLBERT – January 6 – March 5, 2024" with intro text. | pc-project | Exhibition graphics (hub) |
| X317102704 | 2-copy-2.jpg | in-situ | 2000×1332 | Pearl Lam Galleries installation view: title wall "PHILIP COLBERT – Solo Exhibition – DREAMS OF LOBSTEROPOLIS", painted walls, sculptures on plinths. | pc-project | Exhibition graphics (hub) |
| N317102832 | 250127_KTZ_5034.jpg | in-situ | 2000×1331 | Macao outdoors: Colbert rooster sculpture, "PHILIP COLBERT – MACAO" information sign, visitors. The filename suggests 27 Jan 2025. | pc-project | Public art / exhibition (hub) |
| K316920919 | Journey-to-the-Lobster-Planet-…-2023-MEPC-0077-3.jpg | product (book) | 2000×1333 | "Journey to the Lobster Planet" book: yellow back cover, spine, black front cover. Japanese/English, Karuizawa New Art Museum. | pc-project | Books (hub) |
| X316920903 | The-Lobster-Empire-32x25x30cm-2022-MEPC-0027-3.jpg | product (book) | 2000×1333 | "The Lobster Empire" book: back cover, spine, front cover. | pc-project | Books (hub) |
| Y317234748 | BI_Colbert_Cover-R3_Final.jpg | cover (artwork file) | 1413×2000 | The Big Issue no. 1704, 9–15 Feb 2026: "Exclusive cover by Philip Colbert", lobster in a "Lobster Love" jumper. | pc-project | The Big Issue (hub) |
| vimeo 1234098631 | "PC_Show Reel" | video | 1920×1080, duration unknown (Vimeo blocked from here) | Colbert showreel. Contents not yet viewed. | pc-project (bottom, full width) | Hub |

### B. NEW LANGUAGE Contemporary Tattoo Studio, 2021
| ID | File | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| B316918539 | IMG_1866_crop.jpg | in-situ / merch | 1576×2000 | Grey sweatshirt on a hanger with a framed NEW LANGUAGE wordmark print, against a wall of pinned tattoo flash and drawings. | homepage tile 3 (links to Instagram) |

### C. Psychic Attack, 2021 + 2023
| ID | File | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| H316917316 | BothZines.jpg | print | 2000×1332 | Both covers side by side: purple (PA2, dead tree) and green (PA1, car + UFO), with star stickers. | homepage tile 4 |
| M316973618 | Spread-0.jpg | print | 2000×1332 | PA2 purple cover. | psychic-attack (slideshow 1) |
| L316973601 | Spread-6.jpg | print | 2000×1332 | PA2 spread: blackletter text + framed demon face. | psychic-attack |
| K316973601 | Spread-3-copy.jpg | print | 2000×1332 | PA2 spread: engraved devil/beast illustration. | psychic-attack |
| U316973601 | Spread-2.jpg | print | 2000×1332 | PA2 spread: distressed cross + "Christ or Chaos" with hexagram diagrams. | psychic-attack |
| S316973601 | Spread-1.jpg | print | 2000×1332 | PA2 spread: "SIZZLING hot hips" + caricature sketch. | psychic-attack |
| L316974226 | psychicattack1.jpg | print | 2000×1333 | PA1 green cover. | psychic-attack (slideshow 2) |
| E316974237 | psych1_2.jpg | print | 3269×2179 | PA1 spread: "UFO Day Oct. 27" flyers + "The truth is over here…". | psychic-attack |
| D316974244 | psych1_1.jpg | print | 3269×2179 | PA1 spread: "Doris' Universal Healers" comic panels + UFO sketch text. | psychic-attack |
| G316974256 | psych1_3.jpg | print | 3269×2179 | PA1 spread: UFO / dinosaur collage + "Were the dinosaurs studied by visitors from deep space?". | psychic-attack |
| Y316975246 | PsychicTshirt.jpg | product (merch) | 2000×1332 | Black tee "THE MISSING LINK": chest detail and full flat-lay. | psychic-attack |

### D. Music videos, 2025
| ID | Asset | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| F316939057 | Vimeo 1233725741, "Moorland - Praise" | video (muted autoplay loop) | 1920×1080, duration unknown | Not viewable from here. | homepage tile 6 (links to YouTube TAcUi3VoPDA) |
| A316937699 | Vimeo 1233722388, "DUKE KEATS - MONKEY BRAINS" | video (muted autoplay loop) | 1920×1080, duration unknown | Not viewable from here. | homepage tile 9 (links to YouTube Mhuew6FgQXA) |

No stills exist in the repo for either video.

### E. Grey Area Taipei, 2025
| ID | File | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| M316921083 | Grey-Area-Ground-April-6-2.png | artwork (social flyer) | 1080×1350 (Instagram 4:5) | "Grey Area – GROUND – April 6th" in ornate outlined lettering, a cartoon character, faded grid and blue splashes. | homepage tile 8 (links to Instagram) |

### F. Hefty Bruises 002, 2024
| ID | File | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| U317091143 | a1011066380_10.jpg | artwork (sleeve) | 1200×1200 (Bandcamp art file) | Distressed purple/teal texture with ink spatters and a "HEFTY002 – SDS MAX + VERE" label. | homepage tile 11 (links to Bandcamp) |

### G. Radio Residencies, 2021–2025
| ID | File | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| J316942153 ⧉ U316916739 | RTM-RAWMATERIAL2-small.jpg | artwork (show tile) | 1200×1200 | Halftone portrait framed by a green-leaf and red-flower border on khaki. "RTM" suggests RTM Radio; "Raw Material 2" may be the show name (inferred from filename). | radio; homepage tile 12 (dup) |
| SoundCloud playlist 1672343835 | "Radio" by Moorland | audio embed | n/a | The mixes themselves. | radio |

### H. Personal Graphic Exploration, 2019–2026
| ID | File | Kind | Size | What it shows | Shown on |
| --- | --- | --- | --- | --- | --- |
| A317236361 | 3together2.jpg | artwork (composite) | 2822×1331 | Triptych of compute + Horn + im-hers. Made as the index cover. | homepage tile 10 |
| E317087694 | Horn.jpg | artwork (poster) | 1414×2000 | Silhouetted trumpeter in plants, spider web, chandelier, watercolour sky. | graphics |
| M317087694 | im-hers.jpg | artwork | 1600×2000 | Sticker collage: € sign, Amway, Denver '88, Rover, cartoon hands, black flower forms. | graphics |
| H317087694 | Sky.jpg | artwork | 2000×1414 | Collage: "Radio Luxemburg / Täglich Frisch" sticker, tiger, horseman, butterfly, cyan blots on a grid. | graphics |
| W317087694 | car1.jpg | artwork (poster) | 1414×2000 | Cartoon car, "European Broadcasting Union" text, skull row, butterflies, gradient. | graphics |
| G317087694 | signsoflife.jpg | artwork (poster) | 1414×2000 | "SIGNS OF LIFE", halftone teapot, window grid, leaf shapes. | graphics |
| K317087780 | sherleyholmes.jpg | artwork (poster) | 1131×1600 | Large "1718" numerals, "46 cm / 18.11"" measurement marks, colour scraps. | graphics |
| Y317087780 | Softworld.png | artwork (poster) | 1131×1600 | "Softworld" title, torn-edge frame, halftone figures, horsemen. | graphics |
| K317087780 | NASA.jpg | artwork (poster) | 1131×1600 | Orange field, gradient basketball silhouettes, blue splashes. | graphics |
| R317087780 | smashed.jpg | artwork (poster) | 1131×1600 | Cracked-glass motif over pastel camouflage, small stars. | graphics |
| F317087780 | compute.jpg | artwork (poster) | 1131×1600 | Retro computers, a woman at a terminal, bleached colour bands. | graphics |
| E317087780 | APPLE-EXPO-1.jpg | artwork (poster) | 1131×1600 | Crowd silhouettes over colour wash, city street collage. | graphics |
| M317087824 | drivingwheel4.jpg | artwork (print) | 2000×1414 | Single-colour brown on khaki: "Human" chimp box, star, creature, ducklings, "2010" box. Risograph/screenprint look. | graphics |

### I. Aidan, About and site furniture
| ID | File | Kind | Size | What it shows | Shown on | Proposal |
| --- | --- | --- | --- | --- | --- | --- |
| N317107376 | Me.png | portrait | 2000×1333 | Aidan on a pebble beach by a pier, framed in black. | about | Keep on About |
| R317107440 ⧉ N317107376 | Me.png | portrait | 2000×1333 | Duplicate of the above. | nowhere (About media library) | Unplaced: exact duplicate |
| B316939866 | 003325090029.jpg | portrait | 3089×2048 | Uncropped film scan of the same portrait. | nowhere visible; About page thumbnail and `og:image` | Use as About `og:image` / contact CTA image |
| R317255504 | screenshot-3557155483.jpg | site | 1792×1120 | Screenshot of the current homepage. | `og:image`/Twitter card for home, cv, contact | Unplaced: replace with a real work image as OG; keep as a "before" reference |
| V298299891 | horizontal.jpg | Cargo placeholder | 3000×2000 | Cargo template stock-style photo (child resting their head on a table). Flagged `is_placeholder` by Cargo. | `og:image` on 5 pages; page thumbnails | Unplaced: not Aidan's work |
| N317235263 | star-2_circle.ico | site | 192×192 | Blue star favicon. | favicon | Keep as favicon |

### Duplicates (byte-identical, keep both, place once)
`JOY_5788-edit_2000.jpg` (R317102736 / R317105738) · `Johnnie-Walker-Blue-Label--.jpg` (O316920392 / V316917104) · `Me.png` (N317107376 / R317107440) · `RTM-RAWMATERIAL2-small.jpg` (J316942153 / U316916739) · `Vivobook-13-Slate-OLED-Philip-Colbert-Edition_scenario-photo_06.jpg` (S317105900 / Y317104190) · `imageQC28957483_2000_6.jpeg` (D317104543 / D317106065)

**Totals:** 60 image files (54 unique) · 3 Vimeo videos · 1 SoundCloud embed · 2 YouTube and 3 other outbound link targets.

---

## 4. Gaps per project for a value-led case study

Format: **Have** = existing assets and facts. **Missing** = what the template needs that doesn't exist, as placeholders. Public facts I found are listed as *framing only, to verify with Aidan*.

### Philip Colbert hub (2022–2026)
- **Have:** the bio, gallery and collaboration lists, the "During my time with Colbert…" role line, 21 images, the showreel.
- **Missing:** `[[FACT: Aidan's job title at the Colbert studio and exact dates]]` · `[[FACT: which of the 21 images / projects Aidan personally designed vs. supported]]` · `[[FACT: what the "football stadium animations" and "documentaries" were]]` (no media for either) · `[[QUOTE: Philip Colbert or studio testimonial]]`

### Johnnie Walker × Colbert
- **Have:** 2 product shots (Blue Label, XR21 with glass + lobster stand).
- **Framing (public, to verify):** sales in Taiwan began 29 July 2024 as a limited Blue Label and XR21 gift-box series built around Mr. Lobster. Taiwanese press describes the Blue Label box with Mr. Lobster on a full moon and an RRP of NT$6,100 ([CTEE, 25 Jul 2024](https://www.ctee.com.tw/news/20240725701204-431207), [FoodNext](https://www.foodnext.net/life/recipes/dinner/paper/5739978556)). One source says "global" sale, so the market scope needs checking.
- **Missing:** `[[FACT: Aidan's exact role / what he designed]]` · `[[METRIC: markets / territories launched in]]` · `[[METRIC: units / sell-through]]` · `[[METRIC: press coverage]]` · process media (sketches, box dielines, iterations): none in repo.

### Adidas × Colbert
- **Have:** 1 Superstar product shot, plus possibly the hoodie lookbook shot.
- **Framing (public, to verify):** adidas Originals Superstar "Save The Lobster" (GX7996), lobster and fried-egg motifs with an environmental message ([GOAT](https://www.goat.com/en-sa/sneakers/philip-colbert-x-superstar-save-the-lobster-gx7996), [Marie Claire TW](https://www.marieclaire.com.tw/fashion/news/57087)). Release year is not stated in the results and must be confirmed. If it predates 2022, it falls outside Aidan's "2022–2026" span.
- **Missing:** `[[FACT: Aidan's role]]` · `[[FACT: release date]]` · `[[FACT: is the hoodie (2309_ADV_46156) part of this collab?]]` · `[[METRIC: sell-out / markets]]` · in-context media (retail, on-foot).

### ASUS × Colbert
- **Have:** 1 styled bundle shot.
- **Framing (public, to verify):** ASUS announced the Vivobook 13 Slate OLED Philip Colbert Edition on 10 May 2022, alongside a Steven Harrington edition. Colbert's artwork runs across the device, accessories and packaging, and the bundle includes a lobster figurine that holds the stylus, plus limited-edition shoelaces ([ASUS press](https://press.asus.com/news/press-releases/193), [LanOC](https://lanoc.org/news/hardware-news/asus-launches-vivobook-13-slate-oled-limited-artist-editions)).
- **Missing:** `[[FACT: Aidan's role (packaging? accessories? stickers?)]]` · `[[METRIC: markets / territories launched in]]` · `[[METRIC: units / sell-through]]` · close-up and detail shots (only the one wide flat-lay exists).

### Shenzhen solo exhibition
- **Have:** 1 façade photo.
- **Framing (public, to verify):** "Philip Colbert: The Myth of the Lobster Planet", Sea World Culture and Arts Center, Shekou, 17 June – 15 October 2023. Co-organised by Pearl Lam Galleries and COEXIST, Colbert's first show in South China, 40+ works ([Pearl Lam press release](https://www.pearllam.com/wp-content/uploads/2023/06/Press-Release-EN.pdf)). The banner dates in the photo match.
- **Missing:** `[[FACT: what Aidan designed: key visual? banners? signage? catalogue?]]` · `[[METRIC: exhibition attendance]]` · `[[METRIC: press coverage]]` · interior / wayfinding / print photos (none). The other exhibition photos (Rome, Naples, Taipei, Pearl Lam, Room-1-2, Macao) could fill an "exhibition graphics across the partnership" section if Aidan worked on those.

### NEW LANGUAGE
- **Have:** 1 photo (sweatshirt + flash wall), the year, the Instagram handle.
- **Missing:** `[[FACT: what Aidan designed: logo, wordmark, merch, signage, social?]]` · `[[FACT: the studio's positioning / brief]]` · `[[METRIC: follower growth / bookings]]` · `[[QUOTE: studio owner]]` · logo artwork, applications (cards, signage, social posts): none in repo.

### Psychic Attack
- **Have:** the richest content on the site. Concept text, specs (A5, 40pp, staple-bound, printed at home), "Both editions sold out", 11 images including covers, 8 spreads, tee.
- **Missing:** `[[METRIC: print run per edition]]` · `[[METRIC: time to sell out]]` · `[[FACT: where it was sold (shops / fairs / online)]]` · `[[METRIC: t-shirt run]]`.

### Moorland, "Praise"
- **Have:** title, year, Vimeo loop, YouTube link.
- **Missing:** `[[FACT: Aidan's role: director? editor? art direction? graphics/titles?]]` · `[[FACT: is Moorland Aidan?]]` · `[[METRIC: video views / streams in first X weeks]]` · `[[METRIC: press coverage]]` · stills (we can pull frame grabs from the video, since that's existing media, but can't do it from here).

### Duke Keats, "Monkey Brains"
- **Have:** title, year, Vimeo loop, YouTube link.
- **Missing:** `[[FACT: Aidan's role]]` · `[[FACT: the artist's world / who Duke Keats is]]` · `[[METRIC: video views]]` · `[[METRIC: press coverage]]` · stills.

### Grey Area Taipei
- **Have:** 1 flyer (Instagram 4:5), the event name "Ground" and date "April 6th", the year, the Instagram handle.
- **Missing:** `[[METRIC: event attendance / tickets sold]]` · `[[FACT: one-off or ongoing series of flyers?]]` · `[[METRIC: Instagram engagement on launch post]]`.

### Hefty Bruises 002
- **Have:** 1 sleeve image (Bandcamp file), artists "SDS MAX + VERE", catalogue no. HEFTY002, the Bandcamp link.
- **Missing:** `[[FACT: did Aidan design 001 / the label identity?]]` · `[[METRIC: pressing size / sell-through]]` · photo of the physical vinyl.

### Radio Residencies
- **Have:** the description (Voices Radio, RTM Radio, monthly), dates, 1 show tile, the SoundCloud playlist.
- **Missing:** `[[METRIC: number of shows / years]]` · `[[FACT: did Aidan design the show artwork?]]` · `[[FACT: how this connects to his design work (Grey Area, Hefty Bruises, music videos)]]`.

### Personal Graphic Exploration
- **Have:** 12 works + composite, a one-line rationale (found imagery, archival research).
- **Missing:** `[[FACT: titles/years per piece]]` · `[[FACT: were any shown / printed / sold?]]`. The visual DNA links to Psychic Attack (archival halftone), Grey Area (ornate type + cartoon), Hefty Bruises (spatter textures) and the radio tile (framed halftone portrait), which is the "lab feeds client work" story. No new media is needed for this one.

### About / CV
- **Missing:** a real CV (`[[FACT: education, employment, clients]]`), plus `[[METRIC: years at Colbert studio]]` to replace "Over 4 years".

---

## 5. Discovery: how strong case studies are structured

**Method note.** This cloud session's network allowlist blocks direct page fetches for the reference sites (pentagram.com, johnniewalker.com, itsnicethat.com and others failed with "not found"). The findings below come from web-search results about those pages plus general knowledge of the formats. I couldn't open each page to check its layout. If you want them verified page by page, add `pentagram.com`, `www.pentagram.com`, `www.itsnicethat.com`, `www.creativereview.co.uk`, `www.johnniewalker.com`, `vimeo.com` and `www.youtube.com` to the environment's allowlist and start a new thread.

**The Robert Wun reference.** I couldn't find a Robert Wun–owned page for the Johnnie Walker collab, or any source for "40 markets". Johnnie Walker's own framing is "two worlds of craftsmanship: Scotch Whisky and haute couture". The press release lists "selected markets including the US, Greater China, South East Asia, Canada, Australia, Europe and the UK". If you have the link you meant, send it and I'll check it.

### Cross-cutting patterns (all types)
1. **Metadata strip up top.** Pentagram project pages pair a short lede with a structured block: Client · Sector · Discipline · Office · Partner(s) · Project team · Collaborators (each named with their role). This is the at-a-glance strip in your brief. Collaborators are credited separately from the core team, which is the honest way to show Aidan's role inside Colbert's studio.
2. **Two depths per project.** Pentagram serves a visual-first project page and a separate long-read "/story" page for the same work. That matches "top 3–4 get full case studies, the rest short" and can be done within one page as an image run followed by an optional "Read the story" section.
3. **Lead with the idea, not the deliverable.** The strongest write-ups state the idea in one line (Pentagram's MoCA identity, for example, is framed around a square motif taken from Maya Lin's architecture) before any list of applications.
4. **Image : text ratio.** Visual-led pages run roughly 80/20 image to text. Text sits in short blocks between image runs, never one long essay up top.
5. **Credits are factual and specific.** Who did what, plus outside specialists. No adjectives.

### A. Brand collaborations (artist × brand)
- **Section order the best examples use:** one-line idea framed as two worlds meeting (Johnnie Walker × Robert Wun: "two worlds of craftsmanship") → what each partner brings (heritage/craft on one side, the artist's universe on the other) → the object(s) → availability and scale (markets, limited run) → credits.
- **Media sequence:** hero product shot → packaging detail → product in a styled set → (when available) retail or campaign in-situ → close-ups of motifs.
- **Role and impact:** brand press releases state markets, edition size and price. Designer portfolios state role in the credit block ("Packaging design", "Illustration adaptation"). Trade coverage frames value as collectability and storytelling ([The Spirits Business, Feb 2026](https://www.thespiritsbusiness.com/2026/02/the-rise-of-artist-designed-bottles-in-spirits/)).
- **Evidence:**
  - [Johnnie Walker × Robert Wun, Year of the Horse (brand story)](https://www.johnniewalker.com/en/stories/robert-wun-lunar-new-year-horse) and [press release via Yahoo Finance](https://finance.yahoo.com/news/johnnie-walker-haute-couturier-robert-192500440.html)
  - [Business of Fashion: Johnnie Walker × Olivier Rousteing](https://www.businessoffashion.com/articles/luxury/inside-luxury-whisky-brand-johnnie-walker-vault-strategic-fashion-play-olivier-rousteing-collaboration/). Notably it credits the packaging agency (Servaire&Co) separately from the artist, which is the same split as Aidan inside Colbert's studio.
  - [Formes de Luxe: 16 wine & spirits artist collabs](https://www.formesdeluxe.com/article/artists-artisans-musicians-and-fashion-designers-16-wine-spirits-collabs-showcasing-packaging-creativity.65215)
- **Implication for Aidan:** the "brand bridge" section works best written as *"Colbert's world brought X; [brand] brought Y; the studio's job was Z"*, with Aidan's part in the credit strip. That's honest even if his role turns out to be partial.

### B. Exhibition identity and graphics
- **Section order:** exhibition name, venue, dates → the curatorial idea in one line → the graphic idea (usually one motif or typographic move) → applications from outside in (street banners, façade, entrance, title wall, wayfinding, captions, print) → the catalogue/campaign → credits (exhibition designer and graphic designer listed separately).
- **Media sequence:** façade/street → entrance/title wall → room views → detail of type → printed matter. In-situ photography carries nearly all of it.
- **Role and impact:** Pentagram's exhibition pages credit the exhibition designer and graphics separately (e.g. Wes Anderson: The Archives, designed by Ab Rogers Design with Pentagram on graphics and campaign). Impact is rarely numeric on studio pages; it comes from press and attendance.
- **Evidence:**
  - [Pentagram: Wes Anderson: The Archives (Design Museum)](https://pentagram.com/work/wes-anderson-the-archives)
  - [Pentagram: Museum of Chinese in America (identity + environmental graphics)](https://pentagram.com/work/museum-of-chinese-in-america/story)
  - [Pentagram: Cooper Hewitt](https://pentagram.com/work/cooper-hewitt-smithsonian-design-museum-1/story) and [It's Nice That coverage of it](https://www.itsnicethat.com/articles/pentagram-cooper-hewitt)
  - [Typotherapy: Tamasha exhibition identity](https://www.typotherapy.com/clients/tamasha-exhibition/exhibition-design-visual-identity/), a smaller-scale model closer to Aidan's
- **Implication:** Aidan already has a strong out-of-doors sequence across the Colbert shows (Shenzhen façade, Rome bus, Naples banners, Taipei signage, Macao sign, Pearl Lam and Room-1-2 title walls). If he worked on those, one "exhibition campaigns across 5 cities" study is stronger than a thin Shenzhen-only page.

### C. Identity for a small studio (tattoo / culture business)
- **Section order:** who the studio is and what it wanted to be seen as → the positioning problem (avoid the genre's clichés) → the mark and system → applications (merch, signage, social, cards) → result.
- **Media sequence:** logo hero → system sheet → merch / in-studio → social grid.
- **Role and impact:** small-studio case studies state services as a list (identity, art direction, web) and give impact qualitatively ("now seen as a fine-art destination"). Numbers, when they appear, are bookings or followers.
- **Evidence:**
  - [VMV.STUDIO: OSCO, London tattoo collective rebrand](https://www.vmv.studio/osco)
  - [Forma Studio: Ink Asylum](https://madebyforma.ro/project-inkasylum), which is framed around repositioning from tattoo parlour to fine-art destination
- **Implication:** the existing photo (merch against the studio's flash wall) is a good "applications" image but there's no mark/system image. This should be a short or mid-length piece until Aidan supplies more.

### D. Music videos
- **Section order:** artist + track + label/year → the concept in a sentence → Aidan's role → the embedded video → 3–6 sequenced stills → credits (director, DOP, editor, graphics) → views/press.
- **Media sequence:** autoplaying muted loop as the hero (the site already does this) → full embed → a stills strip.
- **Role and impact:** director and motion-design portfolios put a full credit block on every project and list awards/press under it.
- **Evidence:**
  - [It's Nice That: Nicer Tuesdays on Will Norman's video for Jme "TNMT"](https://nicertuesdays.itsnicethat.com/events/04-03-2025-london), an example of a video written up as an idea plus a maker
  - [It's Nice That: Studio Moross (art direction across music campaigns)](https://www.itsnicethat.com/articles/nicer-tuesdays-music)
  - [Composer/director credit-card conventions (Twine)](https://www.twine.net/blog/best-music-composer-portfolio-examples/), weaker, but shows the credit-per-project pattern

### E. Print, merch and culture pieces (zines, flyers, sleeves, radio)
- **Format the best independent designers use:** one image-led entry with a one- or two-line caption naming the client/artist, the object and the year. The work does the talking. Bráulio Amado's sleeves and posters are typically shown with just the client and title, and his yearly books collect hundreds of pieces with short captions.
- **Media sequence:** the object → 1–3 details or spreads → the object in hand/use if available.
- **Role and impact:** a single line ("Both editions sold out") is the right weight. It already exists on Psychic Attack.
- **Evidence:**
  - [It's Nice That on Bráulio Amado's 2017 publication](https://www.itsnicethat.com/articles/braulio-amado-2017-publication-230418) and [his Róisín Murphy sleeves](https://www.itsnicethat.com/features/roisin-murphy-braulio-amado-graphic-design-111220)
  - [The Vinyl Factory: Bráulio Amado's Juan MacLean artwork](https://www.thevinylfactory.com/features/braulio-amado-juan-maclean-brighter-light-artwork)
  - [It's Nice That: Ian Teeple's punk flyers](https://www.itsnicethat.com/articles/ian-teeple-illustration-graphic-design-discover-170826), flyer work presented as a body of practice

### F. Personal / self-initiated work
- **Pattern:** presented as the designer's practice rather than "projects". It's a grid with a short statement, sometimes with cross-links to the commissions where the language reappears. Cargo-built independent sites (Amado, Tereza Bettinardi, Victoria Escobar per [Colorlib's list](https://colorlib.com/wp/graphic-design-portfolios/)) keep this minimal: grid first, two-item nav.
- **Implication:** the brief's "lab behind the client work" framing fits. The concrete move is to tag each personal piece with the commissioned project it relates to (see the visual-DNA note in section 4).

---

## 6. Open questions for Aidan (blocking the full case studies)

1. What exactly did you design on Johnnie Walker, Adidas, ASUS and the Shenzhen show? Job title and dates at the Colbert studio?
2. Which of the other Colbert images (Bentley, Vogue SG, Big Issue, AS Roma, books, Rome/Naples/Taipei/Macao/Pearl Lam shows) did you work on?
3. Is Moorland you? What was your role on the Moorland and Duke Keats videos?
4. What did you make for NEW LANGUAGE, and do you have the logo or other applications?
5. Do you have any process material (sketches, iterations, dielines) or more in-situ photos you'd be happy to add? The brief says to use existing media only, so this is optional.
6. Any numbers you're comfortable publishing (print runs, markets, views, attendance)?

---

*Sources for public facts:* [Pearl Lam press release](https://www.pearllam.com/wp-content/uploads/2023/06/Press-Release-EN.pdf) · [ASUS press release](https://press.asus.com/news/press-releases/193) · [CTEE](https://www.ctee.com.tw/news/20240725701204-431207) · [FoodNext](https://www.foodnext.net/life/recipes/dinner/paper/5739978556) · [GOAT](https://www.goat.com/en-sa/sneakers/philip-colbert-x-superstar-save-the-lobster-gx7996) · [Marie Claire TW](https://www.marieclaire.com.tw/fashion/news/57087) · [Johnnie Walker × Robert Wun press](https://finance.yahoo.com/news/johnnie-walker-haute-couturier-robert-192500440.html)
