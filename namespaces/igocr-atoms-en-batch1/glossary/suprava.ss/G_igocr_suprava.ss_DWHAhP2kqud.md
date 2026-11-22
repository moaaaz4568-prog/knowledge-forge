---
type: glossary
topic: suprava.ss
aka: [InMail, InMails]
origin: sources/S_igocr_suprava.ss_DWHAhP2kqud.md
---

# G_igocr_suprava.ss_DWHAhP2kqud — InMail

## Term

InMail here is one of the two LinkedIn channels the Claude Code system runs — the system finds leads on LinkedIn, sends connection requests and InMails, and classifies cold email replies. The word appears twice, once as 'InMails' and once in 'InMail Queue', beside 'connection requests', 'Sample Leads', and 'Blacklist'. The spreadsheet Claude builds has four tabs — Sample Leads, Blacklist, InMail Queue, and Connection Queue — and the n8n workflow moves warm or hot replies into the queue by priority. An InMail in this source is a queued message to a lead, not a cold blast.

## Synonyms

- InMails (plural form used in the source)

## Live Example

> "Suprava Sabat Step 2: Build the spreadsheet Open Claude Code → paste the spreadsheet prompt Claude builds 4 tabs: • Sample Leads • Blacklist • InMail Queue • Connection Queue Replace sample leads with your real list." — sources/S_igocr_suprava.ss_DWHAhP2kqud.md

## When the Meaning Breaks

- Read as LinkedIn's paid messaging feature in general: InMail here is a queue inside a spreadsheet the system manages — leads enter it by priority after a warm or hot reply, not by buying credits.
- Read as the same as a connection request: the system sends both, but they sit in separate queues — InMail Queue and Connection Queue — and the workflow treats them as different steps.
