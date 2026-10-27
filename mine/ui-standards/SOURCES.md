# Sources

This skill restates, in our own words, rules distilled from the repositories below, merged with one product owner's standing UI rulings. No source code from any repo is copied in. The short values, recipes and terms quoted here are facts and techniques, credited below.

All 14 repos were read on **2026-10-26** as text only. Nothing from them was installed or run.

| # | Repo | Commit | Licence | What we took |
|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 28b3b8dee8c9 | MIT | WCAG 2.2 rules with platform-specific target sizes, component resilience rules (chips, long tokens, live badges, essential truncation), the error-summary contract, chart "when not to use" thresholds, the pre-delivery checklist idea. **Dropped:** its style, palette and font catalogs (they push glassmorphism, dark dashboards and stock indigo). |
| 2 | VoltAgent/awesome-design-md | 3b605329240c | MIT | How specific a good DESIGN.md is (every colour has a role and a prohibition, exact shadow strings, weight ceilings, Known Gaps). **Dropped:** the brand files themselves; never clone another brand. |
| 3 | nexu-io/open-design | 26d60298f812 | Apache-2.0 | The anti-slop list with exact hex values, the accent budget (about 2 uses per screen), action economy, never lowering contrast on hover, the 5-state coverage rule, loading thresholds, retry escalation, the critique loop against rubber-stamping (cite evidence, score the worst band). Its craft notes credit refero_skill (MIT). |
| 4 | Leonxlnx/taste-skill | 12af471f627f | MIT | Measured numbers from 23 real product screens (sidebar, rows, KPIs, charts, tables, forms, density, phone), data-honesty rules, one question/one finding, the generated-dashboard tells, copy bans. |
| 5 | pbakaus/impeccable | 414603bf14c7 | Apache-2.0 | Operate/Persuade/Read modes, "earned familiarity", the craft floor, the harden checklist (including Persian/RTL), browser-surface theming, Nielsen and cognitive-load rubrics, P0–P3 severities, the slop detector's rule names. (Also installed separately as a plugin.) |
| 6 | DavidHDev/react-bits | e12c22192ac7 | **MIT + Commons Clause** | Only a "when to use" entry. **Never copy its source into anything we distribute.** |
| 7 | emilkowalski/skills | 2d228630ba14 | MIT | The frequency gate, easing tokens, duration table, press and popover recipes, interruptibility, the animation performance tiers, the break-ui worst-case catalog, library picks, the mobile floor. (Most are also installed individually.) |
| 8 | Nutlope/hallmark | 7ec868225c6c | MIT | The Floor/Reflex/Finish tier model with written waivers, the 8-state control contract, the field recipe, undo over confirm, silent success, tooltip timing, z-index and spacing scales, concentric radii, the fake-send ban, the eyebrow test. **Dropped:** forced variety between builds, its banned-font list for product UI, the em/en-dash ban. |
| 9 | google-labs-code/design.md | 6e5da5382f41 | Apache-2.0 | The DESIGN.md format: front-matter tokens, section order, component props, the linter's rules. |
| 10 | magicuidesign/magicui | efe76fc5755e | MIT | The product-safe allowlist; "1 core + 1 supporting effect", auto-scroll pauses. |
| 11 | greensock/gsap-skills | aed9cfd32777 | MIT | GSAP cleanup and ScrollTrigger rules for the rare times GSAP is used. **Dropped:** "GSAP as default", reduced motion as `duration: 0`. |
| 12 | oso95/scroll-world | 71cc36d3bb15 | MIT | Only a "when to use" entry (it needs paid generation and downloaded CLIs). |
| 13 | DavidHDev/canvas-ui | a04a99b23529 | **MIT + Commons Clause** | Only a "when to use" entry. |
| 14 | enesozturk/dimensional-drawing | 5c457437c8c8 | MIT | The discipline of surveying every instance, never inventing a value, and marking unknowns `[TBD]`; its use as a spec and review tool. |

## Contradictions we settled (and why)

| Topic | Sources disagree | House rule | Why |
|---|---|---|---|
| Motion cap | 300ms (Emil) vs 420–500ms for drawers and modals (hallmark, impeccable) | 300ms cap in product UI | Product screens are used all day; slower motion reads as lag |
| Exit easing | ease-in for exits (hallmark) vs never ease-in (Emil, taste, open-design) | ease-out, shorter | Ease-in feels sluggish at the moment the user is waiting |
| Reduced motion | `duration: 0` (GSAP, design.md) vs gentler fades (Emil, impeccable) | Keep ≤200ms fades, drop movement | State changes still need feedback |
| Body size | 16px minimum (hallmark) vs 14px cells (taste) | 14px UI, 16px prose and inputs | Density for tables; no iOS input zoom |
| Fonts | Inter/system banned (hallmark, impeccable detector) vs fine for product (impeccable operate, taste app) | Keep the project's face; the tell is the combination, not the font | Changing fonts in a shipped product is churn |
| Thin lines | ban (taste pages) vs 1px lines are fine (taste app, hallmark) | 1px card edges and row rules allowed | The ban is about marketing pages |
| Input edge contrast | #e5e7eb (taste) vs ≥3:1 (hallmark, impeccable, WCAG 1.4.11) | ≥3:1 | Accessibility floor |
| Navigation | top bar by default (hallmark) vs labelled sidebar (taste) | Left sidebar | Owner's dashboard standard |
| IDs in mono | yes (taste) | Body face | Owner rejected monospace values |
| Middle dots, dashes | banned (hallmark) | One separator in data sublines; en dash for ranges | Correct typography; no dot-chains in headings |
| Pie/donut | never (hallmark) vs thin ring OK (taste) | Thin ring for 3–5 parts only; never a fat donut or gauge | Middle ground |

## Owner rulings folded in

These come from one product owner's standing rulings, given over months of UI reviews:
- UI must read as written by a person: plain words, one accent, values in the body font, a shared status said once.
- "Redesign" means refine today's screen, not restructure it.
- A whole-page mockup is approved before any big build.
- Pages are composed, not stacked: steps bar on top, two columns, the primary action pinned once.
- Verify by clicking and looking at screenshots, never by reading the code alone.
- No niche words hard-coded into the UI; they come from the user's settings.
- Never download a new tool just to check a screen.
- A repo's own rules win over a skill.

## Credits and licences

- This skill's text is MIT (see the LICENSE in the folder above).
- It restates ideas, numbers and techniques from the 14 repos above in its own words, and credits each one. impeccable, open-design and design.md are Apache-2.0; the rest are MIT.
- No code from React Bits or Canvas UI (MIT + Commons Clause) is included; the skill only says when to use them.
