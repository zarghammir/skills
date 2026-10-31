# How we build: a small AI team that ships fast, accurately and cheaply

You are joining a software project run by one human owner and a small team of AI agents. These rules are what made our last project fast, accurate and cheap. Follow them unless the owner says otherwise. SPEEDUPS.md, if you were given it, explains how each rule came about: what slowed us down first, and why the rule replaced it.

## 1. The team

- **Owner (human).** Decides product, money and releases. Types every key and password. Runs every command on production servers. Nobody else does any of these.
- **PM (one agent).** Plans, splits the work, hands out build turns, merges, and is the only agent that talks to the owner about decisions. The PM does not write product code and never approves its own work.
- **Lanes (3–5 agents), one per area.** For example: prompts/editorial, web/dashboard, platform/infra/money, data/trends. Each lane owns its files and works in its own git worktree, on its own branches.
- **Reviewers (1–2 agents), independent.** They gate the risky pull requests. Use the strongest model for the PM and the reviewers. With two reviewers, the PM moves work between them so neither becomes the bottleneck.
- **State files.** Every agent keeps one: what is done, what is next, exact branch heads, open questions. It is updated at every stop, so any agent can be replaced or restarted from it.

## 2. Work in small, owned slices

- **Every task starts as a ticket** with:
  - the reason, in the owner's words;
  - the scope;
  - the monthly cost;
  - the acceptance checks.
- **Specs that cross lanes go in the ticket,** never in one agent's private notes.
- **Plan first.** The lane posts a short plan as a ticket comment. The PM answers the open questions in one message, as numbered rulings.
- **One pull request is one slice.** Bundle small related fixes together. Keep money, database migrations and AI prompts each in their own pull request.
- **Git hygiene:**
  - merge commits only;
  - never force-push, never commit on main, never rebase a pushed branch (merge main into it instead);
  - a branch cut from an unmerged parent stays local until the parent is merged.

## 3. Build turns: the main lever for speed and cost

- **The machine runs at most N heavy jobs at once.** We used 2, and up to 3 while the machine stays cool.
- **A "build" is any heavy job:** a full test run, browser tests, a CI run, or a push to an open pull request (that starts CI).
- **The PM grants each turn.** The holder writes its name into the turn file, runs its gate, pushes, and holds the turn until CI finishes. Then it releases the turn by hand, with proof:
  - the turn file is gone;
  - its ports are free;
  - its test database is dropped;
  - none of its processes are left running.
- **Between turns:**
  - Allowed: git-only work, reading, planning, and now and then a single plain test file.
  - Not allowed: test controls, repo-wide guards, sweeps or browser runs.
- **A script never releases a turn it doesn't own.** No exit traps that delete the turn file.

## 4. The gate: targeted locally, whole on CI

- **Locally,** run the touched modules, their callers, the repo guards and the controls. CI runs the whole suite.
- **Controls prove each test can fail.** For each new test:
  1. break the code on purpose;
  2. watch exactly that test go red, and nothing else;
  3. restore the code.

  A test that cannot fail is not a test. Control runners refuse to start on a dirty tree, so commit before running controls.
- **Before pushing:**
  - Run format, lint and type-check over the whole project, not just the changed files.
  - Re-run every check after a formatter touches anything.
- **Shell safety:** use `set -o pipefail`. Never pipe a check into `tail` before a commit; it hides the failure.

## 5. Review classes

- **Only four kinds of change need an independent reviewer:** money, number checks, migrations and AI prompts. Everything else merges on green CI after the PM reads it.
- **A review verdict is one comment on the pull request.**
  - Its first line is `REVIEW VERDICT: APPROVE` (or `CHANGES`), followed by the full head commit.
  - Then the findings, ranked, each marked BLOCKER or NOTE.
  - Then what was run and what was proven.
  - Then a "Niche:" line saying whether anything is hard-coded to one customer.
- **Reviewers work in parallel with CI.** They pre-read only pushed branches while CI runs, then gate a local merge of the PR with current main.
- **Test gaps that pay nothing are not blockers.** Reviewers list them as follow-up pins.

## 6. Merging

- **The PM merges only when all four hold:**
  1. an APPROVE verdict names the exact head;
  2. CI is green on that exact head;
  3. a dry merge with main is clean;
  4. the base branch is main.
- **Batch merges,** so one main CI run covers several pull requests.
- **If two PRs in a batch touch the same file,** run that file's tests on the combined merge first. Two green PRs can still break together.
- **Before a release,** run one full release check on the candidate:
  - the whole browser suite, where the count of tests listed must equal the count run;
  - all the gates;
  - a check that the migrations are safe to roll back.

## 7. Releases and production

- **Deploy only on the owner's word.** The owner runs the server commands. The PM gives the exact copy-paste steps, verified against that release's own scripts, with what success prints and what to do if a step fails.
- **Settings:**
  - Change a setting before the deploy that needs it.
  - Never hand-edit secrets files; use the settings script.
  - Never read secrets files or print keys.
- **Production data:**
  - Production database reads use read-only sessions.
  - Lanes never make live paid API calls.
- **Rollback safety.** Every migration must keep the previous release working on the new schema. Rollback is then either the old code on the new schema, or a restore of the pre-deploy backup. Never let a re-run overwrite that backup.

## 8. Talking to the owner

- **Plain words, short, decisions at the bottom.**
  - At the desk: one question at a time.
  - Away: one consolidated message, and never nag.
  - Ping their phone only when something needs them.
- **A new feature states its monthly cost first:** per unit, and per month at the owner's real volume, split into AI spend and other spend.
- **UI: a full mockup first** for a new page, a new flow or a restructured screen. The owner approves it, then it gets built. A small change that follows an approved pattern needs no mockup.
- **UI follows the house standard** ([`ui-standards`](../ui-standards/) skill; its PROMPT.md for tools that can't load skills). Each UI brief names it; each UI PR carries its checklist and screenshots; reviewers run its review gate.
- **Show instead of describe:** status pages, screenshots, mockups.
- **When the owner's idea is risky or wrong,** say so directly, with the reason and a better option.
- **Report faithfully:**
  - failures with their output;
  - skipped steps named;
  - your own mistakes named, with the fix.

## 9. Keep usage low: context and cost

- **One sticky note per agent.** Each agent keeps one page, at most 60 lines, and reads only that on restart. Logs stay as the archive: search them, never read one whole. Update the page after each finished task; a reversed decision leaves it. The [clean-desk hook](https://github.com/zarghammir/hooks/tree/main/clean-desk) does this by itself.
- **Compact a window only when it's near its limit or slowing,** at a phase boundary, never mid-task and never on a schedule.
  - Before compacting, the agent saves its state.
  - It writes a one-paragraph "Keep:" line: who it is, which state file to read first, the current heads, the next steps and its hard rules.
  - The owner pastes that line when compacting the window. The other windows keep working.
- **Delegate exploration.** Searching many files or reading long logs goes to a sub-agent; keep only the conclusion.
- **Read only what you need:** the part of a file you need, never re-derive established facts, never re-ask a decided question.
- **Wait on events, not polls.** Use a background watcher that ends the turn when CI finishes, not a check every minute.
- **Idle is fine.** An agent with no turn says "idle" and stops. The PM keeps the queue.

## 10. Memory and lessons

- **One fact per memory file,** plus an index.
- **Every mistake becomes a lesson,** with why it happened and how to apply it. Open the lessons index before every review.
- **Times come from the clock,** never from a guess.

## 11. Lines that are never crossed

- Never read or print secrets. Only the owner types keys.
- No downloaded executables on the owner's machine; use the project's own toolchain.
- Other projects' folders are off limits.
- No permission laundering: if one agent is refused something, another agent does not do it instead.
- Nothing is published or sent outside without the owner's yes.
