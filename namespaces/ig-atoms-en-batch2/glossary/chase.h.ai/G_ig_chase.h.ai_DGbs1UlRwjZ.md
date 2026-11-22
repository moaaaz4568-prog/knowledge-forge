---
type: glossary
topic: chase.h.ai
aka: [memory, Windows buffer memory]
origin: sources/S_ig_chase.h.ai_DGbs1UlRwjZ.md
---

# G_ig_chase.h.ai_DGbs1UlRwjZ — memory

## Term

In this source, memory is the second piece of the speaker's 60-second agent build, after the brain and before the tools: it lets the agent remember past conversations. The word appears 6 times, beside brain, tools, and Windows buffer memory, and the specific form is Windows buffer memory, which appears twice as the node he picks because it is the easiest. His concrete case is the setting itself: a content context length of five, so the agent remembers the last five messages given to it. With the OpenAI model as brain, Windows buffer memory as memory, and three tools to choose from, the agent decides from the conversation which tools to use.

## Synonyms

- Windows buffer memory (the specific n8n node the source uses for memory)

## Live Example

> "So click on memory and we're just going to do Windows buffer memory because it's the easiest." — sources/S_ig_chase.h.ai_DGbs1UlRwjZ.md

## When the Meaning Breaks

- Read as the agent remembering everything: the buffer keeps only the last five messages, so anything older than that is gone from its memory.
- Read as memory doing the thinking: memory only stores the conversation; the brain — the OpenAI model — decides, and the tools execute.
