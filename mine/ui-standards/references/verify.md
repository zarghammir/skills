# Verify: click it, look at it, break it

Passing tests prove the code *can* draw a screen. Only looking proves what it is like to use. A screen counts as verified only when someone has **seen** it in the states that matter.

## 1. Click and look

- **Click every control you changed:** open states, hover and expanded variants, Escape and outside-click to close menus, the keyboard path (Tab, Enter, Space, Escape).
- **Screenshot each result and read the whole frame** before checking the claim you were testing. First sweep the frame with no question in mind, then check the claim. A screenshot offered as evidence for one thing must not silently pass over another defect in the same frame. Clipped breadcrumbs, a disabled control that looks live, and a sentence repeated on every row all hide in frames that "passed".
- **Check geometry, not just existence.** Use `getBoundingClientRect()` to confirm the element sits inside the viewport and is not clipped by an `overflow: hidden` ancestor. A dropdown can exist in the DOM and still be invisible.
- **Assert which page each screenshot came from** (URL or heading). A screenshot of the wrong page is still a valid PNG.
- **A string change is reviewed by rendering it with real values.** The diff shows the template; only the page shows what it reads like with a long name inside it.
- **Native `title` tooltips can't be captured.** Use a DOM tooltip, and assert both its accessible name and its accessible description.
- **Never hand over a screenshot you haven't looked at.**

## 2. Viewports and modes

At minimum:
- **390** (phone)
- **768** (tablet)
- **1280** (laptop)

Add these where relevant:
- 320 (smallest)
- 1440 / 1920 (wide)
- light **and** dark
- 200% zoom
- `prefers-reduced-motion`
- RTL (`dir="rtl"`) for any product that may ship Persian or Arabic

## 3. Tools, in order of preference

1. **The project's own Playwright.** Use the `playwright-cli` skill or the repo's e2e setup. Follow the project's machine rules: some teams share one browser slot between agents. Wait for it rather than running outside it.
2. **Without a browser run (between turns), for a static page or prototype:**
   1. Load the page in jsdom and click through to the state you want.
   2. Write out `document.documentElement.outerHTML` next to copies of the CSS.
   3. Render it with macOS Quick Look: `qlmanage -t -s 1400 -o <out> <file>.html`. For phone width, render a wrapper page with `<iframe width="390">`.
   4. Report the result as "looked at via Quick Look", never as a browser screenshot. It is static (no hover or focus) and uses local fonts.
3. **Never download a new tool to verify.** No `npx some-cli`, no new browsers or binaries. Use what the project already has (`./node_modules/.bin/…`).

## 4. Break it (worst-case data)

Run this on every list, table, card or form screen. Change the data at the fixture, props or API boundary, never by editing the markup. Keep the fixture as a regression test.

| Area | Values to try |
|---|---|
| Names | `Aleksandra Wiśniewska-Kowalczyk`; `Christopher Alexander Montgomery III`; `Jo`; `王秀英`; `نور الهدى عبد الرحمن` (needs `dir="auto"`); `Đặng Thị Ngọc Hân` (diacritics clipped by tight leading?); `👩🏽‍💻 Priya` (initials from grapheme clusters); missing name (email only) |
| Identifiers | `bartholomew.fitzgerald@northwind-industries-holdings.example.com`; a long URL with a query string; a UUID; `Q3 Board Deck — FINAL (revised) v12 [approved by legal].pdf` |
| Labels | `Benachrichtigungseinstellungen` (30-character German compound); French at +30% length; 12 tags (needs `+8`); an empty or whitespace title; `<script>alert(1)</script>`, `&amp;` and `**bold**` (escape once, render as text); a 2,000-character paste; an embedded newline |
| Numbers | 0 (division by zero, empty meter); 1 (plural); 1284 (needs a separator); 1,000,000 (compact form?); `$12,345,678.90`; −42.5; 142% and −3% (meters out of range); null, undefined and NaN (never rendered); a live 99 → 100 change (tabular figures) |
| Collections | 0, 1, exactly the page size, page size + 1, 1,000+ (virtualise or paginate), one item 10× bigger than the rest, duplicate names |
| Time | now ("just now"), 12 days / 11 months / 3 years ago (absolute date after about a week), a future date, `1970-01-01`, a timezone day-shift (`2025-12-31T23:30:00-08:00`) |
| Media | a 404 avatar, no avatar, 4000×200 and 200×4000 images, a dark logo in dark mode, a slow image (no layout shift) |
| States | loading (the skeleton matches the layout), API error (no raw `TypeError` on screen), partial data, every enum value in one list, no permission (disabled actions keep the layout and say why), the current user in the list ("You") |
| Environment | a 320px container, a 280px sidebar, 2560px wide, 200% zoom, dark, RTL, touch only (no action reachable only by hover) |
| Failure | offline, timeout, 401 (to login), 403, 404, 429, 500; a double-clicked submit (only one request); an interrupted drag (`pointercancel`) |

**Common symptoms and fixes:**

| Symptom | Fix |
|---|---|
| Squished avatar | `flex-shrink: 0` |
| Text overflowing its column | `min-width: 0` |
| An email running off the edge | `overflow-wrap: anywhere` |
| A wrapping badge | `nowrap` + `flex-shrink: 0` |
| An avatar drifting beside a three-line name | `align-items: flex-start` |
| "1 members" | `Intl.PluralRules` |
| Jittering digits | `tabular-nums` |
| A translated label overflowing | `min-width`, not `width` |
| Clipped diacritics | looser line-height |
| A broken image | initials fallback |
| Truncated text with no way to read it | full value on hover, focus or tap |
| 1,000 rows stuttering | virtualise |

**Report format.**
1. A table: `# | Severity (Broken / Ugly / Fragile) | Field | Value | What happens | Fix (file:line)`.
2. The decisions the owner must make (truncate or wrap, paginate or virtualise).
3. What held up.

Report the findings before fixing them.

## 5. Evidence in the PR

- 2–4 screenshots in the PR body:
  1. where the change lives in the app
  2. the main screen
  3. one variant (phone or dark)
  4. one detail
- Name the browser specs and viewports you ran, with counts. A Playwright `--project` filter can silently skip a spec, so compare the count that ran with `--list`.
- Say which findings were seen and which were inferred.
