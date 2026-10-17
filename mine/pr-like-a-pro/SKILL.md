---
name: pr-like-a-pro
description: How to write a pull-request body the owner can read cold, "like I'm five", that still carries every measurement a reviewer needs. Use for every pull request; the builder writes the body this way, and whoever makes the merge call checks it first.
---

# PR like a pro

The owner reads pull requests between projects, tired, on a phone or a wide screen, and does not remember which PR is which. The body's first job is to put their mind back where it needs to be in three sentences. Its second job is to let a reviewer verify every claim without asking. Both jobs are done in the same document, in this order, in these words.

Written after an owner said of one PR: "I can honestly read it like I'm 5 … it explained the part that it needed, it didn't explain the part it didn't … it gathers my thoughts back to the place they have to be."

## The voice

- **Plain words first, technical words only where the reader needs them to find something.** "Saved is the bin. Everything you pressed Save on, newest first." Not "the saved-items store with descending sort".
- **Name the thing by what a person does with it**, then bold that noun once: **Saved**, **Settings**, **The welcome**.
- **One load-bearing phrase per paragraph, in bold.** The reader skims bold; the bold must carry the paragraph on its own.
- **Headings are sentences that say what the section proves**, not labels: "The three states this ships honest about", "Measured, not claimed", "Four defects the browser found, all in my own work". A heading that is a label ("Testing") tells the reader nothing about whether to read it.
- **Explain what was needed and leave out what was not.** No history of the branch, no list of every file, no restating the ticket. If a fact does not change what the reader thinks or does, it goes.
- **Why, beside every what.** A state that is visible but disabled gets the reason it is not hidden. A control removed gets the harm it was doing. A number gets the floor that makes it trustworthy.
- **Own the defects.** "All in my own work." A body that only reports greens is not believed.
- **Short sentences. No em-dashes as glue; a new sentence instead.** Numbers in tables, not prose.

## The shape, in order

Section names below are the voice. Where the repository's `AGENTS.md` or contributing guide prescribes its own section names (Purpose, What works, Test evidence, Known limitations, Risk and rollback, and so on), keep those names and pour this content into them. The repository wins on names; this skill governs what goes under them and in what order.

1. **`Closes #n.`** One line. Then a stacking line if stacked ("Stacked on #64; merging this merges its parent").
2. **What this is, in plain words.** One sentence for the whole ("Three screens a reader actually uses, and the plumbing behind them"), then one short paragraph per thing, each opening with the bolded noun and what a person does with it. This is the paragraph that re-anchors the owner's mind. Write it for them.
3. **What this ships honest about.** A table: *Thing · State · Why it is not hidden*. Every control that is visible but not working, every panel that says "nothing is sent yet", every described-but-not-drawn switch, with the ticket that will make it real and the reason faking it would be worse than admitting it.
4. **The dead control this removes** (when there is one). What was written by the person and read by nobody, what silently overrode it, and what one answer replaces the two.
5. **Measured, not claimed.** State where it was measured (production build, real browser, which port). A table of the measurements: states swept, accessibility violations at any impact, serious or critical, overflow, tap targets, each verify script's exit code with its floor, unit test count and file count, lint / format / typecheck as three zeros. Then **the sweep's own floor**, printed so it is not taken on trust (how many states recorded what they rendered, none landed on another route, minimum controls scanned per state). Then **the controls**, one line each: what was changed, which named check went red, and that only that one went red, run in the same window as the thing it guards.
6. **Defects the browser found, all in my own work.** A numbered list. Each item: the defect in plain words, why it matters beyond this PR when it does (bold it), and what closed it. Include the one caught before the machine.
7. **An assertion retired, then given back** (when it happened). Why the retirement was honest, who ruled to fix it, what the fix carries and deliberately does not carry, and the control that found the hole in the test itself.
8. **Things the screenshots showed that the DOM did not.** State the rule: a screenshot is a measurement, not a deliverable. Take the pictures, look at them before sending them, list what was wrong that every green number missed, and say every number was re-measured after the fixes.
9. **Things I did not decide alone.** Rulings taken with the reviewer or the owner, each with its reason, so nobody re-derives them from the code's general tone.
10. **For the other author** (when two branches share a shape). The merge order ruled, what will be folded into whose convention, and the general rule the collision taught.
11. **The screenshots.** A table *Shot · What it shows*, taken from a build just watched to behave, with the script asserting which page each came from. Where they live and why they are or are not committed, stated as a rule (lifetime, not file type). **Any tracked picture this PR makes stale is named here as known stale**, with the ticket that will regenerate it; a silently stale one is the defect.
12. **Also in here.** Documentation and decision-log changes, one line each.
13. Footer as the repository requires.

## Rules that make the body true

- Every number in the body is measured at the tip, through the real path, and re-measured after any change to a shared component.
- A control is named by the check it reddens. "Reddened only the limits test" is evidence; "tests pass" is not.
- A known-stale artefact with a note is honest; a silently stale one is the defect. The same holds for a disabled control with its reason beside it versus a hidden one.
- A retired assertion is recorded as retired, with why, and given back when it can be.
- The picture is looked at, not only taken. Correct markup that reads badly is a defect the DOM cannot see.
- If the body's first version said something false, the corrected body says so and names the sentence it replaces.
- Explain the part that needed explaining. Do not explain the part that did not.

## What to check before the merge call

The first paragraph re-anchors a reader who has been on another project all day. The states table has a "why" in every row. Every measurement has a floor or a control beside it. The defects section owns its findings. Any stale picture is named. Nothing in the body is a label where a sentence was possible.

Related: `pr-plain-words` (the short owner-facing explanation when presenting a PR for approval; it summarises this body, never replaces it), `feature-roadmap` (the page before the work starts).
