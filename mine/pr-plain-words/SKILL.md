---
name: pr-plain-words
description: Use whenever you suggest, present, or report a pull request to an owner who does not read code. Explain exactly what the PR is for in simple words for a non-technical reader, with full details, so they can decide whether to approve it.
---

# PR in plain words

The owner approves pull requests but does not read code and does not remember which PR is which. Every time a PR is suggested, presented for approval, or reported on, explain it as if to a non-technical person. Do not hide details behind ticket numbers or jargon; translate them.

## Before writing

Read the PR's own title and body (`gh pr view <n> --json title,body`) and, if a review verdict exists, the reviewer's comment. Explain what is actually in the PR, not what you remember planning.

## The shape: precise, not over-explained

Answer exactly these five, in order, one or two sentences each, then one line on where it stands and whether to approve:

1. **What is happening in the records.** Which data the PR touches and how: for example customers, orders, products, users; created, changed or read.
2. **The flow** the person follows, step by step.
3. **Who** uses it (the role).
4. **What exactly they see** (the screens, in order).
5. **What purpose it serves and what problem it solves.**

No inventory of what the reviewer did; one sentence on review status is enough.

## When a longer explanation is needed

1. **One line:** the PR number as a clickable link, and the feature in everyday words ("teaches the app to record what a technician does to a job").
2. **What a person can now do.** One bullet per behaviour a user can see. Say what they see, not what the code does.
3. **What it fixes under the hood.** Still plain. Lead with the consequence a user would notice ("the pending counter showed three when you changed one thing"). A technical name appears only in brackets after the plain phrase, and only if the reader needs it to find something.
4. **What it does not include.** Scope left for later, with the ticket it went to, in plain words.
5. **Where it stands.** What the reviewer checked, what is still open, and whether approval is wanted now or later.

## Rules

- Full details; never shorten by leaving out a change. Shorten by using plainer words.
- Analogies over terms. "One record instead of two numbers that can disagree" beats "denormalised total".
- Numbers only when they change what the owner does.
- The same standard applies to ticket comments and any status page the owner reads.
- Refresh the explanation when the PR changes before approval; do not reuse a stale one.
- The explanation travels with every message that names a PR for approval or reports on it. Never point back to an earlier message; a link plus a five-word label is not an explanation. Repeat it in full each time.

## Pictures, always

Many owners are visual. Every PR presentation includes the PR's own screenshots: two to four pictures, one caption each (the main screen; one variant such as tablet width or another language; one detail). For a PR without a screen, send one picture of the screen it protects, with a caption saying what would have gone wrong, or a small diagram. Text alone is not a finished explanation.

If your chat does not render inline images, send each picture as its own file with its explanation as the caption.

Related: `pr-like-a-pro` (the PR body itself; this explanation summarises it, never replaces it).
