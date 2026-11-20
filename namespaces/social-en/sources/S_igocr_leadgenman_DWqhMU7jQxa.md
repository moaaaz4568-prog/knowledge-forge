---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWqhMU7jQxa_1.txt"
words: 242
sha1: 18f84a527a06b6c0832cd2b8b043f24ed030b1a7
lang: en
account: leadgenman
quality: ocr+carousel-2
---

# S_igocr_leadgenman_DWqhMU7jQxa

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWqhMU7jQxa_1.txt`
> الأجزاء: 2 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWqhMU7jQxa_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DWqhMU7jQxa_4.txt`

<!-- image 1 -->
CLAUDE.md
Your AI's instruction manual.

You define:
• Project rules & conventions
• Code style preferences
• Architecture decisions

Without CLAUDE.md, Claude is just guessing.

1  # TiltIT -- Manthan's Project Instructions
2  ## Code Standards & Conventions
3  - TypeScript strict mode, no `any` types allowed
4  - Use @phosphor-icons/react for all icons
5  - Dark mode default, light mode must work from day 1
6  - Semantic Tailwind tokens (text-foreground, bg-muted)
7  ## Architecture & 3D Rendering Engine
8  - Three.js + React Three Fiber for 3D scene rendering
9  - Zustand + subscribeWithSelector for global state
10 - WebCodecs API + MediaEncoder for MP4 export pipeline
11  ## Commit Format (mandatory after every change)
12  - TI-XXX: Clear description of change (YYYY-MM-DD)
13  - Co-Authored-By: Manthan Patel
14  ## Never push unless Manthan says so. No exceptions.
<!-- image 4 -->
hooks
Automate before & after.

You define:
• Pre/post tool triggers
• Auto-format on save
• Shell scripts on events

Set it once, runs every time.

settings.json
1 {
2   "hooks": {
3     "PreToolUse": [
4       {
5         "matcher": "Edit|Write",
6         "command": "npm run lint -- --fix --quiet"
7       }
8     ],
9     "PostToolUse": [
10      {
11        "matcher": "Write",
12        "command": "npx prettier --write $FILE_PATH"
13      },
14      {
15        "matcher": "Bash",
16        "command": "echo Manthan: done $(date +%H:%M)"
17      }
18    ],
19    "Notification": [
20      {
21        "command": "terminal-notifier -title Manthan"
22      }
23    ]
24  }
25 }