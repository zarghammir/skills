# Components: states, recipes, libraries, sources

## The eight states of every control

| State | Rule |
|---|---|
| Default | Meets contrast. Its edge is ≥3:1 if it is an input. |
| Hover | **One** signal (a background or border step), inside `@media (hover:hover) and (pointer:fine)`. Never lowers text contrast. |
| Focus | `:focus-visible` ring, instant, 2px, ≥3:1, offset 2px. |
| Active | Pressed: `scale(0.97)` or a 1px drop, on pointer-down. Must not shift the layout. |
| Disabled | Native `disabled` attribute + `opacity: .5` + `cursor: not-allowed` + **a visible reason** (one shared line, not one per row). It must look inert, not just be inert. |
| Loading | Inline spinner or label change. The control's width does not jump. It is disabled while the request is in flight, so nothing can be submitted twice. |
| Error | Border + message + `aria-invalid`. Never colour alone. |
| Success | Only from a real server answer. Silent where the effect is already visible. |

- Precedence when states overlap: disabled > loading > active > focus > hover.
- Read-only looks different from disabled.

## Recipes

- **Buttons:**
  - Size to content with a `min-width`, never a fixed `width`.
  - Heights: 32 (sm), 36 (default), 40 (lg); 44 on touch. Icon size 16.
  - **One button shape and one icon style per product.**
  - Label = verb + object ("Approve storyboard", "Export CSV").
  - Set an explicit `type` on every `<button>`.
- **Fields:**
  - The border never changes width between states. The focus ring is a separate `outline` (reserve a transparent one at rest), so nothing shifts.
  - Reserve about 24px at the right edge for a clear, error or spinner icon.
  - The helper line has `min-height: 1lh`; an error replaces it, so the layout doesn't jump.
  - The placeholder shows a format ("name@company.com"), never an instruction.
  - Submit is disabled only while a request is in flight. A failed submit focuses the first invalid field.
- **Overlays:**
  - A **modal is the last answer**, after inline editing and disclosure.
  - Use native `<dialog>` with `showModal()` and `inert` behind it, or a Radix/Base UI Dialog.
  - Close on Escape, on a backdrop click and with a visible close control. First focus goes to the first interactive element; focus returns to the trigger on close.
  - Menus and popovers render in a portal or the top layer, **never inside an `overflow: hidden` ancestor** (they get clipped).
  - Confirm before dismissing a sheet that has unsaved edits.
- **Tooltips:**
  - Render in the DOM (a Radix Tooltip), never the native `title` attribute: it can't be screenshotted, styled or reached by keyboard.
  - Hover delay 500–700ms; keyboard focus shows it at once. It stays open while hovered (WCAG 1.4.13).
  - Never hide essential information only in a tooltip.
- **Toasts** (Sonner):
  - Mount one `<Toaster />` at the root, with `theme` following the app theme.
  - **Use toasts for failures and for effects the user can't see.** When the change is visible on screen, add no "Saved!" toast.
  - Auto-dismiss in 4–5s. Pause on hover and focus. Use `role=status`.
  - Undo toasts last 5–10s.
- **Undo over confirm:**
  - Reversible actions run at once and offer Undo.
  - Irreversible ones confirm by naming the object; for high-stakes deletes, ask the user to type the object's name.
- **Optimistic updates:** apply at once, roll back on failure, and show "Couldn't save — Try again".
- **Search:** debounce 250ms. Echo the query in the no-results state. Treat Persian ی/ي and ک/ك as the same letter.
- **Copy buttons:** show "Copied" for about 2s.
- **Chips and tags:**
  - Wrap before shrinking.
  - Overflow becomes an operable "+3" that opens the full list.
  - Don't make every pill clickable; static labels stay static.
- **Long values:**
  - `overflow-wrap: anywhere` for emails and URLs (never `word-break: break-all`).
  - `min-width: 0` on flex and grid text columns.
  - `flex-shrink: 0` on avatars, icons, badges and trailing actions.
  - `white-space: nowrap` on badges.
- **Truncation policy:**
  - Wrap identifying text (two lines is fine).
  - End-truncate secondary metadata, with the full value one hover or tap away.
  - Middle-truncate file names, paths and hashes.
  - **Never truncate numbers, amounts, dates or anything being compared.**
- **Images:** set `aspect-ratio` or fixed dimensions so nothing shifts. `object-fit: cover` only for decorative crops. On error, fall back to initials, computed from grapheme clusters (`Intl.Segmenter`) so emoji names don't break.
- **State in the URL:** filters, tabs, sort and page live in the URL, so Back and sharing work.

## Library picks (React/Next)

Check `package.json` first. If a competing library is already installed, use it and don't churn. Recommend one library, not a menu.

| Need | Use |
|---|---|
| Components and theming | **shadcn/ui** (the project's own registry) on Radix or Base UI primitives |
| Dialog, popover, menu, select | Radix or Base UI, never a hand-built `<div>` dropdown |
| Command menu | cmdk (no open animation) |
| Toasts | Sonner |
| OTP input | input-otp |
| Animation beyond CSS | motion |
| Animated number (only where the change is the point) | NumberFlow |
| Dashboard charts | recharts, with animation off |
| Drag and drop | dnd kit (always with a keyboard/button alternative) |
| Virtualised lists (1,000+ rows) | react-virtuoso |
| Theme without flash | next-themes |
| Class variants | cva + clsx |

If the repo's AGENTS.md says otherwise (e.g. native `<select>` on phones), **the repo wins**, and the PR body says so.

## Effect and component sources

| Source | Licence | Product UI | Marketing pages | Notes |
|---|---|---|---|---|
| **shadcn/ui** | MIT | Default | Yes | Copy-in components; we own them after install |
| **Magic UI** (magicui.design) | MIT | Allowlist only: number-ticker (one KPI change, once), animated-circular-progress-bar, animated-list (activity feed), file-tree, code-comparison, script-copy-btn, blur-fade (one subtle entrance), scroll-progress, avatar-circles, static dot/grid patterns for empty states | Up to 1 core effect + 1 supporting effect per viewport | Only about 5 of its components handle reduced motion; **wrap each one in a reduced-motion guard**. Customise via props or a wrapper, not by editing the source. |
| **React Bits** (reactbits.dev) | **MIT + Commons Clause** | Rarely: Stepper, CountUp, AnimatedList, HoldButton (hold-to-confirm) after a keyboard and screen-reader check | Yes | Fine inside our apps. **Never copy its source into anything we distribute** (a public skill, a published package, a template). Most backgrounds pull in WebGL/three (100KB+). |
| **Canvas UI** | **MIT + Commons Clause** | No | One-off experiments only | Uses an experimental browser API and the GPU; same distribution restriction |
| **GSAP** (+ ScrollTrigger) | Free (public npm) | Rarely: a real timeline or SVG need | Scroll storytelling | Cleanup rules in [motion.md](motion.md) |
| **scroll-world** | MIT | No | A hero only, with owner approval and the cost stated first | Needs paid video generation and downloaded CLIs, which many teams block on their machines |
| **dimensional-drawing** | MIT | As a spec or review tool (component anatomy sheet) | Docs and launch films | No runtime footprint. Its "survey every instance, never invent a value, `[TBD]`" discipline is house discipline. |

**Banned in product UI from any library:**
- shimmer, rainbow or pulsating buttons
- gradient, aurora or sparkle text
- border-beam, glow or neon cards
- meteors, particles, globes, marquees
- text scramble or typewriter effects
- custom cursors
- bento grids of glowing tiles
- AI-chat chrome (prompt bars, "thinking" lines) used as decoration

These are the signature of a templated AI landing page.
