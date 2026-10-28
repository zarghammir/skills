---
name: project-status-page
description: Build and maintain ONE living status page per project for a visual, non-technical owner. It is a published Artifact link, never chat prose or PNG renders, and it answers "what's live, what needs me, what's being built, what's next, what does it cost" at a glance. Use it when the owner asks for status or "where are we", after a deploy or a big batch of merges, or when they ask a question that deserves a visual answer ("answer it on the status page"). template.html beside this file is the starting page.
---

# Project status page

The owner observes; they don't read code or long text. After too many pages, one owner said: "You only need to give me the status tracking artifact." So each project gets exactly one page. It is the only thing they are sent to look at, and it is kept current.

## The rules

1. **One page per project, one link, for good.**
   - Republish the same file, or pass the same `url`. Never create a new artifact for an update, and never send a separate feature page.
   - Feature flows, screenshots and answers to their questions all go INTO this page.
2. **No links to other artifacts on the page.** Old footer links "didn't work" for them. Everything they need is on this one page.
3. **Questions are asked with the choice prompt, not on the page.**
   - The page may show what is waiting for them, under "Now (your time)".
   - The actual decision is always asked as a choice prompt. In the owner's words: "a real question that pops up on the screen, not in the artifact … not very trackable".
4. **Refresh it on time.**
   - Refresh after every deploy, after each big batch of merges, and whenever they ask.
   - A stale page is a bug: it once sat 20 hours stale.
   - The stamp time comes from `date`, never from memory.
5. **Plain words.**
   - Write each change as what they will see on the screen, not as the kind of bug it was.
     - Good: "A ten-minute brief held two stories instead of six."
     - Bad: "The fixtures asserted article time."
   - Technical names go in brackets, or nowhere.
6. **One colour code everywhere:**
   - **green:** done or live;
   - **blue:** being built now;
   - **amber:** waiting on you;
   - **grey:** later or idle;
   - **red:** a problem caught.
7. **Money:** give every cost per unit (per video, per press) and per month at their real volume, set against their budget. Split AI spend from other spend when both exist.
8. **Screenshots go inside the page.**
   - Use before/after pairs, and make each caption say what the picture shows.
   - Embed them as compressed JPEG data URIs, about 1,000 px wide, and keep the page under about 1 MB.
   - Never render the page itself to a PNG and send that. PNG renders waste tokens; send the link.
9. **The page is link-shared,** so it carries no server address, key path, secret, personal email or customer data.
10. **It works everywhere:** at 390 px phone width with no sideways scroll, and in both light and dark themes (the template's tokens handle this).
11. **Simple beats complete.** If they ask one question ("which phase are we in?"), answer that one, with one diagram. A five-section dashboard for a one-line question was too much.

## Layout, top to bottom

The top screen always shows **today**. Older history moves down, or is dropped once nobody needs it.

| # | Block | What it answers |
|---|---|---|
| 1 | Header stamp | When this was written, what is live (one bold phrase), and the plan in one sentence. |
| 2 | Jump link | Only when they asked a question that is answered lower down. |
| 3 | **Now (your time)**, amber card | At most 3 numbered items: the test to run and the exact things to check on screen, decisions waiting (also asked by choice prompt), and any server step. |
| 4 | **Today** | What went live; what is merged but not live yet; what is being built now (each with its cost); one spend-check line. |
| 5 | **Your question**, blue box | Short answer and cost first; a 4–6 step flow; built vs to-build table; who does what; an example of what they'd see; the rules it can't break; when it pays off; their recorded answers. |
| 6 | Three number tiles | Only numbers they care about: changes in the release, cost per unit, cost per month against the budget. |
| 7 | **What release N brings** | One line per change, as a screen effect; problems caught before release; a "Known gap" line. |
| 8 | **Built since release N** | What goes out next, with before/after screenshot pairs. |
| 9 | **The team** | One small card per lane: what it is on, with a coloured dot. |
| 10 | **When it's ready** | Rough dates, each row tagged Live / Being built / Waiting on you / Later. |
| 11 | **Budget** | One bar per spending line: spent against its cap. |

Delete any block that has nothing true to say today. Never fill a block with filler.

## How to update it

1. **Read the live page first** with `Artifact` `action: "read"`, and build from the saved file it returns. It may have changed since your last copy.
2. **Take facts from their source:** merged PRs, the deploy log, CI results, the spend page, the ticket. Never from memory. The time comes from `date`.
3. **Rewrite the top blocks** (stamp, Now, Today). Move finished items down, and delete "being built" lines that have shipped.
4. **Check before publishing:**
   - 390 px width with no sideways scroll;
   - both themes;
   - no secret or server address;
   - no links to other artifacts;
   - every number has a unit and a source.
5. **Republish to the same link,** and keep the icon unchanged.
6. **Tell the owner in one line** with the link. If a decision is waiting, follow with the choice prompt.

## First publish

1. Copy `template.html`, then fill it or delete blocks.
2. Title: "<Project> status". Icon: `chart`.
3. Write down the URL in the project's memory and log, so every later session updates the same page.

## What went wrong before (don't repeat it)

- **Too many pages** (feature pages, roadmaps, mockups all sent separately). The owner couldn't tell what each was for.
- **A dense five-section dashboard** for a one-line question.
- **PNG renders of the page.** They cost tokens; a link is enough.
- **Questions asked only inside the page.** They went unanswered for days.
- **A page left 20 hours stale,** with a footer of dead links to old pages.
