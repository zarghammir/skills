# Marketing and content pages (Persuade and Read modes)

This file covers **Persuade** pages (landing pages, product sites, pricing) and **Read** pages (docs, articles). These pages are read and scrolled, not worked in. They get more expression than product screens, but the anti-slop list still applies in full.

## Process

1. **Mockup first.** The owner approves a whole-site mockup (every page, light and dark, phone and desktop) before any build. Publish it as an Artifact page.
2. **Inventory 8–12 facts** specific to this subject before writing a word. Copy built from facts can't be generic.
3. **Write the argument.** Each section makes one claim and gives its proof. A section with no claim is deleted.
4. **Write the idea sentence** ("On this page, [the product] becomes [one visual device]") and pick **one live thing**: the single moving or interactive element the page is remembered for. Everything else stays still.
5. **Run the competitor test.** Swap the logo for a competitor's. If the page still works, it is generic; rework the idea.

## Rules

- **Specific reference, not adjectives.** Name one real-world object the page should feel like.
- **Headlines:**
  - At most 2 lines at every width, about 5 words.
  - Display size at least 4× the body; tracking −0.02 to −0.04em; leading 0.95–1.1.
  - Left-aligned, with at most one centred moment.
- **Body text:** 16–20px, leading 1.5–1.6, 45–75ch. At most 5 type sizes and 2 typefaces on the page.
- **Space:** 96–160px between sections, equal outer margins, and no blank stretch over half a screen.
- **Colour:** one ground (70–90% of the page), one ink, one accent under 5% of any screen.
- **Nav:** wordmark, 3–5 links, one action.
- **Sections vary in layout.** Don't follow the stock order (hero, logos, three features, testimonial, pricing, CTA). Use the order the argument needs.
- **Images:** real product captures and real photos, never drawn browser chrome or a fake dashboard made of grey bars. Set `aspect-ratio` on every image, and never lazy-load the LCP image.
- **Proof:** only real proof (named customers who agreed, real numbers with a source). No logo walls of companies that aren't customers.
- **Calls to action:** one primary action, repeated at most once (at the end), with specific wording ("Make your first video"), not "Get started" or "Learn more".

## Motion (Persuade only)

- **Tokens:** `--ease-out cubic-bezier(.22,1,.36,1)`, `--ease-expo cubic-bezier(.16,1,.3,1)`. Press 140ms, hover 180ms, UI 240ms, one hero reveal 600–900ms. Exits at 60–70% of the entrance. Stagger 50–90ms, 500ms total at most.
- **One authored motion moment**, plus at most one supporting effect per viewport. Content is visible with scripts off and under reduced motion.
- **Banned:**
  - bounce
  - preloaders
  - custom cursors
  - scroll hijacking
  - typewriter text
  - the same fade-up on every section
  - hover lift on every card
  - parallax on body copy
  - auto-rotating carousels without pause
- **Scroll storytelling** (GSAP ScrollTrigger, scroll-world style video flights) needs owner approval, with the cost stated first, and a still fallback under reduced motion.

## Read mode (docs, articles)

- Measure 60–75ch, body 16–18px with leading 1.6–1.75.
- Headings use a clear scale with more space above than below.
- Code blocks scroll inside their own frame.
- A table of contents for long pages.
- No motion beyond feedback.

## Technical floor

- **Basics:** `lang`, `<title>` and meta description on every page; a skip link; real heading order with no skipped levels.
- **Overflow:** `overflow-x: clip` on html and body (not `hidden`, never `100vw` widths); `min-width: 0` on display headings inside grids.
- **Above the fold:** the headline, the lede and the primary action all visible at 1280×800.
- **Speed:** WebP or AVIF images, reserved space (CLS under 0.1), `font-display: swap`.
