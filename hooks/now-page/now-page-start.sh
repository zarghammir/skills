#!/bin/bash
# SessionStart: tells the agent to read its one-page NOW note, and nothing else.
dir="${NOW_PAGES_DIR:-$HOME/.claude/now}"
text="Your current state is one page: $dir/<your-role>.md. On start or after a compact, read ONLY your page, then work. Open logs only when a task needs an old detail, and search them, never read one whole. After each finished task, update the page: Updated time, Goal, In progress, Next 3, Blocked / waiting, Decisions that still matter, Gotchas. One line each, with links, no pasted logs. Finished items go to your log. Over 60 lines, prune first. A reversed decision leaves the page."
jq -n --arg t "$text" '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$t}}'
