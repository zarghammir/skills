---
name: ui-standards
description: One house UI standard for every project and every agent. Load it BEFORE building, changing, mocking up or reviewing any user interface — web pages, app screens, dashboards, forms, tables, review/approval flows, components, HTML artifacts and prototypes, emails, mobile screens — and whenever someone says a UI "looks AI-generated", "too much text", "redesign", "make it better", "polish", or asks to review a UI PR. Merges 14 leading design skills (taste-skill, hallmark, impeccable, emilkowalski/skills, ui-ux-pro-max, open-design, Google design.md, awesome-design-md, magicui, react-bits, gsap-skills, scroll-world, canvas-ui, dimensional-drawing) with a product owner's standing UI rulings into one set of rules with exact values, a build workflow, a verification routine and a review gate. It wins over other installed UI skills when they disagree; a repo's DESIGN.md / AGENTS.md wins over it.
---

# UI standards

One standard for every screen any agent builds. These are the rules with exact values. The `references/` files hold the detail; load each one when its step comes up.

## Who wins when rules disagree

1. **The owner's explicit decision for this screen.**
2. **The repo's `DESIGN.md` and `AGENTS.md` / `CLAUDE.md`.** When you follow a repo rule that contradicts this skill, name the deviation and its reason in the PR body.
3. **This skill.**
4. **Other installed UI skills** (impeccable, frontend-design, emil-design-eng, apple-design, animate, shadcn, taste or hallmark copies, ui-ux-pro-max). Load them for depth: motion craft (emil-design-eng / animate), audit and critique verbs (impeccable), shadcn mechanics (shadcn). Where they contradict this skill, this skill wins. In particular, ignore their pushes toward glassmorphism, dark dashboards by default, style catalogs, forced novelty and GSAP-by-default.

## Step 0: what kind of surface is it?

| Mode | Surfaces | Bar |
|---|---|---|
| **Operate** (default) | App screens: dashboards, review and approval flows, tables, forms, settings, admin, tools | **Earned familiarity.** Precision and restraint; patterns users already know. → [product-screens.md](references/product-screens.md) |
| **Persuade** | Landing pages, product sites, pricing | One idea, one live thing, real proof. → [marketing-pages.md](references/marketing-pages.md) |
| **Read** | Docs, articles, help | Measure, rhythm, nothing moves. → [marketing-pages.md](references/marketing-pages.md) |

The mode comes from the surface, not the product: a product's dashboard is Operate, its marketing site is Persuade.

## The workflow

1. **Read the context first.**
   - The repo's DESIGN.md. If there is none, propose one from [design-md-template.md](references/design-md-template.md), derived from the shipped UI.
   - AGENTS.md.
   - The screens that already exist next to yours (match their components, spacing and words).
   - The owner's recorded decisions for this project (tickets, notes, agent memory).
2. **Decide the scope.**
   - **"Redesign", "make it better" or "simplify" from the owner means REFINE today's screen:** fewer words, the existing colours, small polish. It does not mean restructure. Keep what the owner liked. Show Today vs Proposed. Cap the change list at about 6 items.
   - If you can't tell whether they want a refine or a restructure, ask in one line.
   - **Mockup first** for anything big: a new page, a new flow, or a restructured screen. Show a whole-page mockup as a published Artifact, get the owner's approval, THEN build. Small changes that follow an approved pattern (a line, a button, a label) need no mockup.
3. **Design the page as a whole** before writing components.
   - Name the screen's **one question** and its **one finding**.
   - Lay out the page anatomy: steps bar on top for multi-step work, a two-column work area, compact secondary sections, the primary action **once** in a pinned header (with its price beside it if it costs money), destructive controls small.
   - **Every action appears once per page;** an edit control sits next to the thing it edits.
   - **Each step shows only its own sections.**
   - Choose the column count from the real data, and write the grid sum down.
4. **Build with tokens and every state.**
   - No literal colours or fonts outside the token file.
   - Every control has all 8 states ([components.md](references/components.md)).
   - Every data region has loading, empty, error, full and edge states.
   - Write copy to [copy.md](references/copy.md); motion follows [motion.md](references/motion.md).
5. **Verify by looking** ([verify.md](references/verify.md)).
   - Click every changed control and screenshot it.
   - **Read the whole frame**, at 390 / 768 / 1280, in light and dark.
   - Run the worst-case data sweep.
   - Follow the project's machine rules (some teams share one browser slot between agents). Never download a new tool.
6. **Self-review against the gates** ([review.md](references/review.md)) and [anti-slop.md](references/anti-slop.md).
   - Fix every Floor item.
   - Fix each Reflex item, or waive it in the PR body with a reason.
   - The PR body carries 2–4 screenshots and the list of tells you removed.

## The Floor (never waived, a BLOCK in review)

1. **Contrast.** Text, placeholders, error and success text ≥4.5:1. Large text, icons, input and control edges, focus rings and chart marks ≥3:1. Check both themes.
2. **Focus and keyboard.** A visible `:focus-visible` ring that appears instantly. Everything works by keyboard. No `outline: none` without a replacement. No clickable `<div>`.
3. **Hit targets** at least 24×24 CSS px. The house target is 44×44 on touch and for primary controls. No action reachable only by hover.
4. **States.** Every data region has loading (layout-shaped, no shift), empty (what + one action), error (in place: what, why, what to do + Retry) and full. No control can be submitted twice.
5. **Honest data.** No invented metrics, testimonials, Acme or John Doe in shipped UI. Displayed totals reconcile with the displayed values. Never render `NaN`, `undefined` or `null`. No fake send.
6. **Layout integrity.** No page-level horizontal scroll at 320–2560px. No clipped or overlapping text. Menus are never clipped by an `overflow: hidden` ancestor. Inputs are 16px on phones, and zoom is never disabled.
7. **Motion safety.** A `prefers-reduced-motion` variant ships with every animation. No `transition: all`. Only transform and opacity are animated. Nothing animates on keyboard shortcuts or 100+/day actions. Nothing flashes more than 3 times a second.
8. **Tokens.** No literal colour or font-family outside the token file. One icon set; no emoji as icons.
9. **The blocker tells:**
   - purple/violet→blue gradients and gradient text
   - a thick coloured left stripe on cards
   - a card nested inside a card
   - an icon in a coloured tile on every card or KPI
   - an eyebrow/kicker label above headings
   - glass or glow as decoration
   - the same badge or sentence repeated on every row
10. **Semantics.** Native elements first; icon-only buttons have names; errors are announced; images that carry meaning have alt text.

## Product defaults at a glance (Operate)

| Thing | Default |
|---|---|
| Shell | Labelled **left sidebar** 224–240px, light and neutral, grey active pill, 16px outline icons, 14px labels, sentence case |
| Dashboard home | At most 3 blocks: today's progress · waiting for your approval (count + button) · spend this month. Everything else is its own page. |
| Page title | One h1, a noun, 20–28px at 600. Optional grey data subline. Never "Welcome back". |
| Primary action | **One filled button per view, shown once:** in a pinned header on long or multi-step pages, with its price beside it if it costs. **No duplicate buttons.** Everything else is secondary, ghost or link. |
| Accent | One colour, about 2 visible uses per screen: primary action, focus, selection, main data series |
| Type | One sans; 24 / 16 / 14 / 12 (11 floor); weights 400 / 500 / 600; tabular figures on numbers; **no monospace values** |
| Space | 4px base; scale 4 · 8 · 12 · 16 · 24 · 32 · 40 · 64; one gutter value (16); card padding 20 |
| Surfaces | Resting card: 1px line, no shadow, radius 8. Shadows only on floating layers. Border OR shadow. |
| Controls | Height 32–40 (44 on touch); radius 6; input edge ≥3:1; label above |
| Tables | Rows 40–48; grey sentence-case header with no fill; numbers right-aligned; one status pill max per row; no zebra |
| KPIs | One divided row; value 20–32px; no icon tiles or sparklines; deltas name their window; colour = good/bad |
| Charts | One series (three max); one hue; 2px straight lines; 3–5 faint solid gridlines; no fat donut or gauge; animation off |
| Motion | Feedback only. Press 120ms `scale(.97)`; menu 200ms; modal 250ms; drawer 300ms; cap 300ms; ease-out `cubic-bezier(.23,1,.32,1)`; never ease-in; no entrances |
| Phone | Sidebar becomes a top bar + sheet or a 4–5 item bottom bar; tables become two-line rows under 640px; targets 44px |
| z-index | 1 · 10 · 100 (dropdown) · 200 (sticky) · 300 (nav) · 400 (modal) · 500 (toast) · 600 (tooltip) |

## House taste (from a product owner's standing rulings)

- **Human, not AI-made.**
  - Write like a colleague: short, plain, warm.
  - Verbs on buttons.
  - Say a shared status once, at the top.
  - One accent, used once. Values in the normal font.
  - No outlined boxes or coloured borders on every card.
  - Count the words before and after.
- **Visual first.** Owners judge what they see, so show a picture (screenshots, a mockup, a published page) rather than describing it in prose.
- **Not a pile.**
  - Pages are composed, not stacked: progress on top, work side by side, the primary action pinned once.
  - **Every action appears once on a page,** never repeated "for convenience".
  - **Each step shows only its own sections.** A Publish step doesn't show the draft again.
  - Every suggestion carries an Apply action, priced if it costs.
  - Approve once for a set.
- **Refine before restructure.** Never take away a part of today's screen the owner likes without asking.
- **Any niche.** User content, niche words and examples come from data or settings, never hard-coded into the UI.

## Pre-delivery checklist (paste into the PR body)

```
UI standards — ui-standards skill
- [ ] Mode: Operate / Persuade / Read; DESIGN.md read (or proposed)
- [ ] Scope: refine vs restructure confirmed; mockup approved (if big)
- [ ] One question/finding per screen; layout composed (steps bar / two columns / primary pinned once); no duplicate buttons; each step shows only its own sections
- [ ] Floor 1–10 pass (contrast, focus, targets, states, honest data, layout, motion, tokens, tells, semantics)
- [ ] All 8 control states; 5 data-region states; worst-case data sweep done
- [ ] Copy: verbs on buttons, no repeated per-row text, no banned words; word count before → after
- [ ] Clicked every changed control; screenshots read at 390 / 768 / 1280, light + dark
- [ ] Anti-slop sweep: tells removed → <list>
- [ ] Reflex waivers (rule → reason): <none / list>
- [ ] Screenshots attached (where it lives, main, variant, detail)
```

## Reference map

| Need | File |
|---|---|
| Dashboards, tables, KPIs, charts, forms, settings, states, phone | [references/product-screens.md](references/product-screens.md) |
| Type, colour, surfaces, space, z-index, dark mode, responsive, accessibility | [references/foundations.md](references/foundations.md) |
| Control states, field / overlay / toast recipes, library picks, effect libraries and their licences | [references/components.md](references/components.md) |
| Every AI tell with its replacement | [references/anti-slop.md](references/anti-slop.md) |
| Button, error, empty and loading wording; voice | [references/copy.md](references/copy.md) |
| Durations, easing, recipes, performance, reduced motion, GSAP | [references/motion.md](references/motion.md) |
| Click-and-look, viewports, worst-case data catalog | [references/verify.md](references/verify.md) |
| Gate tiers, severities, review questions, verdict format | [references/review.md](references/review.md) |
| Landing pages, sites, docs | [references/marketing-pages.md](references/marketing-pages.md) |
| Per-project DESIGN.md contract and template | [references/design-md-template.md](references/design-md-template.md) |
| Where every rule came from | [SOURCES.md](SOURCES.md) |
| Portable version for cloud sessions and other tools | [PROMPT.md](PROMPT.md) |
