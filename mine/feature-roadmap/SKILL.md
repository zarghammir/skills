---
name: feature-roadmap
description: Before starting any feature, part of a feature, or new phase, produce a simple visual roadmap (a flowchart in plain words) for the owner, delivered as a link to a web page. Use when the owner is visual and watches the work rather than reading code.
---

# Feature roadmap, before the work starts

Written for an owner who said: "Before you start each phase, make the flowchart, with more details, in simple words. I'm going to be observing, I'm not diving deep into the technical part. I just want to make sure that it aligns with our ideology. Whenever you want to start a feature, a part of a feature, or a brand-new feature, make these diagrams."

## When

Every time work is about to start on a feature, a slice of one, or a new phase; and whenever the owner asks "what is X". Do it before the work starts, never after.

## The structure (same every time, so the owner can compare)

One self-contained HTML page, system fonts, no external assets. Sections, in this order:

1. **Title and one sentence:** what this feature is, in the words the people who will use it would use. No product terms the owner has not met.
2. **Why it's needed:** the goal, customer request or requirement it serves, in one sentence.
3. **The flow, as numbered boxes with arrows:** what a person does, step by step, and what the system does in response. Green = built and live, blue = being built now, grey = later. Six to nine boxes.
4. **Who uses it:** the roles, one line each.
5. **What they will see:** the screens, named the way the app's navigation names them, with where each sits in the app.
6. **What is in this phase and what is not:** two short lists, the "not" list naming the ticket that carries it.
7. **How we will know it works:** three to five checks in plain words (no test names).

Keep it to one page. Plain words over completeness. A technical detail goes in only if the owner needs it to decide something.

## Delivery

- **Publish the page and give the link in one line.** A link is cheaper than rendering pictures, and the owner can open it on any device. In Claude, publish it as an Artifact (write the HTML without its own doctype/html/head/body wrapper, and with no fixed body width).
- Keep one page per feature and **republish to the same link to update it**, so the link the owner has stays current as the phase moves.
- Then the short chat message: one line with the link, then the decision you need or the work you are starting.

Related: `pr-plain-words` and `pr-like-a-pro` (explaining the finished work).
