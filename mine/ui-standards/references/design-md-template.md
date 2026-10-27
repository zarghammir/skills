# DESIGN.md: the per-project design contract

Every product that ships UI keeps one `DESIGN.md` at its repo root, in Google's format (github.com/google-labs-code/design.md; spec version `alpha`).

- Agents read it **before** touching UI.
- It wins over this skill wherever the two disagree.
- If a project has no DESIGN.md, write one in this shape from the shipped UI. Derive the values from the code and the rendered screens, never from intentions. Show it to the owner before relying on it.

## How the format works

- **Tokens** are YAML front matter between `---` lines (or fenced `yaml` blocks under each section). **Prose** sits under `##` headings.
- **Tokens are the normative values.** Prose explains intent. When they disagree, the tokens win and you fix the prose.
- **Token values:**
  - Colours are hex `#RRGGBB`.
  - Dimensions are `px`, `em` or `rem` only.
  - `lineHeight` is unitless.
  - References look like `{colors.primary}`.
  - A component may reference a typography token.
- **Component props** have 8 standard keys: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Variants are sibling keys, for example `button-primary-hover`.
- **Section order** (sections may be skipped): Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Extra sections go after these (Motion, States, Responsive Behavior, Known Gaps).
- **Contrast checking:** a linter checks it only between colours paired inside a component. Give every component both `backgroundColor` and `textColor`, and reference every colour from at least one component.
- **The linter** is `@google/design.md lint DESIGN.md`. Run it only if the project already has the package as a dev dependency; don't `npx` a new download. Otherwise run the checklist at the end of this file by hand.

## Writing rules

1. **Open with one specific reference, not adjectives.** "A bank statement a careful accountant trusts" steers a model; "modern, clean, premium" gives you the generic middle.
2. **Give every colour a role and a prohibition.** Example: "**Ink** `{colors.ink}` #1c1f23: body text. Never pure black."
3. **Count the accent's uses:** "one filled primary button per view", "accent only on: primary action, focus ring, active nav, the main data series".
4. **Give exact values:** shadow strings, control heights, weight ceilings, touch targets, fallback fonts.
5. **Document every state of every component:** hover, focus, active, disabled, loading, error, empty. Brand files almost always miss these.
6. **Never invent a value.** Write `[TBD]` and list it under Known Gaps.
7. **Keep Do's and Don'ts to 6–12 deliberate lines, each with a reason.** A long Don'ts list means the Overview was too vague.
8. **Never copy another brand's identity.** The brand DESIGN.md collections (awesome-design-md) are examples of how specific to be, not templates.

## Template

```md
---
version: alpha
name: <Product>
description: <one sentence: a SPECIFIC reference object + who uses it>
colors:
  primary: "#..."        # the ONE accent: primary action, focus ring, active nav, main data series
  on-primary: "#ffffff"
  ink: "#..."            # body text; near-black, never #000000
  ink-muted: "#..."      # secondary text; ≥4.5:1 on canvas AND surface
  canvas: "#..."         # page ground
  surface: "#..."        # cards and panels
  line: "#..."           # 1px card edges and row rules (decorative)
  control-border: "#..." # input/control edges; ≥3:1 against surface
  positive: "#..."       # text-safe green (≥4.5:1)
  negative: "#..."       # text-safe red  (≥4.5:1)
  warning: "#..."
typography:
  title:    {fontFamily: <face>, fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.01em}
  heading:  {fontFamily: <face>, fontSize: 16px, fontWeight: 600, lineHeight: 1.4}
  body:     {fontFamily: <face>, fontSize: 14px, fontWeight: 400, lineHeight: 1.45}
  prose:    {fontFamily: <face>, fontSize: 16px, fontWeight: 400, lineHeight: 1.55}
  label:    {fontFamily: <face>, fontSize: 12px, fontWeight: 500, lineHeight: 1.35}
  numeric:  {fontFamily: <face>, fontSize: 14px, fontWeight: 400, lineHeight: 1.45, fontFeature: tnum}
rounded: {chip: 4px, control: 6px, card: 8px, dialog: 12px, full: 9999px}
spacing: {xs: 4px, sm: 8px, md: 12px, lg: 16px, xl: 24px, xxl: 40px, section: 64px}
components:
  button-primary:       {backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.label}", rounded: "{rounded.control}", height: 36px}
  button-secondary:     {backgroundColor: "{colors.surface}", textColor: "{colors.ink}", rounded: "{rounded.control}", height: 36px}
  input:                {backgroundColor: "{colors.surface}", textColor: "{colors.ink}", rounded: "{rounded.control}", height: 40px}
  card:                 {backgroundColor: "{colors.surface}", textColor: "{colors.ink}", rounded: "{rounded.card}", padding: 20px}
  status-positive:      {backgroundColor: "#...", textColor: "#..."}   # pale tint + dark same-hue text
  status-negative:      {backgroundColor: "#...", textColor: "#..."}
---

# <Product>

## Overview
<The specific reference. Who uses it, how often, on what device. Mode: Operate / Persuade / Read.
Density: dense / medium / sparse. Two or three lines on the feel, with no adjectives that fit every product.>

## Colors
<Each token: name, hex, role, where it is NOT allowed. Ground model: e.g. white cards with 1px line on a #f9fafb canvas.
Dark mode: derived values (never inverted), ground L 10–14%, no navy or slate.>

## Typography
<Family + fallback stack. Hierarchy table: Token | Size | Weight | Line height | Tracking | Use.
Weight ceiling (e.g. 600). tabular-nums on every number column; confirm the face's digits change width.>

## Layout
<Base unit 4px. Sidebar width, content max-width, gutter (ONE value). Grid sums written out.
Page anatomy: steps bar on top for multi-step flows; work area in two columns; primary action placement.>

## Elevation & Depth
<Border OR shadow. Resting cards: 1px line, no shadow. Floating layers only (menu, popover, dialog, toast):
the exact shadow string. z-index scale: base 1, raised 10, dropdown 100, sticky 200, modal 400, toast 500, tooltip 600.>

## Shapes
<Radius table + use. Nested: inner = outer − padding. Pills only for status chips.>

## Components
<Per component: anatomy and all states: default, hover, focus-visible, active, disabled (+ why), loading, error, empty.
Buttons, inputs, select, table, card, tabs, dialog, toast, status pill, empty state, skeleton.>

## Do's and Don'ts
- Do … because …
- Don't … because …

## Motion
<Tokens (durations, easing). Max 300ms. What never animates. Reduced-motion behaviour.>

## Responsive Behavior
<Breakpoints table: Name | Width | What changes. Touch targets 44px. Sidebar collapse. Table → two-line rows under 640px.>

## Known Gaps
- [TBD] <anything not yet decided>
```

## Pre-commit check (by hand when the linter isn't installed)

- [ ] Every `{ref}` resolves.
- [ ] `primary` exists.
- [ ] Every colour is used by at least one component.
- [ ] Every component text/background pair is ≥4.5:1, and control edges are ≥3:1.
- [ ] Sections are in spec order, with no duplicate headings or top-level keys.
- [ ] No `TO_FILL` and no invented values; unknowns are `[TBD]` and listed in Known Gaps.
