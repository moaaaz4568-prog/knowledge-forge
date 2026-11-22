---
type: glossary
topic: chase.h.ai
aka: [email sub-agent, sub-agent]
origin: sources/S_ig_chase.h.ai_DIiAkpHNaGx.md
---

# G_ig_chase.h.ai_DIiAkpHNaGx — email sub-agent

## Term

In this source, an email sub-agent is the part of the speaker's AI agent setup that handles mail: hooked to Gmail modules and a contact database, it knows a person's contact information from their name alone, and when a new message arrives a text classifier decides whether it is an FAQ email or a lead email, then drafts a reply in his voice for a thumbs up or thumbs down. The phrase appears twice, beside sub-agent, orchestrator agent, and text classifier, and it sits under the orchestrator agent he talks to by voice. His concrete case is the inbound lead reply, where the draft is created automatically every single time someone reaches out with a question.

## Synonyms

- sub-agent (the shorter form the speaker uses for the same pieces)

## Live Example

> "Let me show you my AI agent setup and how the email sub-agent works." — sources/S_ig_chase.h.ai_DIiAkpHNaGx.md
> "So I just kind of wanted to show you how the email sub-agent works." — sources/S_ig_chase.h.ai_DIiAkpHNaGx.md

## When the Meaning Breaks

- Read as the whole setup: the email sub-agent is one piece under the voice-driven orchestrator agent, so crediting it with routing every tool call would confuse it with the orchestrator.
- Read as auto-send: it creates drafts for his approval, never sends on its own, so a sent email would not be this sub-agent doing its job.
