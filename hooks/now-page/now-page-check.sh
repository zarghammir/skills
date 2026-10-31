#!/bin/bash
# PostToolUse on Write|Edit: a NOW page stays one page.
dir="${NOW_PAGES_DIR:-$HOME/.claude/now}"
file=$(jq -r '.tool_input.file_path // .tool_response.filePath // ""')
[[ "$file" == "$dir"/*.md ]] || exit 0
[[ -f "$file" ]] || exit 0
lines=$(wc -l < "$file" | tr -d ' ')
problem=""
(( lines > 60 )) && problem="This NOW page has $lines lines, over the 60 limit. Prune it before doing anything else: move finished items to your log."
head -3 "$file" | grep -q '^Updated:' || problem="$problem This NOW page has no Updated: line near the top."
[[ -n "$problem" ]] || exit 0
jq -n --arg t "$problem" '{hookSpecificOutput:{hookEventName:"PostToolUse",additionalContext:$t}}'
