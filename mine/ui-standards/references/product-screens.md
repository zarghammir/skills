# Product screens (Operate mode)

Operate mode covers dashboards, review and approval screens, tables, forms and settings. The bar is **earned familiarity**: a user who knows the category trusts the screen at once and never pauses at a subtly-off component. The tool should disappear into the task.

Most numbers below come from a measured study of 23 real product screens (taste-skill). Each one is a default, not a law: the project's DESIGN.md wins.

## 1. Before the first pixel

- **One question, one finding.** Name the single question this screen answers ("What needs my approval today?") and the one finding it shows first. The biggest, first-read element answers that question.
- **The most frequent job is one click away.** List the user's jobs by frequency before you lay anything out.
- **Design the page as a whole.** Never build it section by section from the API's shape; that is how screens turn into a stack of full-width boxes.
- **Inventory the real data:** fields, their limits, which are optional, the real count ranges. Design for the real data, not for lorem.

## 2. Page anatomy (owner standard)

- **App shell = labelled left sidebar.**
  - Width 224–240px, on a neutral or light background. **Never** a dark or saturated sidebar on a light app.
  - Nav rows have a 32px hit area on a 34px pitch. Icons 16px outline (about 1.5px stroke). Labels 14px at weight 400, sentence case.
  - The active item is a neutral grey pill (radius about 8). Group labels are 12–13px grey sentence case, never uppercase.
  - Product mark, name and workspace switcher sit at the top.
  - Nav items lead to other pages, never to anchors on the same page.
  - A count on a nav item appears only on a queue that needs action, and names its noun ("Approvals 3").
- **Dashboard home holds at most three blocks:**
  - today's progress
  - waiting for your approval (count + a button to its page)
  - spend this month or one key metric

  Everything else gets its own page (library, history, settings).
- **Multi-step work pages** (make, review, approve):
  - A **steps bar on top**.
  - A **two-column work area**: the thing being worked on on one side (the script, the document, the storyboard), with evaluation, suggestions and controls beside it.
  - **Compact secondary sections** (claims, checks, metadata) that are not full width.
  - **The primary action appears once, in a pinned (sticky) header,** with its price breakdown beside it if it costs.
  - **Every action appears once on the page.** An edit control sits next to the thing it edits. Never repeat a button "for convenience".
  - **Each step shows only its own sections.** A later step doesn't repeat an earlier step's content; for example, the Video step doesn't show the script again.
  - **Destructive controls are small**, placed next to what they affect, never the first full-width section.
- **Every suggestion or recommendation has an action** (Apply, Use this). If it costs money, show the price on the button or right beside it. A suggestion with no way to act on it is a dead end.
- **Approve once.** One Approve for the whole set. Per-item approval only when the items really are decided separately.
- **Show progress in context.** A page that stacks full-width sections top to bottom with no steps bar is a must-fix.

## 3. Canvas and grid

- Content padding 24–32px on desktop (16–20 on phone), or a centred column of 1088–1208px.
- **One gutter value** for both horizontal and vertical gaps (16 is the usual).
- **Grid arithmetic must close.** Write the sum down, e.g. 3×372 + 2×16 = 1148.
- Cards in one row share a bottom edge. Any empty band over 40px inside a card is a defect.
- Choose the column count from the number of items: no orphan cell on the last row, no stretched blank card.
- A narrow table (≤5 columns or ≤6 rows) caps at about 760px and pairs with the next block instead of stretching.
- **Tables before cards.** Uniform records go in a table; cards are for things that are each interactive on their own.
- **Density**: row pitch, padding and type size move together.

| Density | Data points | Rows |
|---|---|---|
| Sparse | 6–25 | 56–92px |
| Medium | 25–50 | 44–56px |
| Dense | ~120 | 13px body, 28px list rows, 40–42px table rows |

  Placed space reads calm; leftover space reads unfinished.

## 4. Page title and actions

- Exactly one h1, 20–28px at weight 600. It is a noun ("Approvals", "Overview"); never "Welcome back", never an emoji.
- An optional 14px grey second line about the **data** (the period, the finding), never about the interface.
- **One primary (filled) action per view.** Everything else is secondary, ghost or a link with different wording.
  - Never two filled buttons side by side.
  - Never two solid buttons for the same action in one viewport.
- Date range lives at page level **or** per card, never both. Control height 32–36px.
- Export, Share and the date picker don't all cluster by the title; put each where it acts.

## 5. Numbers and KPIs

- **Default KPI row:** one container split by 1px dividers, with the label above the value.
  - Value 20–32px, about 1.7× the label. The "answer" figure may be 30–36px. **Nothing at 48px or more.**
  - **No icon in a coloured circle, no sparkline on the tile, no tinted tile background, no brand-coloured value.**
- Units are a smaller grey suffix ("5 min").
- **Deltas** are 12–14px and name their window ("vs last 30 days").
  - Colour shows **good or bad, not up or down**: a rise in latency is bad.
  - A zero change is grey. A change from zero is written "+4 (new)".
- **Tabular figures** (`font-variant-numeric: tabular-nums`) on every number that is compared, aligned or updated. Use the body face; don't switch to monospace. Check that the face's digits actually change width with the setting.
- Fixed decimals per metric: money 2, percent 1–2, counts 0. Thousands separators. A sign on every change. Format with `Intl.NumberFormat`, plurals with `Intl.PluralRules`. **Never render `NaN`, `undefined` or `null`.**
- **Data honesty:**
  - A fact shown twice is one variable.
  - Totals are computed from the rounded values as displayed (£21.68 + £8.34 − £3.81 must show £26.21).
  - Every relative figure names its baseline.
  - No invented metrics, Acme, John Doe or round vanity totals. If a value is unknown, show an honest "—", not a plausible fake.

## 6. Charts

- **Pick the form:**

| Data | Form |
|---|---|
| One value | A stat |
| 2–5 values | A stat row or horizontal bars |
| A time series | A line |
| More than ~7 categories, or more than 15 bars | A table |
| Parts of a whole | A stacked horizontal bar, or a thin ring (3–5px) for 3–5 parts with no slice labels |

  **Never a fat donut, a gauge, a 3D chart or dual axes.**
- **One series per chart, three at most.** Switch metrics with a control instead of overlaying them.
- **Plots are 120–260px tall**, styled like this:
  - 3–5 faint **solid** gridlines, no y-axis line.
  - 4–7 round ticks (12px grey), the top tick above the maximum.
  - A zero baseline for bars and counts. A zoomed axis must say so.
  - 4–8 x-labels, never rotated.
- **Marks:**
  - Lines are 2px, straight segments, no smoothing, no dot on every point.
  - Fill under a line: none, or a tint of 14% or less, and never a gradient.
  - Bars are square, or have at most a 4px top radius.
- **Colour:**
  - One hue per chart, placed on the main data element (this can be the product's accent).
  - Multiple series use a lightness ramp of that hue, not a rainbow.
  - A screen with more than about 4 hues is a warning.
- **Legend and labels:**
  - No legend for a single series. Otherwise at most 5 items, with each swatch drawn as the mark itself.
  - Annotate the event that matters ("Deploy a3f0").
  - A forecast is dashed after "today". Labels never collide.
- **Accessibility:**
  - Data marks ≥3:1 against the background. Data labels ≥4.5:1.
  - Colour is never the only signal.
  - Offer a table view or a one-line summary of the insight.
- **Turn chart animation off** for analytic charts (recharts `isAnimationActive={false}`).

## 7. Tables

- **Rows:**
  - 40–48px tall; two-line rows with media 56–72px.
  - The header is 12–13px grey sentence case, with **no fill band, no zebra striping and no uppercase**.
  - Row rules are 1px, a step lighter than the card edge.
- **Columns:**
  - The identity column takes ⅓–½ of the width.
  - **Numbers are right-aligned, in tabular figures.**
  - A missing value is a grey "—"; a real zero is printed as 0.
  - The sign lives in the text, not only in the colour; don't paint every negative red.
- **Status:**
  - At most **one status mark per row**: a pale-tint pill with dark text of the same hue (e.g. `#dcfae5` / `#04250e`), 20–24px tall, text ≥11px at 500, `white-space: nowrap; flex: none`.
  - **If every row has the same status, say it once in the header instead.**
- **Row actions:**
  - None, or one overflow menu.
  - A row that needs doing gets a visible text action in a fixed column, not a hover-only icon.
- **Length:**
  - An overview shows 4–6 rows plus "View all (1,284)", with no pagination.
  - A full list shows "1–50 of 1,284" with a sticky header. Filters, sort and page live in the URL.
- **IDs and hashes:** body font, middle-truncated, with a copy button. Never truncate amounts, dates or anything being compared.

## 8. Forms and settings

- **Fields:**
  - The label sits above the field, 14px at weight 500. No floating labels, and no placeholder standing in for a label.
  - Inputs are 36–40px tall (44px on touch), radius 6–8, and their **edge is ≥3:1** against the surface.
  - Spacing: 24px from the description to the first field, 16px between fields, 24px to the actions.
- **Validation:**
  - Validate on blur once the field has been touched, then on every input while it's invalid. Async checks are debounced 250–500ms and never block typing.
  - Errors sit under the field, linked with `aria-describedby`.
  - After a failed submit, focus moves to the first invalid field (or to a linked error summary when there are several). Inline errors stay in place.
- **Saving:**
  - **One save model per view:** autosave with a "Saved" stamp, OR one Save per panel.
  - Settings use a label column of about 360–450px beside a control column; sections are split by 1px rules with 32px of space.
- **Toggles:**
  - "On" is shown in near-black or semantic green, not the brand accent.
  - A disabled control stays legible and says why (one shared explanation, not one per row).
- **Destructive actions:**
  - They come last, in their own section, with the consequence written out.
  - **Prefer undo** (5–10s) over a confirmation dialog. When something truly can't be undone, the confirmation names the object, and the confirm button repeats the action ("Delete project"), never "Yes" or "OK".

## 9. States: every data region has all five

| State | Rule |
|---|---|
| Loading | The final layout with flat grey bars at the real size, no shimmer and no layout shift. A refresh keeps the old values and updates a freshness stamp. |
| Empty | Keep the frame and header. Say what goes here and offer one action. Never a bare "No results". An empty chart draws its zero line, with no illustration. Distinguish first use, no results (echo the query), filtered out and no permission. |
| Error | Shown in the block that failed, never as a full-page takeover. State what failed, why if known, and what to do ("Couldn't load payments. Last updated 09:14." + Retry). Keep the user's input. |
| Full | The real data. |
| Edge | The longest real values, 0, 1, a lot, missing optional fields. See [verify.md](verify.md). |

**Loading thresholds:**

| Duration | What to show |
|---|---|
| Under 300ms | Nothing |
| 300ms–2s | A subtle skeleton or spinner |
| 2–10s | A layout-matched skeleton or a labelled spinner ("Loading payments…") |
| 10–30s | A determinate bar plus Cancel |
| 60s+ | Stop animating; show the error with Retry |

Every request has a timeout.

**Retry:**
- The first retry is immediate, then back off 2s, 4s, 8s.
- After 3 failures, show "Contact support" with a copyable error ID.

**First run:** put the first action where the data will appear, and show setup progress at its true percentage. Never collapse an error into an empty state.

## 10. Phone and tablet

- Below 1024px the sidebar becomes a 48px top bar with a sheet, or a bottom bar of 4–5 labelled items. A sidebar over 30% of the width fails.
- Margins 16–20px. Targets ≥44px. Text ≥12px. Inputs 16px so iOS doesn't zoom.
- KPIs become a 2-column grid with an even count. At most one row of controls above a chart.
- **Below 640px, tables become two-line rows:** secondary fields move to line 2 and are never dropped. Otherwise the table scrolls inside its own frame with the first column fixed. **The page itself never scrolls sideways.**
- List and detail panes show one region at a time; Back returns to the same scroll position.
- Tablet (641–1023px) is its own band; design it, don't just shrink the desktop layout.

## 11. Motion on product screens

Motion is for feedback and state only. **Nothing performs an entrance.** No page-load choreography, no count-ups, no hover lift on cards. Values are in [motion.md](motion.md).
