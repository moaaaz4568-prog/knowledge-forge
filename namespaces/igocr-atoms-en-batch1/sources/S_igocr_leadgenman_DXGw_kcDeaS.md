---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DXGw_kcDeaS_4.txt"
words: 134
sha1: 9897be296baac0c89bc3b5b39fe7684f712917e7
lang: en
account: leadgenman
quality: ocr+carousel-2
---

# S_igocr_leadgenman_DXGw_kcDeaS

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DXGw_kcDeaS_4.txt`
> الأجزاء: 2 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DXGw_kcDeaS_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DXGw_kcDeaS_9.txt`

<!-- image 4 -->
hooks/ -- deterministic rails
EXPLORER
.claude/
.claude/hooks/ --
deterministic
automation
Hooks fire on lifecycle events.
PreToolUse, PostToolUse, Stop, SessionStart.
Unlike CLAUDE.md, hooks ALWAYS run.
For anything that MUST happen, open automatically.
{
  "hooks": [
    {
      "PreToolUse": {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "grep -q && exit 2"
          }
        ]
      }
    },
    "PostToolUse": [
      {
        "matcher": "Edit [Write]",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write"
          }
        ]
      },
      {
        "type": "command",
        "command": "run lint --silent"
      }
    ]
  }
}
CLAUDE.md suggests. Hooks run every time -- guaranteed.
<!-- image 9 -->
steal this -- comment STARTER
EXPLORER
your-project/
CLAUDE.md
CLAUDE.local.md
.claude/
agents/
code-reviewer.md
debugger.md
test-writer.md
refactorer.md
doc-writer.md
security-auditor.md
hooks/
pre-commit.sh
lint-on-save.sh
session-start.sh
rules/
api.md
database.md
frontend.md
skills/
commit-push-pr/
SKILL.md
review-pr/
SKILL.md
.mcp.json
settings.json
settings.local.json
CLAUDE
local
hooks
skills
settings
your-project > steal this
COMMENT
"STARTER"