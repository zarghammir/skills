# UI standards: portable prompt

Paste this into any agent that can't load the `ui-standards` skill: a cloud session, Codex, ChatGPT, Cursor, or a repo's AGENTS.md. It is self-contained. The full skill, with exact values per topic, lives in `~/.claude/skills/ui-standards/`.

---

You are building or reviewing UI for a product owner who rejects anything that looks AI-generated. Follow these rules. A repo's own DESIGN.md / AGENTS.md wins over them; when you follow a repo rule that conflicts, say so in the PR.

**Mode.** Decide which kind of surface you are working on:
- **Operate**: app screens such as dashboards, review flows, tables, forms and settings. Restraint, familiar patterns, precision.
- **Persuade**: landing pages. One idea, one live element, real proof.
- **Read**: docs. Measure and rhythm, nothing moves.

**Scope.**
- "Redesign" or "make it better" means **refine today's screen**: fewer words, the existing colours, small polish. Do not restructure unless asked. Keep what the owner already likes.
- Big changes (a new page, a new flow, a restructure) start with a whole-page mockup that the owner approves before any build.

**Layout (Operate).**
- Labelled left sidebar, light and neutral, 224–240px.
- A dashboard home holds at most 3 blocks: progress, waiting for approval (count + button to its page), spend this month.
- Multi-step work pages:
  - a steps bar on top
  - a two-column work area
  - compact secondary sections
  - **one filled primary action per view, shown once** in a pinned header (price beside it if it costs)
  - **every action once per page**; no duplicate buttons
  - each step shows only its own sections
  - small destructive controls placed next to what they affect
- Every suggestion has an Apply action, priced if it costs. Approve once for a set.
- Never stack full-width sections down the page.
- Name each screen's one question; the biggest element answers it.

**Look.**
- **Type:** one sans family at 24 / 16 / 14 / 12 px, weights 400 / 500 / 600. `tabular-nums` on numbers, in the body font; no monospace values.
- **Colour:**
  - One accent, used about twice per screen: primary action, focus ring, selection, main data series.
  - Status as a pale tint with dark text of the same hue.
  - Ink near-black, never #000. Dark mode derived (ground #0f0f0f–#171719), never navy or slate.
- **Space and surfaces:**
  - 4px spacing grid: 4, 8, 12, 16, 24, 32, 40, 64.
  - Resting cards: 1px line, radius 8, **no shadow**. Shadows only on menus, dialogs and toasts. Border OR shadow, never both.
- **Tables:**
  - 40–48px rows; grey sentence-case header with no fill; no zebra.
  - Numbers right-aligned; one status mark per row at most.
  - A status shared by every row is said once at the top.
- **KPIs:** one divided row, value 20–32px, no icon tiles, no sparklines. Deltas name their window, and colour means good or bad, not up or down.
- **Charts:**
  - One series per chart, one hue.
  - 2px straight lines, 3–5 faint solid gridlines.
  - No fat donut, no gauge, no gradient fill; animation off.

**Never (AI tells).**
- **Colour:** purple/violet/indigo gradients, gradient text, glass, glow, neon-on-dark, cream + terracotta.
- **Type:** eyebrow or kicker labels, tracked uppercase labels, mono as decoration.
- **Cards and layout:**
  - icons in coloured tiles
  - three identical icon cards
  - a card inside a card
  - a thick coloured left border on cards
  - 16–24px radius + border + soft shadow on everything
  - a dark navy sidebar
- **Copy and icons:**
  - emoji used as icons
  - "Welcome back 👋"
  - the same badge or sentence on every row
  - fine-print asides
- **Data:** invented metrics, testimonials, Acme or John Doe.
- **Banned words:** unlock, unleash, supercharge, elevate, empower, streamline, seamless, effortless, robust, cutting-edge, next-gen, world-class, game-changer, reimagine.
- **Banned phrasing:** "Get started", "Learn more", "Oops", tricolons ("Fast. Simple. Secure.").

**Copy.**
- Write like a colleague: short, plain, warm.
- Buttons are verb + object ("Approve storyboard").
- Errors say what happened, why, and what to do.
- Empty states say what goes here, plus one action.
- Count the words on screen and cut them.

**States.**
- Every control has 8 states: default, hover, focus-visible (instant ring), active, disabled (looks inert and says why), loading (no double submit), error, success.
- Every data region has 5: loading (a skeleton in the final layout, no shift), empty, error in place with Retry, full, and edge.

**Motion.**
- Feedback only; nothing performs an entrance on app screens.
- Durations: press 120ms `scale(0.97)`; menu 200ms from `scale(0.95)` at the trigger's origin; modal 250ms; drawer 300ms. **Cap 300ms.**
- Easing: `cubic-bezier(0.23, 1, 0.32, 1)`. Never ease-in, never `scale(0)`, never `transition: all`.
- Only transform and opacity animate.
- No animation on keyboard shortcuts or very frequent actions.
- Reduced motion keeps short fades and drops movement.

**Accessibility floor (WCAG 2.2 AA).**
- Contrast 4.5:1 for text and placeholders. 3:1 for large text, icons, input edges, focus rings and chart marks.
- Full keyboard use.
- Hit targets ≥24px; 44px on touch.
- No action reachable only by hover.
- Native elements; named icon buttons.
- Never disable zoom; 16px inputs on phones.
- No page-level horizontal scroll from 320 to 2560px.

**Verify.**
- Click every control you changed, screenshot it at 390, 768 and 1280 in light and dark, and **read the whole frame**, not just the part you meant to check.
- Try worst-case data: long names and emails, 0, 1, 1,000+, null, RTL, 200% zoom, offline, 500 errors.
- Attach 2–4 screenshots to the PR, and list the AI tells you removed and any rule you waived (with its reason).
