# Anti-slop: what makes a UI read as AI-made

The owner rejects UI that "looks AI generated". Each item below is a tell. Before showing any screen, sweep it against this list, delete what you find, and fix it with the replacement given.

Behind every tell is one test: **if someone could guess this design from its category alone ("an AI SaaS dashboard"), rework it.**

## The generated-dashboard tells (product UI)

| Tell | Instead |
|---|---|
| Dark or navy sidebar with a coloured active pill and a left bar | Light neutral sidebar, grey active pill |
| "Welcome back, Alex 👋" | A noun title ("Today") |
| Four KPI cards, each with an icon in a tinted circle | One divided KPI row, label above value, no icons |
| A green "+12.5%" and a sparkline on every KPI | Deltas only where they matter, with the window named; the trend gets its own chart |
| KPIs at 36–48px bold in the brand colour | 20–32px in ink |
| Gradient area chart, smoothed spline, a dot on every point | 2px straight line, no fill or ≤14% tint, no point markers |
| Rainbow palette, a different hue on every bar | One hue, or a lightness ramp of it |
| A fat donut with a big total in the hole | Stacked horizontal bar or bar list |
| Legend on a single-series chart; gridlines every 20px; axis lines on both sides | No legend; 3–5 faint gridlines; no y-axis line |
| 16–24px radius + border + big soft shadow on every card | 8px radius, 1px line, no shadow |
| Zebra table with uppercase headers, plus checkbox, avatar, chip and kebab on every row | Plain rows, sentence-case grey header, one status mark at most |
| Left-aligned proportional numbers | Right-aligned tabular figures |
| Saturated status chips with white text | Pale tint + dark same-hue text |
| The accent on every button, tab and link | The accent on the one primary action, selection and focus |
| Top bar with search + bell + avatar and nothing else real | A top bar only if it holds something real, or none |
| Export / Share / date picker clustered by the title | Each control where it acts |
| Acme Corp, John Doe, round vanity totals, growth on a week-old account | Real or honest data; "—" when unknown |
| Pagination under a 6-row list | "View all (n)" |
| An equal 4-up grid with orphans and stretched blank cards | Column count chosen from the item count; grid sum written down |
| Neon, glow or glass on dark | Flat surfaces, lighter per level |
| **Inter on #f8f8f8, white 12px cards, no colour on the data ("the kit's own face")** | Give the product a face: its hue on the main data series plus one signature element only this product has |
| A coloured icon per category | Text labels; one icon set, grey |
| Illustration + "No data yet" in an empty chart | The chart frame with its zero line and one sentence |
| **Rounded card with a thick coloured left border** | No side stripes; one status mark if needed |
| The same badge or sentence repeated on every row ("needs its own check") | Say a shared status once, at the top |
| Values in monospace "to look technical" | Body face with `tabular-nums` |
| Outlined boxes and coloured borders on every card, heavy double rings | Whitespace and grouping first; one 1px line |
| Explanatory fine print and system-voice asides ("(optional, saved to History)") | Delete it, or write one plain sentence where it's needed |

## Visual tells (any surface)

- **Colour:**
  - purple/violet → blue, blue → cyan or indigo → pink gradients
  - gradient text
  - Tailwind stock indigo/violet as the accent
  - glows, halos, radial spotlights, aurora/mesh blobs
  - glassmorphism and `backdrop-filter` blur as decoration
  - cream/beige + terracotta "warm minimal"
  - near-black + one neon
- **Type:**
  - eyebrows and kickers (a small label above a heading); delete the line, and if nothing but a name for what follows was lost, it was an eyebrow
  - tracked uppercase micro-labels
  - mono used as costume
  - an italic, serif or coloured "accent word" inside a heading
  - oversized full-sentence headlines
  - 9 nearly equal type sizes (a flat hierarchy, under 1.25× per step)
- **Layout:**
  - three icon-above-heading feature cards
  - icons in rounded coloured tiles
  - a card nested inside a card
  - everything centred
  - the same 12–16px radius on everything
  - identical section after identical section
  - numbered section labels (01 / 02 / 03)
  - bento grids
  - decorative grid or stripe backgrounds
  - floating blurred pill nav
- **Icons:** emoji or unicode glyphs used as icons (✨🚀🎯⚡🔥💡✅). Use one monoline SVG set (Lucide, Phosphor or Heroicons) at a 1.5–1.8px stroke with `currentColor`. Never mix two icon libraries.
- **Decoration:**
  - decorative status dots ("● Live", "Available")
  - pulsing dots
  - blinking cursors
  - drawn browser or OS windows and device frames when a real capture is possible
  - fake product UI built from grey bars
  - hand-drawn SVG people
- **Shadows:** hard offset shadows; a thin border plus a wide shadow on every card in a row.
- **Motion:**
  - the same fade-up on every block
  - hover lift on every card
  - bounce or overshoot
  - meaningless infinite loops
  - reveals that fail and leave a blank band

## Copy tells

- **Banned words:** unlock, unleash, supercharge, elevate, empower, streamline, seamless, effortless, robust, cutting-edge, next-gen(eration), world-class, best-in-class, industry-leading, mission-critical, future-proof, game-changer, revolutionize, reimagine(d), harness, leverage (as a verb), delve, journey, "in today's landscape".
- **Banned shapes:**
  - "Not just X, it's Y"
  - tricolons ("Fast. Simple. Secure.")
  - "Whether you're X or Y"
  - "Say goodbye to…"
  - "Built for the modern team"
  - "X, reimagined"
  - "Welcome to…" / "Meet…"
  - colon titles ("Ledgerly: invoicing for…")
  - aphoristic cadence repeated 3+ times
- **Banned filler:**
  - "Get started" and "Learn more" as default buttons
  - "Click here"
  - lorem ipsum
  - "Feature one / two / three"
  - "Oops!"
  - exclamation marks in errors
  - celebratory toasts for visible effects
- **Dashes:** em dashes at most about one per screen; prefer a full stop or a colon. Use an en dash only for ranges.
- **Captions** that narrate the design ("This card shows your stats") are slop.
- **Invented proof:** no invented metrics ("10× faster", "99.9% uptime"), testimonials, logo walls or case counts. **An honest placeholder beats a fake stat.**
- **Fake sends:** a form that prints "Sent" with no request behind it is a blocker.

## How to use this list

1. Before showing a mockup or opening a PR, take a screenshot and sweep it against the tables above.
2. Count the words on screen before and after your changes; fewer is usually better.
3. Record every tell you found and fixed in the PR body as one line each.
4. A tell kept on purpose (e.g. the brand really is violet) belongs in DESIGN.md with its reason; then it is no longer a tell.
