---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C1rmXHIoXC9.txt"
words: 455
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C1rmXHIoXC9

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C1rmXHIoXC9.txt` — حساب: airesearcherguy — إنستجرام — فيديو C1rmXHIoXC9

---

So I've been working on these virtual workforce automations. I'm trying to make them better, and recently I read an article that talked about the limitations of RAG, which is basically the vector store connects to a retrieval system in AI. And that limitation is if the query is outside of the content of the files inside of the vector store, the AI may hallucinate. So how do you improve on that? The article suggested adding a web search capability. Obviously, the easiest way to do this in no code would be if OpenAI would allow web search for GPT Assistants. Since they don't, a little complicated, but here's what I had in mind. So first, you would create your vector store in Voiceflow. Then in your no code workflow, you connect that to GPT. You submit your query. The query would pull from the vector store and Voiceflow, and then you would give it to GPT and say, this is the query. Here's the context from the vector store. Step one, determine whether or not you can accurately and sufficiently respond to the query with the information in this vector store. Then ask it to indicate yes or no. That's step one. The answer is yes, then you can say, okay, answer the query. The answer is no, then you would run a Google search using the custom search engine API. Then you'd have to pull in all of the titles and meta descriptions for the search results. Give that to GPT and say, okay, since you indicated that the vector store didn't have the information necessary to complete this query, here are the top 10 web search results, their titles and meta descriptions. Do any of these look like they might provide sufficient information to finish the query? Please choose one. And then GPT would come back with the title of one of the articles. You would match that with one of the titles, open up the page, scrape the page, give GPT the scraped information, and then ask, did this give you sufficient information to answer the query, yes or no? And then this would be a loop process until the final answer was yes, I have the sufficient information to answer the query. Anyway, all of this would probably be a ton easier to actually code, but it can be done in no code. I don't think Make is the right platform for it though, since Make really doesn't support looping. I'm probably gonna open a N8N account soon so that I can play with their looping function and see if I can't use that. Anyway, hopefully that made sense to anybody trying to build something similar. Hopefully that helps. Cheers.