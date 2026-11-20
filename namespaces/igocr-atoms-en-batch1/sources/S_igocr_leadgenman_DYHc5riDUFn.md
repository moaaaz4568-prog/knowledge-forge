---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_1.txt"
words: 574
sha1: ab378bb49ab9cfb916f9ad30afb756c020e8dfa8
lang: en
account: leadgenman
quality: ocr+carousel-7
---

# S_igocr_leadgenman_DYHc5riDUFn

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_1.txt`
> الأجزاء: 7 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYHc5riDUFn_8.txt`

<!-- image 1 -->
CLAUDE.md
Your AI's instruction manual.

You define:
• Project rules & conventions
• Code style preferences
• Architecture decisions

Without CLAUDE.md, Claude is just guessing.

Manthan's Project Instructions
# NotifyMotion --
## Code Standards & Conventions
- TypeScript strict, no 'any' types
- @phosphor-icons/react for all icons
- Dark mode default, light works day 1
## Architecture
- Canvas 2D + Zustand for global state
- WebCodecs + MediaRecorder for MP4 export
## Commit Format (after every change)
- NM-XXX: clear description
- Co-Authored-By: Manthan Patel
## Never push unless Manthan says so.
<!-- image 2 -->
skills/
Capabilities Claude picks on its own.

What it does:
• Model-invokable. Claude decides when to load
• One folder per skill. SKILL.md inside
• Persistent across every session

Skills are the new prompts.

1 ---
2 name: ui-ux-pro-max
3 description: Design intelligence on tap
4 ---
5
6 # UI/UX Pro Max
7 Use this skill when building any UI.
8 50 styles, 21 palettes, 50 font pairs.
9
10 ## When to invoke
11 – User says "design" or "build a UI"
12 – File is .tsx, .vue, .svelte, .html
13 – Project is dashboard or SaaS
14 ## Reference
15 – shadcn/ui MCP for examples
16 # Claude loads this on its own.
<!-- image 4 -->
commands/
Slash commands you trigger by name.
What it does:
• Each .md file becomes /command-name
• You decide when to run it
• Pre-built workflows on tap
Type /commit. Claude does the rest.
1 ---
2 description: Analyze diff and write commit msg
3 ---
4
5 # /commit
6 Run `git status` and `git diff --staged`.
7 Identify the *why*, not the *what*.
8
9 ## Format
10 - Subject: 50 chars, imperative mood
11 - Body: explain the reasoning
12 - Use NM-XXX prefix
13 ## Never
14 - Push without asking
15 - Use --no-verify
16 # Slash commands = fastest UX.
<!-- image 5 -->
hooks/
Shell scripts that always fire.

What it does:
• Run before or after Claude tool calls
• Block dangerous commands automatically
• No prompt. No exception. Always fires.

Hooks are your guardians.

1 #!/usr/bin/env bash
2 # Auto-format every file Claude edits.
3 FILE=$(jq -r .tool_input.file_path)
4
5 case "$FILE" in
6   *.ts|*.tsx|*.js|*.jsx)
7     npx prettier --write "$FILE" ;;
8   *.py)
9     ruff format "$FILE" ;;
10  *.go)
11    gofmt -w "$FILE" ;;
12 esac
13
14 # Fires after every Edit.
15 # No questions asked.
<!-- image 6 -->
plugins/

First-class in 2026.

What it does:
• Bundles agents, commands, hooks, MCP scales.
• Install once. Use forever.
• Share across projects + teammates

Plugins are how Claude scales.

{
  "name": "claude-finance",
  "version": "1.0.0",
  "description": "Finance agents by Anthropic",
  "author": "anthropic",
  "agents": [
    "risk-officer",
    "market-analyst",
    "portfolio-manager", "trade-executor",
    "compliance-checker", "research-assistant"
  ],
  "commands": ["analyze", "rebalance"],
  "mcp_servers": ["bloomberg", "yahoo-finance"]
}

# Run /plugin install claude-finance.
# Once. Then forever. claude-finance.
<!-- image 7 -->
settings.json
The control panel.
You control:
• Which tools Claude can use
• Which model. Permissions per directory.
• Hook registry. Output style. Statusline.
One file. Everything Claude is allowed to do.
1 {
2   "model": "claude-opus-4-7",
3   "permissions": {
4     "allow": [
5       "Bash(npm run *)", "Bash(git *)",
6       "Read", "Edit", "Glob", "Grep"
7     ],
8     "deny": ["Bash(rm -rf *)"]
9   },
10  "hooks": {
11    "PostToolUse": [".claude/hooks/format.sh"]
12  },
13  "outputStyle": "terse",
14  "statusLine": ".claude/statusline.sh"
15 }
16 # Permissions, model, hooks. All here.
<!-- image 8 -->
Comment
"MAP"
and I'll send it.
super devs aren't writing better prompts.
they have a better .claude/.