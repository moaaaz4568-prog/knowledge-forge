---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWTkzADDVxe_1.txt"
words: 189
sha1: adabfef25ea055ea903e95e98b5eb61308e71849
lang: en
account: leadgenman
quality: ocr+carousel-3
---

# S_igocr_leadgenman_DWTkzADDVxe

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWTkzADDVxe_1.txt`
> الأجزاء: 3 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWTkzADDVxe_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWTkzADDVxe_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWTkzADDVxe_9.txt`

<!-- image 1 -->
What are Skills?

BEFORE
CLAUDE . md
✗ Loads every single session
✗ Gets bloated over time
✗ One giant file for everything
✗ Can not scope to a task
✗ No on-demand loading
✗ Hard to share across projects

AFTER
Skills/
✓ Load on demand via /skill
✓ Stay lean and focused
✓ One folder per skill
✓ Scoped to specific tasks
✓ Auto-detected by Claude
✓ Share across any project

Skills are modular instruction files that Claude loads only when you need them.
<!-- image 8 -->
Create Your Own Skill
in 3 steps

1 Create the folder
mkdir -p .claude/skills/my-skill/
Each skill lives in its own directory.

2 Write SKILL.md
---
name: my-skill
description: What this skill does.
user-invocable: true
---
# My Custom Skill
Instructions for Claude go here.
Be specific. Give examples.
Frontmatter tells Claude what this skill does, so it knows when to load it.

3 Done. Claude auto-detects it.
claude "use /my-skill to build X"
No config. No setup. Just works.
Pro tip: add tools: in frontmatter to give your skill access to Read, Grep, Bash, etc.
<!-- image 9 -->
Save this.
Comment
"SKILLS"
for the full setup guide