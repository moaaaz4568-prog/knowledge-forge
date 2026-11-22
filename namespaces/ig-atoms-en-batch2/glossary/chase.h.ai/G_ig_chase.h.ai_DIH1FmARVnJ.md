---
type: glossary
topic: chase.h.ai
aka: [RSS feeds]
origin: sources/S_ig_chase.h.ai_DIH1FmARVnJ.md
---

# G_ig_chase.h.ai_DIH1FmARVnJ — RSS feeds

## Term

In this source, RSS feeds are the second of the two things needed to build the custom newsletter: free links for a chosen topic, fetched from ChatGPT, that feed the n8n workflow. The phrase appears 3 times, beside n8n, schedule, and Gmail, and the speaker's example is AI news feeds found by asking ChatGPT. His concrete case is the flow: a schedule trigger runs every morning, a code module holds the feed URLs as JSON, a loop feeds an RSS read module, and an aggregate module packs 20, 40, 60, or 100-plus items into a single list for the LLM. The LLM chain then picks the most relevant articles by the system prompt's criteria, and Gmail delivers the finished newsletter with headline, source, and summary.

## Synonyms

- No variant form of the term appears in this source.

## Live Example

> "So the two things you're gonna need is one, n8n, which you can do with a free trial, and two, you're just gonna need some RSS feeds." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

## When the Meaning Breaks

- Read as the newsletter itself: the feeds are only the raw input; the LLM picks and summarizes, and Gmail delivers the finished newsletter.
- Read as a paid input: RSS feeds are totally free, and the speaker gets them just by asking ChatGPT for links on a topic.
