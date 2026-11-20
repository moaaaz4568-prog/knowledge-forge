---
type: atom
topic: instagram-ocr
source: sources/S_igocr_leadgenman_DYHc5riDUFn.md
location: instagram/leadgenman
---

# T_DYHc5riDUFn_01

"CLAUDE.md Your AI's instruction manual. You define: • Project rules & conventions • Code style preferences • Architecture decisions Without CLAUDE.md, Claude is just guessing." — sources/S_igocr_leadgenman_DYHc5riDUFn.md

# T_DYHc5riDUFn_02

"skills/ Capabilities Claude picks on its own. What it does: • Model-invokable. Claude decides when to load • One folder per skill. SKILL.md inside • Persistent across every session Skills are the new prompts. 1 --- 2 name: ui-ux-pro-max 3 description: Design intelligence on tap 4 --- 5 6 # UI/UX Pro Max 7 Use this skill when building any UI. 8 50 styles, 21 palettes, 50 font pairs." — sources/S_igocr_leadgenman_DYHc5riDUFn.md

# T_DYHc5riDUFn_03

"commands/ Slash commands you trigger by name. What it does: • Each .md file becomes /command-name • You decide when to run it • Pre-built workflows on tap Type /commit. Claude does the rest. 1 --- 2 description: Analyze diff and write commit msg 3 --- 4 5 # /commit 6 Run `git status` and `git diff --staged`. 7 Identify the *why*, not the *what*." — sources/S_igocr_leadgenman_DYHc5riDUFn.md

# T_DYHc5riDUFn_04

"hooks/ Shell scripts that always fire. What it does: • Run before or after Claude tool calls • Block dangerous commands automatically • No prompt. No exception. Always fires. Hooks are your guardians. 1 #!/usr/bin/env bash 2 # Auto-format every file Claude edits. 3 FILE=$(jq -r .tool_input.file_path) 4 5 case" — sources/S_igocr_leadgenman_DYHc5riDUFn.md

# T_DYHc5riDUFn_05

"plugins/ First-class in 2026. What it does: • Bundles agents, commands, hooks, MCP scales. • Install once. Use forever. • Share across projects + teammates Plugins are how Claude scales. {" — sources/S_igocr_leadgenman_DYHc5riDUFn.md

# T_DYHc5riDUFn_06

"settings.json The control panel. You control: • Which tools Claude can use • Which model. Permissions per directory. • Hook registry. Output style. Statusline. One file. Everything Claude is allowed to do. 1 { 2" — sources/S_igocr_leadgenman_DYHc5riDUFn.md

# T_DYHc5riDUFn_07

"and I'll send it. super devs aren't writing better prompts. they have a better .claude/." — sources/S_igocr_leadgenman_DYHc5riDUFn.md
