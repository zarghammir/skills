# Reviewing UI (for reviewers and for self-review before a PR)

Approval is earned. Default to looking for the problem; review the rendered screen, never the stated intent.

## Gate tiers

| Tier | Meaning | Outcome |
|---|---|---|
| **Floor** | The non-negotiables in SKILL.md: contrast, focus, states, no fake data, no page-level horizontal scroll, reduced motion, no AI tells from the "blocker" list | **BLOCK** until fixed. Cannot be waived. |
| **Reflex** | The defaults in product-screens, foundations, components, motion and copy | Fix it, **or** waive it with a written reason in the PR body (at least one sentence, specific). If the same rule is waived three times in a row, it is house style; move it into DESIGN.md. |
| **Finish** | Polish: optical alignment, one-word last lines, themed `::selection`, nicer empty-state wording | Note it; it doesn't block. |

**Severity for findings:**
- **P0**: blocks the task or loses data.
- **P1**: major, or a WCAG AA failure. Must fix before release. "Would a user contact support about this?" means P1 or worse.
- **P2**: minor.
- **P3**: polish.

## The review pass, in order

1. **Read the context:** the ticket, DESIGN.md, AGENTS.md, and the owner's decisions for this screen. A deviation from this skill that the repo's rules require is a decision, not a defect, as long as the PR body names it.
2. **Look at the screenshots, or render it yourself.** Sweep each frame with no question in mind, then check the claims.
3. **Answer the product-screen questions:**
   1. Is the screen's one question answered by the biggest thing, read first?
   2. Do edges line up, with no dead strip, orphan cell or stretched blank card? Does the grid sum close?
   3. Is colour only on data, status, the one primary action and focus? Is there a single filled primary per view?
   4. Do the numbers add up and align? Do duplicated facts agree? Does every relative figure name its baseline?
   5. Does zero look like zero and missing look like "—"? Are count badges only on queues that need action?
   6. Are all five states present for every data region (loading, empty, error, full, edge)?
   7. Phone: is the nav folded, does each block still answer its question, and is there no sideways page scroll?
   8. Keyboard: can every action be reached with Tab and Enter, is focus visible, and does Escape close overlays?
   9. Copy: verbs on buttons, nothing repeated per row, no banned words, word count reasonable?
   10. AI tells: sweep [anti-slop.md](anti-slop.md).
   11. Motion: anything on a frequent action? Any `transition: all`, ease-in, `scale(0)`, or entrance choreography?
   12. Owner layout: steps bar on multi-step pages, two-column work area, primary action pinned once (no duplicate buttons), each step showing only its own sections, small destructive controls, an action on every suggestion?
4. **For a large new screen, score usability** (optional): Nielsen's 10 heuristics at 0–4 each (out of 40). Most real interfaces score 20–32; under 20 needs rework.
   - Check cognitive load too: ≤4 options per decision, 1 primary + 1–2 secondary actions, nothing the user has to remember from a previous screen.
5. **Run the persona sweep** (one line each):
   - impatient power user (shortcuts, bulk actions)
   - confused first-timer
   - screen-reader user
   - stress tester (worst-case data)
   - distracted phone user

## Anti-rubber-stamp rules

- **Every finding cites evidence:** `file:line`, a screenshot, or a measured value.
- **Score the worst sustained part,** not the average.
- **If everything passed, look again.** "If every score is 7+, you're not reviewing critically."
- For a big new page, use a **fresh-context reviewer** (a subagent that hasn't seen the build conversation) so the builder's intent doesn't anchor the verdict. Give it the screenshots, DESIGN.md and this checklist.

## Verdict format

Follow the project's convention. A good default is **one PR comment whose first line is `REVIEW VERDICT`**. Under it:
1. **BLOCK** or **APPROVE**.
2. Findings as one table: `| # | Severity | Where | Before | After | Why |`.
3. The waivers you accept, with their reasons.
4. What held up (2–3 lines).

Send a BLOCK to whoever merges the moment you find it; don't wait to finish the whole review.
