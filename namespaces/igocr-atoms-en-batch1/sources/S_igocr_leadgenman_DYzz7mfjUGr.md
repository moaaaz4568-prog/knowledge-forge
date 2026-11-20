---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYzz7mfjUGr_0.txt"
words: 120
sha1: a94e2712cb074322d6f9fa9073e78cc11acf87dd
lang: en
account: leadgenman
quality: ocr
---

# S_igocr_leadgenman_DYzz7mfjUGr

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DYzz7mfjUGr_0.txt`

<!-- image 0 -->
.claude - tilt - leadgenman
EXPLORER
.claude
CLAUDE.md
agents
code-reviewer.md
debugger.md
hooks
pre-commit.sh
post-edit.sh
mcp
magician.json
notion.json
skills
remotion-edit.md
sounddefect.md
settings.json
remotion-edit.md
programmatic videos
---
name: remotion-edit
description: Compose programmatic videos
with Remotion v4
user-invocable: true
---
# Remotion Video Editing
Use this skill when Manthan asks to
"render a video", "build a Remotion comp",
or generate MP4s programatically.
## Project setup
- npx create-video@latest test
- Composition: 1080x1920 @ 30fps
- Audio: <Audio src={staticFile("vo.mp3")} />
## Build a scene
- One <Sequence> per beat
- spring() for entry, interpolate() for tween
- Stagger with delayRender + continueRender
- Use <Series.Sequence> for stacked beats
## Typography & motion
.cLAUDE CODE SETUP
The .claude folder that makes
Claude Code 10x sharper