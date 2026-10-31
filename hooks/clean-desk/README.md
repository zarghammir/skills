# clean-desk

One sticky note per agent, read by itself on every restart. For Claude Code.

## The idea

Picture a helper with a desk. Before answering anything, even "hi", the helper reads every paper on the desk. Few papers: fast and cheap. Lots of papers: slow, costly, and some of them are no longer true.

So each helper gets three things:

1. **A sticky note.** One page, at most 60 lines: what I'm doing now.
2. **A drawer.** The old logs. Opened only when a job needs something old.
3. **A true note.** When a decision changes, the old one comes off.

This matters most with a team of agents. Keep the notes current and nobody needs a round of saving state before a compact, because the note is already saved.

## What the hooks do

| Hook | When | What it does |
|---|---|---|
| `clean-desk-start.sh` | The session starts or resumes, or after a compact | Tells the agent to read only its own note, and how to keep it |
| `clean-desk-check.sh` | After any edit to a note | Warns if the note is over 60 lines or has no `Updated:` line |

A hook can't think. It makes the reminder automatic and checks the size. The agent still writes the note.

## Install

Needs `jq`.

```sh
mkdir -p ~/.claude/hooks ~/.claude/clean-desk
cp clean-desk-start.sh clean-desk-check.sh ~/.claude/hooks/
```

1. Merge `settings-snippet.json` into `~/.claude/settings.json`. Merge it, don't replace the file.
2. Give each agent a note from `TEMPLATE.md`, for example `~/.claude/clean-desk/reviewer.md`.
3. Restart your Claude Code windows. Hooks load when a window starts, so a window that's already open won't run them.

To keep notes somewhere else, set `CLEAN_DESK_DIR`.

## Two tips

- Don't move old logs. They already work as the drawer, and moving them breaks links. Search them, never read one whole.
- Keep your always-loaded memory file short too. It sits on every agent's desk all day.

Part of [agent-team-playbook](../../mine/agent-team-playbook/). MIT licence, see [mine/LICENSE](../../mine/LICENSE).
