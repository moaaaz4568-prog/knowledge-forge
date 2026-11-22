---
type: glossary
topic: chase.h.ai
aka: [Notion]
origin: sources/S_ig_chase.h.ai_DGVx595RO7r.md
---

# G_ig_chase.h.ai_DGVx595RO7r — Notion

## Term

In this source, Notion is the second half of the speaker's 60-second agent build: after Gmail can send mail, Notion gets a page for every email the agent sends. The name appears 7 times, beside Gmail, page, and email, and the speaker's setup is that the AI figures out the page title itself while he pastes in the parent page once. His concrete case is the test: he tells the agent to send an email and create a Notion page with that information, and the agent sends the mail, then hands back a link to the page. The build uses N8N with zero code, and the agent is ChatGPT with memory and tools until the Gmail and Notion tools are added.

## Synonyms

- No variant form of the term appears in this source.

## Live Example

> "I wanna connect to my Notion too. So when I tell it to send an email, it can also do stuff like, hey, create a new page inside Notion with details about the email it sent." — sources/S_ig_chase.h.ai_DGVx595RO7r.md

## When the Meaning Breaks

- Read as Notion doing the emailing: Notion only receives the page; Gmail sends the email, and the agent decides the subject, body, and recipient from the conversation.
- Read as a page for every chat: the Notion page is created per email the agent sends, with details about that email, not a log of the whole conversation.
