# Motion

Product motion is feedback, not decoration. On an app screen, nothing performs an entrance.

## 1. Gate before you animate

**How often is it seen?**

| Frequency | Rule |
|---|---|
| 100+ times a day (keyboard shortcuts, command palette, tab or route switch, row navigation, sort, filter, paging) | **No animation.** The state changes instantly. |
| Tens of times a day (hover, list navigation) | Near-imperceptible only: a colour or background step. |
| Occasional (menus, modals, drawers, toasts) | Standard motion, values below. |
| Rare (first run, a finished long job) | One small moment is allowed. |

- Keyboard-initiated actions never animate.
- **Name the purpose** or delete the animation. Valid purposes are feedback, spatial link (where did this come from), state change, and softening a jarring jump. "It looks nice" is not one.
- **Data the user reads never moves for style.** No chart line-draw, no count-up on KPIs, no shimmer bigger than a flat skeleton.

## 2. Tokens (one set per product; extend it, never fork it)

```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);   /* enter/exit, the default */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);  /* things moving on screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);   /* sheets, drawers */
--dur-press: 120ms;   --dur-hover: 150ms;   --dur-tooltip: 125ms;
--dur-menu: 200ms;    --dur-accordion: 200ms;
--dur-modal: 250ms;   --dur-drawer: 300ms;
```

- **Hard cap: 300ms** for any product UI motion.
- **Exits run at 60–75% of the entrance.** They use the same ease-out curve, never ease-in.
- `linear` is only for progress bars, spinners and hold-to-confirm fills.
- **Never use `ease-in` on UI.** Don't hand-roll near-duplicate cubic-beziers; use the tokens.

## 3. How things move

| Element | Recipe |
|---|---|
| Press (every pressable) | `:active { transform: scale(0.97) }`, 120ms `--ease-out`, fires on pointer-down |
| Popover / dropdown / menu | opacity + `scale(0.95)` → 1, 200ms, `transform-origin: var(--transform-origin)` (Radix/Base UI), so it grows out of its trigger |
| Tooltip | from `scale(0.97)`, 125ms. First hover after a 500–700ms delay; neighbours in the same toolbar open instantly. On keyboard focus, show it at once. |
| Modal | `scale(0.96)` → 1 + opacity, 250ms, centred; backdrop fades in step with it |
| Drawer / sheet | `translateY(100%)` or `translateX(100%)` → 0, 300ms `--ease-drawer` |
| Accordion | height via `grid-template-rows: 0fr → 1fr` (or measured px), 200ms. Never animate to `auto`. |
| Toast | Use the library default (Sonner). Toasts are only for failures and effects the user can't see happen. |
| Tab indicator | transform only, 200ms `--ease-in-out` |
| Live number update | update in place; an optional crossfade ≤200ms. Never count up on load. |

- **Never `scale(0)`.** Start at 0.95 plus opacity 0.
- On popovers, never use a pure fade with no initial transform.
- Exit along the path you entered.
- **Interruptible:** use CSS transitions (they retarget mid-flight) for anything that can re-trigger, not `@keyframes`. Use `@starting-style` for mount entry. Never lock input during a transition.
- **Springs are only for real drag surfaces:** `{ type: "spring", bounce: 0, duration: 0.4 }`, with `bounce: 0.2` only after a flick. Dismiss on velocity above about 0.11 px/ms or on distance.
- **Stagger** is only for a first-load group seen occasionally: at most about 5 items, 40ms steps. Never on re-renders, filters or pagination, and it must never block clicks.
- **No bounce, elastic or overshoot easing** on menus, modals or popovers.

## 4. Properties and performance

- **Only `transform` and `opacity`** (and `clip-path` where browser support is OK). Exceptions: accordion height, and the width of an absolutely positioned indicator that has no children.
- **Never `transition: all`.** Name each property.
- Swap layout properties for transforms: width/height → `scale`; top/left/margin → `translate`; display → opacity; animated box-shadow → `filter: drop-shadow`.
- No React `setState` per frame. Write to `ref.current.style.transform`, or use a motion value.
- Don't drive a child's transform from a CSS variable on its parent, because it re-styles the whole subtree.
- Anything that plays during navigation, fetching or hydration uses CSS or WAAPI. If you use Motion, pass a full `transform` string; the `x`/`y` shorthands run on the main thread.
- Keep animated blur to 2–5px, and never over 20px.
- Use `will-change` only after you have seen a 1px shift or measured dropped frames, and only on the element that animates.
- Virtualize lists over about 1,000 rows.
- Budget 8ms a frame on a mid-range phone at 120Hz, not "smooth on my MacBook".

## 5. Accessibility ships with the animation

- `prefers-reduced-motion: reduce` means fewer and gentler, not zero. Keep opacity and colour fades of 200ms or less; drop all translate, scale and overshoot. Never use a global `0.01ms` kill switch that also kills state feedback.
- Put hover effects inside `@media (hover: hover) and (pointer: fine)`. Hover may change colour or background only; no hover lift or scale on cards. **No action may be reachable only by hover.**
- Pause auto-moving content on hover and focus. Anything that moves for more than 5s needs a pause control.
- If you use translucency, also handle `prefers-reduced-transparency` (solid background) and `prefers-contrast: more`.

## 6. Tool ladder (cheapest first)

1. CSS transition (hover, press, class toggle)
2. `@starting-style` (mount entry)
3. CSS animation, then WAAPI
4. **Motion**, for springs, layout animation, exit animation and gestures

For a whole component (toast, drawer, command menu, select), use the library ([components.md](components.md)), not a hand-built animation.

**GSAP** is only for real timelines, SVG morph or draw, or scroll storytelling on marketing pages. GSAP's own skills call it "the default for React"; that is vendor bias, so ignore it. If you do use it:
- Clean up with `useGSAP(() => …, { scope })`, and wrap later callbacks in `contextSafe`.
- Use `gsap.matchMedia()` with a `reduceMotion` condition that gives gentler motion, not `duration: 0`.
- Put a ScrollTrigger on the timeline, never on a child tween. Never combine `scrub` with `toggleActions`.
- Call `ScrollTrigger.refresh()` after fonts and images load, and kill triggers on route change.
- Set `gsap.defaults({ duration: 0.2 })` with a `CustomEase` of `.23,1,.32,1`.

## 7. Never on product screens

Leave these off product screens. Some may appear on marketing pages, with care:
- scroll reveals, parallax, pinning or scrubbing, fake horizontal scroll
- SplitText, typewriter, scramble or marquee text
- ambient loops (float, pulse, orbit), pulsing "live" dots, 3D tilt, mouse-follow effects
- route or page transitions, sliding tab content, shared-layout animations on navigation
- glass or "materialize" blur-ins
- confetti; the only exception is one rare moment, such as a first video published
- sound, or haptics on the web
- Lottie for UI state

## 8. Feel-check

- Watch it at 2–5× slower, then at real speed.
- Try it on a real phone.
- Interrupt it (click again mid-animation).
- Turn on reduced motion.
- Report findings as one table: `| Before | After | Why |`.
