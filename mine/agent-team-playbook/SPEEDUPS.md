# What slowed us down, and what fixed it

This is the history behind the rules in PROMPT.md. A team of one human owner, one PM agent, 3–5 lane agents and 1–2 reviewer agents started out slow. Each item below was a real slowdown and the decision that removed it. Read it before you set up a new team, so you start with the fast version.

Each item has three parts:
- **Slow:** what we did at first.
- **Cost:** why it hurt.
- **Now:** the rule that replaced it.

Section 9 lists the shortcuts that backfired. Don't repeat them.

---

## 1. The big one: CI on the owner's only computer

This took three weeks and a long route to solve, and most of the other rules come from it.

**The problem**
1. GitHub's hosted runners stopped once the free minutes ran out on the private repo, and the budget was $0.
2. We moved CI onto the owner's laptop as self-hosted runners.
3. That laptop was also running every lane's tests.

**What it cost**
- One test suite took 21–26 minutes, plus 0–30 minutes in the queue. Each failed CI round cost about 30 minutes plus a re-review.
- Load reached 24, 58, 59, 77 and 143 on a 14-core machine. Once memory ran out (88 MB free) the machine rebooted, and the reboot wiped /tmp along with our tools.

**The route, in order**
1. **CI blocked by billing.** Raising the budget was refused, so we ran CI on the owner's Mac. The owner ran the runner setup, because agents were refused the database-role step.
2. **Runner hazards.** The runners uploaded the owner's personal package caches and connected to the database as a superuser. Fixed with separate cache folders and a non-superuser CI role.
3. **"CI is the bottleneck."** The owner added runners 3 and 4. Load hit 24, so the owner took the project folders out of Spotlight indexing.
4. **Five full suites at once heated the machine.** We added test slots, path filters (skip jobs a change can't affect, with one summary check where "skipped" counts as "not affected") and a cap on parallel workers.
5. **We measured before buying anything.** Template databases gave no gain (24:40 → 26:10). The real cost was about 840 database create/drop pairs per suite, plus video rendering at 25% of the time.
   - Cutting databases per run from 869 to 153 brought the suite from 18:46 to 16:40.
   - Cheaper render tests brought it to about 10 minutes.
6. **Tools moved off /tmp after the reboot,** into a home-folder tools directory and `~/Projects` worktrees.
7. **Lanes stopped running the whole suite locally.** They run touched modules, their callers, the guards and the controls; CI runs everything once.
8. **Parallel workers kept overheating the machine.** `pytest -n auto` with 14 workers hit load 59, and 3 CI workers hit 58. Capped at 2 workers everywhere.
9. **Load caps failed three times** (2 slots → 3 slots → "start nothing above load 30" → "≤ 22"). Agents kept starting jobs just under the line. The owner replaced the caps with **build turns:** only the lane holding the turn may build. That meant one turn, later two, one again once a second project shared the machine, and up to three while the machine stays cool.
10. **We closed the loopholes in what counts as a build.**
    - The PM's own CI re-runs count.
    - Opening a PR counts, because it starts CI.
    - A push to an open PR counts.
    - A reviewer re-running the whole suite counts. Green CI on the exact head now replaces that run.
11. **Paid alternatives were priced from measured runs and declined.**
    - Hosted overflow was about $5–10 a day.
    - A paid plan meant overage of about $70–150 a month, at 35–60 runs a day × about 28 job-minutes each.
    - There was no spare machine.
12. **A heat guard was added,** and a second project now shares the machine through stop files that work both ways.

**Where it ended up**
- Free self-hosted runners with path filters.
- Targeted gates locally; the whole suite runs once, on CI.
- At most 2 test workers.
- Build turns granted by the PM, where CI runs count as builds.
- A heat guard that pauses heavy work at once.

The result: normal load is about 8–10 with 2 builds plus CI, CI costs $0, and 82 PRs merged in about a day and a half.

**Lessons from it**
- **Measure before buying capacity.** The slow part was rarely what we guessed.
- **Count every kind of build,** including CI runs, PR openings, pushes to open PRs and reviewer re-runs.
- **Keep runners × workers below the core count,** and gate on the 5-minute load, not the 1-minute load.
- **A self-hosted runner on a personal machine** needs its own cache folders and a database user without superuser rights.
- **Price paid options from your own measured runs,** then let the owner choose.

---

## 2. Testing and gates

- **Slow:** Every lane ran the whole suite before every push, and CI ran it again.
  - **Cost:** 5,178 tests in 17–20 minutes, twice per change, while the machine overheated.
  - **Now:** Locally, run touched modules, their callers, guards and controls. The whole suite runs once, on CI.
- **Slow:** The reviewer re-ran the whole suite on each PR.
  - **Now:** Green CI on the exact head commit stands in. The reviewer gates only a local merge with main on the touched areas.
- **Slow:** Many tiny PRs, each one a CI run.
  - **Now:** Bundle related small fixes into one PR. Keep money, migrations and AI prompts in their own PRs.
- **Slow:** Free-form testing between turns grew into guard sweeps and control loops.
  - **Now:** Between turns, at most one plain test file, or up to three in one command if the machine is calm. Controls and guards run only inside a held turn.

## 3. Machine load and build turns

- **Slow:** Lanes coordinated builds among themselves, through a reminder line.
  - **Cost:** The laptop crashed.
  - **Now:** One build slot, granted by the PM.
- **Slow:** A denylist of commands that weren't allowed outside a slot.
  - **Cost:** It failed three times, because agents found a command that wasn't on the list.
  - **Now:** An allowlist outside a turn (git, gh, type-check, lint, format, read, write), with no exceptions.
- **Slow:** Turns granted in advance, or with conditions ("start when X finishes").
  - **Cost:** The machine sat idle while a lane waited for its condition.
  - **Now:** Grant at the moment the turn is free, to one named lane.
- **Slow:** One slot for browser tests.
  - **Now:** A second browser slot with its own ports. Every slot release proves the turn file is gone, the ports are free, the test database is dropped and no processes are left.
- **Slow:** A heat watch on the 1-minute load.
  - **Cost:** It tripped falsely four times.
  - **Now:** Use the 5-minute load for warnings, and pause (SIGSTOP) heavy processes at once on a real thermal warning.

## 4. CI

- **Slow:** Every PR ran every job.
  - **Now:** Path filters, plus one summary check that the merge gate reads.
- **Slow:** Each merge started its own main CI run.
  - **Now:** Batch merges, so one main run covers several PRs. If main's tree is the same as the PR merge ref that CI already tested, cancel the main run as redundant and say so.
- **Slow (a second project):** Hosted CI minutes ran out.
  - **Now:** A minute budget: Linux only, job timeouts, cancel superseded runs, skip draft PRs, push once per fix.

## 5. Review and merging

- **Slow:** The owner clicked every merge.
  - **Now:** The PM merges on a reviewer APPROVE plus green CI on the exact head.
- **Slow:** One serial reviewer, doing about 2 reviews an hour against 8 PRs waiting.
  - **Now,** in the order we added them:
    1. **Review classes:** only money, number checks, migrations, AI prompts and auth need a reviewer. Everything else merges on green CI after the PM reads it.
    2. **A second reviewer.**
    3. **The PM moves PRs** to whichever reviewer has the shorter queue.
- **Slow:** Long review rounds.
  - **Cost:** Six rounds on one regex fix. On another project, 40 minutes of coding took 2 hours of review plus 1 hour waiting on clicks.
  - **Now:**
    - The reviewer starts reading on the first push.
    - Findings are BLOCKER or NOTE only.
    - At most one fix round.
    - Test gaps that cost nothing become follow-up notes, not blockers.
    - If the same kind of problem comes back, change the approach instead of patching again.
    - On some projects, small changes (about 100 lines or fewer) skip review.
- **Slow:** A slower model ran the reviewers and lanes.
  - **Now:** The fast strong model everywhere. A slow model is a bottleneck of its own.

## 6. Owner communication and decisions

- **Slow:** Questions parked on status pages.
  - **Cost:** They went unanswered for days.
  - **Now:** Ask decisions through the choice prompt, one at a time. Pages only show things. Put commands in code blocks.
- **Slow:** Many status pages.
  - **Now:** One status page per project, with screenshots. See the `project-status-page` skill.
- **Slow:** A comparison built as a permanent feature.
  - **Cost:** 6+ hours behind the review queue.
  - **Now:** A one-off tool the owner runs, in 1–2 hours. The owner wants answers, not features.
- **Slow:** Asking the owner about technical permission blocks.
  - **Now:** Take the compliant path and tell the owner in one line. Never ask the same question twice.
- **Slow:** Building first and pricing later.
  - **Now:**
    - Every new feature states its monthly cost first.
    - Every UI change starts from a full mockup the owner approves.
    - When the owner is at the laptop, ask freely. When away, send one consolidated message with the questions at the bottom.

## 7. Context and usage

- **Slow:** Long sessions with no compaction.
  - **Cost:** 96% of tokens were cache re-reads of a ~500k context. One PM used 13× the tokens of another.
  - **Now:** Compact at phase boundaries. Send exploration to sub-agents that return only the conclusion.
- **Slow:** A compaction freeze every 2 hours.
  - **Cost:** It stalled the lanes.
  - **Then:** Every 3 hours, on a schedule. Each window saved its state and a one-paragraph "Keep:" line, and the owner pasted the lines in one round.
  - **Cost:** Every round still froze the whole team, and agents were idle while they waited for it.
  - **Now:** No schedule. A window compacts only when it's near its limit or slowing; the others keep working.
- **Slow:** Heavy multi-agent runs by default.
  - **Now:** Only when the owner asks. Under usage pressure, go terse.

## 8. Coordination between agents

- **Slow:** A lane said "carrying on" and then sat idle.
  - **Cost:** 80 minutes were lost.
  - **Now:** The PM subscribes to idle notices after every dispatch. "Carrying on" means idle.
- **Slow:** Two watchers each waited on a `pgrep` match.
  - **Cost:** They matched each other, so a gate sat unstarted for 45 minutes.
  - **Now:** Wait on a process id or an output line, never on a name match.
- **Slow:** A spec written in one agent's private scratch notes.
  - **Cost:** Other lanes couldn't read it.
  - **Now:** Cross-lane specs go in a ticket comment.
- **Slow:** Lanes waited idle between turns.
  - **Now:** Between turns, do git-only work (plan, write, stage the next branch), so each turn starts ready.
- **Slow:** Tools and worktrees under /tmp.
  - **Cost:** A reboot wiped them.
  - **Now:** Keep them in reboot-safe folders under the home directory.

## 9. Shortcuts that backfired: don't repeat them

1. **Load caps instead of turns.** Agents start just under the line. Use granted turns.
2. **`-n auto` "because the shared-database bug is fixed".** The fix made the tests correct, not cheap. Cap workers.
3. **Merging UI PRs on CI alone.** Main's end-to-end tests broke three times. Run the whole browser suite on main after any merge that changes ordering or fixtures.
4. **Batch merging on "each PR green" alone.** Two green PRs broke together. Test the files they share on the combined merge first.
5. **An exit trap that deletes the turn file.** It released a turn the script didn't own. Only the owner of the whole turn releases it.
6. **"Push the untested test and let CI run it."** Withdrawn.
7. **Spending cloud credit freely.** Use local first, set a stop line, and launch nothing without the owner's yes.

## 10. The meta-rule

**When a rule fails three times, change its shape, not its strength.** A tighter load cap, a longer denylist or a stricter reminder kept failing. A different mechanism worked: a granted turn, an allowlist, a ticket comment.
