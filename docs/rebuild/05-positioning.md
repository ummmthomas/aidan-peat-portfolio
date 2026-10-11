# Site-wide value narrative: three positioning directions

Step 4 of the rebuild. **Direction 1 is built into this branch.** Directions 2 and 3 are written out below so they can replace it. The copy for them lives here rather than in `site-src/`, and switching means editing `site-src/pages/homepage.html`, `about.html`, `top-nav.html` and `site-src/routes.json`.

Every direction is built only from what the site already says: the old hero line "Graphic designer and visual artist. London, UK.", the About copy ("a strong interest in the arts, contemporary culture, and navigating creative solutions through the power of design", "Over 4 years of experience within a fast-paced artist's studio"), the Colbert copy and the project list.

---

## Direction 1 (built): the artist's world, made into brands

**The idea:** Aidan's strongest, most commercial work is translating one artist's universe into brand partnerships with global brands, and the branded content that launches them. Lead with that, in the industry's own terms: "brand partnerships" and "branded content". Everything else shows the same instinct at culture scale.

**Hero headline:** Turning an artist's world into work brands can launch, and fans want to keep.

**Subhead:** Graphic designer and visual artist, London. Four years in Philip Colbert's studio, across his brand partnerships with Johnnie Walker, adidas and ASUS, the branded content around them, and his exhibitions from Shenzhen to Naples. Outside it: flyers, sleeves, videos and identities for music and nightlife.

**About (opening):** Graphic designer and visual artist, based in London. I make an artist's world work for a brand, and a brand's world work for an artist: brand partnerships, and the branded content that launches them. Over 4 years of experience within a fast-paced artist's studio, Philip Colbert's… *(full text in `site-src/pages/about.html`)*

**Index order and grouping:**
1. *Philip Colbert, 2022–2026 · Brand partnerships and branded content*: Johnnie Walker, Shenzhen, adidas, ASUS, the whole partnership
2. *Music, nightlife and culture*: Moorland, NEW LANGUAGE, Grey Area, Duke Keats, Hefty Bruises, Radio
3. *Self-initiated*: Psychic Attack, Personal Graphic Exploration

**Card captions:** Limited gift boxes made to be collected · A solo show announced at building scale · The Superstar, saved by a lobster · A laptop sold as a collectable · An identity that works as merch · Two zines, both editions sold out · The lab behind the client work

**Card metrics:** each card leads with one number from its case study's impact stats, pulled in by `tools/build.py` (the first filled-in stat marked `data-headline`, else the first filled-in stat). Cards with nothing filled in yet show their `[[METRIC]]` placeholder, highlighted, until the number arrives. The Colbert hub's case-study cards work the same way.

**Page title / meta (home):** "Aidan Peat: graphic designer for brand partnerships and branded content" / "Graphic designer and visual artist, London. Four years in Philip Colbert's studio, across his brand partnerships with Johnnie Walker, adidas and ASUS and the branded content around them, plus flyers, sleeves, videos and identities for music and nightlife."

**Nav:** About · Instagram · Work with me
**Contact CTA:** Planning a brand partnership or branded content with an artist? Get in touch.

**Risk:** this direction stands or falls on Aidan's role in the Colbert brand partnerships. If his part turns out to be small, use Direction 2.

---

## Direction 2: visual identity for culture

**The idea:** Aidan as the designer culture comes to, across music, nightlife, fashion and tech. The Colbert work becomes the biggest proof, not the whole pitch. It's the safer choice if his Colbert role was supporting.

**Hero headline:** Graphics for the culture brands want to be part of.

**Subhead:** Graphic designer and visual artist, London. Music videos, club flyers, record sleeves and a tattoo studio's identity, and four years in Philip Colbert's studio on work that reached Johnnie Walker, adidas and ASUS.

**About (opening):** Graphic designer and visual artist, based in Hackney, London. I have a strong interest in the arts and contemporary culture, and I design for the people who make it: musicians, clubs, labels, studios and artists. Over 4 years of experience within a fast-paced artist's studio, Philip Colbert's, on collectable artworks, exhibition campaigns, books and brand collaborations. I've also played monthly radio mixes since 2021.

**Index order and grouping:**
1. *Music and nightlife*: Moorland, Duke Keats, Grey Area, Hefty Bruises, Radio
2. *Brands and artists*: the Philip Colbert hub (with JW, adidas, ASUS and Shenzhen inside it), NEW LANGUAGE
3. *Self-initiated*: Psychic Attack, Personal Graphic Exploration

**Card captions:** Moorland: a visual world for "Praise" · Grey Area: a flyer for Ground, Taipei · Hefty Bruises: a sleeve for SDS MAX + VERE · Radio: five years on London radio · Philip Colbert: four years, one lobster, many brands · NEW LANGUAGE: an identity that works as merch

**Page title / meta (home):** "Aidan Peat: visual identity for music, nightlife and culture" / "London graphic designer and visual artist making flyers, sleeves, music videos and identities for culture, and four years of brand work in Philip Colbert's studio."

**Nav:** Work · About · Instagram · Email
**Contact CTA:** Got a release, a night or a brand to launch? Email me.

---

## Direction 3: found images, made new

**The idea:** Lead with Aidan's method rather than his clients: archival research and found imagery turned into graphics. The personal work and the zines become the front door, and the commissions show the method paying off. This is the most distinctive direction and the least commercial.

**Hero headline:** Found images, made new.

**Subhead:** London graphic designer and visual artist. I dig through archives (UFO cuttings, old stickers, occult print, clip art) and turn what I find into work for artists, brands, clubs and labels.

**About (opening):** Graphic designer and visual artist, based in London. I regularly invest time outside of work into experimenting with my personal artistic style, incorporating my passion for found imagery and archival research. That habit runs through everything: two sold-out zines, flyers, sleeves and over 4 years in Philip Colbert's studio.

**Index order and grouping:**
1. *Personal Graphic Exploration* and *Psychic Attack* first
2. Then culture: Grey Area, Hefty Bruises, Radio, NEW LANGUAGE, Moorland, Duke Keats
3. Then the Philip Colbert hub and collaborations

**Card captions:** The lab behind the client work · Two zines from a personal archive, both sold out · Ornate type and a cartoon mascot for a Taipei club · Spatter and grit for a record sleeve · An artist's lobster, carried into global brands

**Page title / meta (home):** "Aidan Peat: graphic design from found imagery and archives" / "London graphic designer and visual artist turning archival research and found imagery into zines, flyers, sleeves and brand work."

**Nav:** Index · About · Instagram · Email
**Contact CTA:** Have something that needs digging into? Email me.
