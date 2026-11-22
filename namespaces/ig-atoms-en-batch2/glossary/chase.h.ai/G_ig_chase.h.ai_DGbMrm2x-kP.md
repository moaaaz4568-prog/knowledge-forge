---
type: glossary
topic: chase.h.ai
aka: [APIs, API]
origin: sources/S_ig_chase.h.ai_DGbMrm2x-kP.md
---

# G_ig_chase.h.ai_DGbMrm2x-kP — APIs

## Term

In this source, APIs are the second of the three things a non-technical person must understand before building an AI agent: they are how the agent sends messages to its tools so they execute things on its behalf. The speaker defines the idea plainly — an API is just two programs talking to one another — and the term appears 3 times, beside tools, messages, and credentials, with the singular API twice for a single call. His concrete case is ChatGPT sending an email: it sends an API call to Google's Gmail saying who it is, giving its credentials, and giving the email to send. No deep technical knowledge is needed, only a top-level understanding of what happens under the hood, alongside what an agent is and which platform to build on.

## Synonyms

- API (singular form, in "An API is just two programs talking to one another")

## Live Example

> "An API is just two programs talking to one another." — sources/S_ig_chase.h.ai_DGbMrm2x-kP.md

## When the Meaning Breaks

- Read as code you must write: the speaker says you do not need deep technical knowledge of APIs, only a broad overview, and the agent itself makes the calls.
- Read as the agent doing the work directly: the agent never touches Gmail itself; it sends an API call and Gmail executes the send on its behalf.
