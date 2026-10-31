---
name: agent-team-playbook
description: Run a software project with a small AI team (one PM agent, 3–5 lane agents, 1–2 independent reviewers, one human owner) the fast, cheap way proven on a real product build. It covers build turns (at most N heavy jobs at once), local gates versus CI, review classes, the PM merge gate, release checks, owner communication (cost first, mockup first) and usage discipline (compaction "Keep:" lines, sub-agents for exploration, background watchers). Use it when starting or running a multi-session build, when the user says "work the way we work", "set up lanes", "PM mode", "build turns", "Keep lines" or "compact the windows", or when an agent joins such a project. PROMPT.md beside this file is the portable version for other tools (ChatGPT, other agents).
---

# Agent team playbook

The rules themselves are in **PROMPT.md** (beside this file). Read it first; it is the canonical text, and the version you hand to other agents and tools. This file adds the Claude Code mechanics and the templates that make those rules fast to follow. **SPEEDUPS.md** gives the history behind the rules: each habit that slowed us down, what it cost, the rule that replaced it, and the shortcuts that backfired. Read it before setting up a new team.

## Start-up checklist (new project)

1. **Owner decisions first, through the choice prompt.** One question at a time:
   - the lanes and what each owns;
   - how many build turns run at once (default 2; up to 3 while the machine stays cool);
   - who reviews (strongest model);
   - the budget and its spending lines.
2. **Create per-agent state:**
   - a memory file per lane (`<project>-<lane>-lane.md`), with a STATE SAVED block at its tail;
   - a reviewer state file;
   - the PM log (`<project>-project.md`), with timestamped lines from `date`;
   - one compact-lines file holding every window's "Keep:" line.
3. **Make a turn folder that survives a reboot:** `~/.<project>-ci/` holding `build-turn` and `build-turn-2`, plus shared scripts. Never keep these in /tmp.
4. **Put lane worktrees under `~/Projects/<project>-<lane>-<topic>`,** never in /tmp.
5. **Set up the ticket space** (Jira or similar) and a decision log page (D-numbers).
6. **Write the standing rules into memory,** one fact per file: secrets, deploys, no paid calls, review classes, gate rule, compaction.

## Build turns: the mechanics

- **The turn file's first line is `<agent-name> <YYYY-MM-DD HH:MM:SS TZ> <purpose>`.** The holder writes it; the PM grants it by message.
- **Check before granting a slot (ports + test DB prefix).** Run `lsof -nP -iTCP:<port> -sTCP:LISTEN` for each port, plus `pgrep -afl` and a cwd scan. Ports being free does not mean nothing is running.
- **The PM's own CI runs hold a turn too.** Start a background watcher that removes the turn file only when the file's first line starts with the PM's own name:

```zsh
SHA=<head>; while true; do s=$(gh api "repos/<o>/<r>/actions/runs?head_sha=$SHA&event=push" | python3 -I main_ci_state.py)
case "$s" in done*) break;; esac; sleep 60; done
head -1 ~/.<project>-ci/build-turn | grep -q '^<pm-name> ' && rm -f ~/.<project>-ci/build-turn
```

- **Release proof:** the turn file is gone, there are 0 listeners on the slot ports, the test DB is dropped, the agent has no pytest or browser processes left, and its tree is clean.

## PM merge gate: the exact commands

```zsh
gh pr view N --json headRefOid,baseRefName,state                    # head + base main
gh api repos/<o>/<r>/commits/$H/check-runs -q '...ci-summary...'      # green on the exact head
gh api repos/<o>/<r>/issues/N/comments  # first line "REVIEW VERDICT: APPROVE" containing $H
git merge-tree --write-tree main pr/N                                 # rc 0 (progressive for a batch)
comm -12 <(git diff --name-only main...pr/A|sort) <(git diff --name-only main...pr/B|sort)  # shared files
gh pr merge N --merge --match-head-commit $H
```

Then post one comment on the ticket. Batch the merges back to back. A later push run may cancel the earlier one; that is expected, because the final head's run covers them all.

## Templates

**Dispatch** (PM to a lane), one message:
> T1 IS YOURS for <slice>: write build-turn with your name first. WHY: <one line>. DO: 1) merge main <sha> 2) <change> 3) control: <test> red without, green with 4) gate: touched + callers + guards + whole-project type-check 5) push, hold T1 through CI 6) report head + CI, release with proof. NOT in this push: <deferred>.

**Rulings** (PM to a lane):
> RULINGS: 1. <decision + one-line why> 2. … Cost line: <$/mo>. <Release> scope; git-only until a turn is granted.

**Review verdict** (one PR comment):
> REVIEW VERDICT: APPROVE <full sha>
> Gated: local merge <sha> with main <sha> (tree <sha>). Ran: <checks + counts>. Controls: <n of m red; each green one explained>. NOTES: N1 … Niche: <nothing hard-coded / gap>.

**"Keep:" line** (one per window, saved in the compact-lines file). It never starts with "/compact"; the owner types that.
> Keep: I'm the <project> <lane> lane <window-name>; PM <name>; reviewer <name>. Read the STATE SAVED block at the TAIL of <lane-file>.md first. <Merged / open PRs with heads>. Next, each on a PM turn: <1>, <2>, <3>. <Two or three hard rules>. No build without a turn; between turns git-only and single plain test files.

**Deploy steps** (PM to the owner). Verify each one against the release's own scripts first:
> Step N of M: <what it does, in one line>. Paste: `<command> | tee ~/<project>-server/deploy-<n>.log`. Good result: "<exact line>". If you see "<failure words>", stop and paste it to me.

**Owner message:** the answer first, then a small table if it needs numbers (per unit and per month; AI spend versus other spend), then the questions at the bottom. Add a phone push only when something needs them.

## One sticky note per agent

An agent's context is re-sent with every message, so old notes cost usage and cause mistakes. Each agent keeps one page, at most 60 lines: Updated time, Goal, In progress, Next 3, Blocked / waiting, Decisions that still matter, Gotchas. One line each, with links.

- On restart, an agent reads only its page. Logs stay where they are as the archive: search them, never read one whole.
- Update the page after each finished task. A reversed decision leaves the page.
- With pages current, nobody needs a state-save round before a compact.
- Keep the always-loaded memory index short too. It sits on every agent's desk all day.
- The [clean-desk hook](https://github.com/zarghammir/skills/tree/main/hooks/clean-desk) does this by itself in every window.

## Usage discipline (what kept cost minimal)

- **Compact a window only when it's near its limit or slowing,** never on a schedule. Scheduled rounds (every 3–4 hours, every window at once) froze the whole team and cost more than they saved once usage allowed. When a window does need it:
  1. It finishes its current step and saves its state.
  2. It refreshes its Keep line and tells the PM.
  3. The owner compacts that one window; the others keep working.
- **Sub-agents** handle wide reads (inventories, code-path maps) and return a report of at most about 2,000 words. Background agents for anything long.
- **No polling loops in the main context;** use background watchers and notifications.
- **Lanes between turns:** git-only, and now and then one plain test file. Controls, guards and browser runs happen only inside a turn.
- **Two reviewers:** move PRs between them when one queues up. A PM stand-in sub-agent can carry a lane whose window died.

## Lessons that cost us time (avoid them)

- Two PRs that are each green can break together when they share a file: test the combined merge.
- A control runner on a dirty tree can wipe uncommitted fixes: refuse to run when the tree is dirty.
- `cmd | tail && git commit` commits even when the check failed: use `set -o pipefail`.
- A Playwright `--project` filter can skip a whole spec silently: compare the `--list` count with the number that ran.
- A layout sheet that clips its content hides a phone-width overflow from "no sideways scroll" checks: look at the 390 px screenshot after any change to a string.
- Re-running a deploy can overwrite the pre-deploy backup: keep the first one.
- macOS awk has no `\b`, and macOS pgrep hides its own ancestors: check one busy port once to prove a filter works.
- Log times come from `date`, never from memory.

## Sharing

PROMPT.md holds no keys, server addresses or project secrets, so it can go to any agent or tool. Keep project-specific facts in that project's memory, never in this skill.
