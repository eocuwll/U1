#!/usr/bin/env bash
# Install Claude Code skills from this repository into ~/.claude/skills/
set -euo pipefail

SKILLS_SRC="$(cd "$(dirname "$0")/skills" && pwd)"
SKILLS_DST="$HOME/.claude/skills"

if [ ! -d "$SKILLS_SRC" ]; then
  echo "ERROR: skills/ directory not found next to this script." >&2
  exit 1
fi

echo "Installing Claude Code skills to $SKILLS_DST ..."

for skill_dir in "$SKILLS_SRC"/*/; do
  skill_name="$(basename "$skill_dir")"
  dest="$SKILLS_DST/$skill_name"
  mkdir -p "$dest"
  cp -r "$skill_dir"* "$dest/"
  echo "  ✓ $skill_name"
done

echo ""
echo "Done. Restart Claude Code (or open a new session) to use the skills."
echo "Available skills:"
for skill_dir in "$SKILLS_SRC"/*/; do
  skill_name="$(basename "$skill_dir")"
  desc=$(grep -m1 '^description:' "$skill_dir/SKILL.md" 2>/dev/null | sed 's/^description: *//' | cut -c1-80 || echo "")
  echo "  - $skill_name: $desc"
done
