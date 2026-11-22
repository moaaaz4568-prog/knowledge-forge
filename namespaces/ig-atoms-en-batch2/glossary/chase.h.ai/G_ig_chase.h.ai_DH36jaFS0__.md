---
type: glossary
topic: chase.h.ai
aka: [webhook, webhooks]
origin: sources/S_ig_chase.h.ai_DH36jaFS0__.md
---

# G_ig_chase.h.ai_DH36jaFS0__ — webhook

## Term

In this source, webhook is the connection that lets Eleven Labs talk to the speaker's N8N agent, carrying voice and text in both directions. The word appears 9 times, beside voice, text, and message, with the plural webhooks twice for the pair of them. His concrete case is the setup: a voice webhook and a text webhook sit in N8N, and the Eleven Labs tool posts the user's request to the voice webhook, which passes it as a body parameter called message. The agent answers back through the same webhook, so the conversation flows like talking to a human, and the speaker also passes a conversation ID through the webhook so the agent knows which conversation to reference.

## Synonyms

- webhooks (plural form, in "through webhooks")

## Live Example

> "And webhooks are essentially just like, um, a way for us to pass information from Eleven Labs to our AI agent, in this case, inside N8N." — sources/S_ig_chase.h.ai_DH36jaFS0__.md

## When the Meaning Breaks

- Read as the voice itself: the webhook only passes information between Eleven Labs and N8N; the voice, the LLM, and the tools live on either side of it.
- Read as one connection for everything: there are two webhooks, one for voice and one for text, and the agent can run on either.
