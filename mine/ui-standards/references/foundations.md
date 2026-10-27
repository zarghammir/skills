# Foundations: type, colour, surfaces, space, accessibility

These are the defaults. A project's DESIGN.md overrides any of them.

## Type

- **One family for product UI.** Use the project's existing face if it has one. A second face only with one job: mono for code blocks, or a display face on marketing pages.
- **Choosing a face for new work:**
  - Pick one workhorse sans, e.g. IBM Plex Sans, Public Sans, Hanken Grotesk, Figtree, Onest or Manrope, or the system stack.
  - Inter is fine if the project already uses it. Inter + #f8f8f8 + white 12px cards + no colour on the data is "the kit's own face": the product needs a face of its own (see the anti-slop rules).
  - Always give a fallback stack and set `font-display: swap; font-synthesis: none`.
- **Product scale:** fixed rem steps, ratio about 1.125–1.25, no fluid type.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Page title | 24 (20–28) | 600 | 1.25 |
| Card / section title | 16 | 600 | 1.4 |
| Body, table cells, nav | 14 | 400 | 20px |
| Prose, form inputs | 16 | 400 | 24px |
| Labels, meta | 12 | 500 / 400 | 16px |
| Pills (floor) | 11 | 500 | |

  - Adjacent levels are ≥1.25× apart, or separated by a clear weight jump.
- **Weights:** about 3 per screen (400 / 500 / 600). Use 700 rarely, for one job. Weight jumps; it doesn't step.
- **Tracking:**
  - 0 on body.
  - −0.01 to −0.02em on 24px and up.
  - Display text on marketing pages −0.02 to −0.03em, never past −0.04em.
  - **No tracked-uppercase labels** in product UI. If uppercase is ever used, it needs 0.06–0.1em tracking.
- **Measure:** prose 65ch (45–75). Tables may run wider.
- **Wrapping:**
  - `text-wrap: balance` on headings, `pretty` on body.
  - No one-word last lines in headings.
  - Never justify text.
- **Numbers:** `tabular-nums` on compared, aligned or live figures, in the body face.
- **Typographic details:** curly quotes, real ellipsis (…), en dash for ranges (9–5), and a non-breaking space between a number and its unit.
- **Persian/Arabic (RTL):**
  - Use logical properties (`margin-inline-start`) and `dir="auto"` on user text.
  - Keep ZWNJ.
  - Format digits by locale (`fa-IR`).
  - Use the Jalali calendar where the product needs it.
  - Leave room for 30–40% longer strings in any translation.

## Colour

- **Build roles, not swatches:** canvas, surface, ink, ink-muted, line, control-border, primary (accent), on-primary, positive, negative, warning, info, focus.
  - Name tokens by purpose (`--accent`), never by hue (`--blue-500`).
  - Never write a literal colour outside the token file.
- **One accent.**
  - In product UI it goes only on: the one primary action, the focus ring, the current selection or active nav, and the main data series.
  - Budget: **about 2 visible accent uses per screen**, under about 5% of the pixels. App screens average about 3% coloured pixels in total.
  - No second accent colour. No accent on inactive states.
- **Status colour** is a pale tint with dark text of the same hue, never saturated chips with white text. **Red is a signal, not a texture**: one red mark per object.
- **Contrast** (WCAG 2.2 AA; thresholds are inclusive, so 4.49:1 fails):
  - Body text, **placeholders**, secondary text, error and success text: **≥4.5:1**. `#6b6b6b` on white is about the lightest grey that passes.
  - Large text (≥24px regular or ≥18.5px bold), icons, **input and control edges**, focus rings and chart marks: **≥3:1**.
  - Decorative card edges and row rules may be fainter, because they aren't needed to find a control.
- **Grey text on a coloured surface:** don't. Tint the secondary text from that surface's hue instead.
- **Never lower foreground contrast on hover.** Hover shifts the background lightness by about 0.06–0.12 (OKLCH L) or changes the border. Only the disabled state may lose contrast.
- **Never colour alone:** add text, an icon or a shape.
- **Banned as an accent unless it is truly the brand and defined in DESIGN.md:** stock Tailwind indigo/violet (#6366f1, #4f46e5, #4338ca, #8b5cf6, #7c3aed, #a855f7). The same goes for purple→blue, blue→cyan and indigo→pink gradients, and a cream/beige page with terracotta.
- **Light ground:**
  - Either white cards with a 1px line on a #f9fafb-ish canvas, or grey panels on white. Pick one model per product.
  - Ink near-black (#111–#1c1f23), never #000. Body never pure black on pure white at large sizes.
- **Dark mode:**
  - Derived, never inverted. Ground L 10–14% neutral (#0f0f0f–#171719); **no navy or slate**.
  - Surfaces step lighter by about 3% L per level. Ink about #f0f0f0 (L 93%).
  - Two greys for secondary text at most. Borders `rgba(255,255,255,0.08)`. Shadows off.
  - Accent chroma −0.02 to −0.04, L +5–10. Body weight drops one step (400 → 350) where the face supports it.
  - Status colours become their own hue on a dark tint of themselves.
  - Test both themes separately; never infer one from the other.
  - An inline script reads the theme setting before first paint. Set `color-scheme: light dark`.
- **New palettes:** derive with OKLCH or `color-mix()`, don't invent hex values. Reduce chroma near white and black.

## Surfaces, radius, elevation

- **Border OR shadow, never both** on the same element.
- **Resting cards:** 1px line, no shadow.
- **Shadows** are only for floating layers (menu, popover, dialog, toast). Example: `0 2px 8px rgb(0 0 0 / .08)`, with offset + blur.
  - Never a hard offset shadow (`4px 4px 0`).
  - Never a thin border + wide soft shadow on every card.
- **Elevation levels:** at most three — none, hairline (`0 0 0 1px var(--line)`), floating.
- **Surface ladder:** whitespace → hairline → tinted well → card. Use a card only for content that is interactive on its own. **Never a card inside a card.**
- **Radius:**
  - Pick one tight system: chips 4, controls 6, cards 8, dialogs 12. Full round is only for status pills and avatars.
  - Avoid the 11–16px "everything rounded" default.
  - Nested radii: **inner = outer − padding** (≥2px).
- **No coloured side stripe** (`border-left` over 1px) on cards, alerts or list items. It is the most recognisable AI dashboard tell.

## Space

- **Base unit 4px.** Scale: 4, 8, 12, 16, 24, 32, 40, 64 (add 96 for marketing). A raw length where a token exists is a defect; allow at most a few documented optical nudges.
- **Grouping:** 8–12px within a group, 24–48px between groups.
  - More space above a heading than below it.
  - Large gaps between groups, tight gaps inside them; never the other way round.
- **Padding:** cards 16–24 (median 20). Never under 8px inside any box.
- **Use `gap`** for siblings. DOM order matches visual order.
- **z-index scale:** base 1, raised 10, dropdown 100, sticky 200, sticky-nav 300, modal 400, toast 500, tooltip 600. Nothing outside it.

## Responsive

- **Breakpoints:**
  - Phone under 640px (gutters 16).
  - Tablet 640–1023px (gutters 24, sidebar collapses).
  - Desktop 1024px and up.
  - Test at 320, 390, 768, 1024, 1280 and 1440, plus a wide screen (1920+), where the gutters grow, not the grid.
- **Viewport units:** `dvh` for app shells and `svh` for heroes, never `vh`.
- **No page-level horizontal scroll, ever.** Use `overflow-x: clip` on the page and `min-width: 0` on flex and grid children. Wide content scrolls inside its own frame.
- **Buttons and primary nav never wrap:** shorten the label, then collapse the row.
- **Gate by capability, never by user-agent sniffing:**
  - `(hover: hover) and (pointer: fine)` for hover effects.
  - `(pointer: coarse)` for 44px controls.
- **Mobile floor:**
  - Viewport `width=device-width, initial-scale=1, viewport-fit=cover` + `env(safe-area-inset-*)`.
  - **Never disable zoom** (`user-scalable=no` or `maximum-scale=1`).
  - `touch-action: manipulation`.
  - `-webkit-tap-highlight-color: transparent` with a real `:active` state.
  - `overscroll-behavior: contain` on inner scrollers.
  - The right `inputmode`, `autocomplete` and `enterkeyhint` on every input. Never block paste.

## Accessibility (WCAG 2.2 AA is the floor)

- **Native elements first:**
  - `<button>` for actions and `<a href>` for navigation, never a clickable div.
  - `<dialog>` or the Radix/Base UI primitives for overlays.
  - No invented ARIA, no `tabindex` greater than 0.
- **Focus:**
  - Every interactive element has a `:focus-visible` ring that appears **instantly** (no fade): 2px, ≥3:1, `outline-offset: 2px`, on the accent hue.
  - Never `outline: none` without a replacement.
  - Sticky headers must not hide the focused element (`scroll-padding-top`).
- **Keyboard:** everything works without a pointer, tab order follows visual order, and there are no traps. On route change, focus moves to main.
- **Hit targets:** at least 24×24 CSS px (the legal floor). **House target 44×44** for touch and primary controls; extend small visual controls with a `::before` inset of −12px.
- **Names:**
  - Icon-only buttons have an accessible name.
  - Decorative icons are `aria-hidden`.
  - Meaningful images have alt text.
- **Live updates:**
  - Errors use `role=alert` or `aria-live`.
  - Toasts use `role=status`, appear in one consistent position, and pause on hover and focus.
  - Live regions exist before content is injected.
  - A changing badge announces one atomic message ("3 items in cart"), never a bare number.
- **Drag:** never the only way to reorder, resize or select; offer buttons or a menu too.
- **Zoom and text spacing:** layout survives 200% zoom and user text-spacing changes. Fixed-height boxes never clip text.
- **Theme browser surfaces too:** `::selection`, `caret-color`, `scrollbar-color`, `accent-color`, `text-underline-offset`.
- **AI-generated content** is labelled as such, and never presented as written by a human.
