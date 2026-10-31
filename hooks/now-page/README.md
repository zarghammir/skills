# now-page

One short page per agent, read by itself on every restart. For Claude Code.

## The idea

Picture a helper with a desk. Before answering anything, even "hi", the helper reads every paper on the desk. Few papers: fast and cheap. Lots of papers: slow, costly, and some of them are no longer true.

So each helper gets three things:

1. **A sticky note.** One page, at most 60 lines: what I'm doing now. That's the NOW page.
2. **A drawer.** The old logs. Opened only when a job needs something old.
3. **A true note.** When a decision changes, the old one comes off the page.

This matters most with a team of agents. Keep the pages current and nobody needs a round of saving state before a compact, because the page is already saved.

## What the hooks do

| Hook | When | What it does |
|---|---|---|
| `now-page-start.sh` | The session starts or resumes, or after a compact | Tells the agent to read only its own page, and how to keep it |
| `now-page-check.sh` | After any edit to a page | Warns if the page is over 60 lines or has no `Updated:` line |

A hook can't think. It makes the reminder automatic and checks the size. The agent still writes the page.

## Install

Needs `jq`.

```sh
mkdir -p ~/.claude/hooks ~/.claude/now
cp now-page-start.sh now-page-check.sh ~/.claude/hooks/
```

1. Merge `settings-snippet.json` into `~/.claude/settings.json`. Merge it, don't replace the file.
2. Give each agent a page from `TEMPLATE.md`, for example `~/.claude/now/reviewer.md`.
3. Restart your Claude Code windows. Hooks load when a window starts, so a window that's already open won't run them.

To keep pages somewhere else, set `NOW_PAGES_DIR`.

## Two tips

- Don't move old logs. They already work as the drawer, and moving them breaks links. Search them, never read one whole.
- Keep your always-loaded memory file short too. It sits on every agent's desk all day.

Part of [agent-team-playbook](../../mine/agent-team-playbook/). MIT licence, see [mine/LICENSE](../../mine/LICENSE).
