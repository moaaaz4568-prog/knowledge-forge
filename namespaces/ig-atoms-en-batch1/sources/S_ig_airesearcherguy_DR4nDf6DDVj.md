---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/DR4nDf6DDVj.txt"
words: 481
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_DR4nDf6DDVj

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/DR4nDf6DDVj.txt` — حساب: airesearcherguy — إنستجرام — فيديو DR4nDf6DDVj

---

I'm gonna explain what you're looking at in just a minute, but basically I recently built something that I call Context Mesh Lite, which is basically a really advanced hybrid RAG system. This is how it works. So currently hybrid RAG, so it's a retrieval augmented generation system that covers keyword and meaning search of your documents. I added SQL on top of that, so basically I added structured data on top of the unstructured data retrieval system. So it's a text, an agentic text to SQL system where the LLM can retrieve rows from tables in structured data adjacent to the unstructured data database. But going a step further, I also included graph search. So basically the LLM also extracts entities and actions and puts those in graph tables that are then retrieved to enrich the retrieval. So you'll have hybrid vector, which is vector embeddings as well as full text retrieval. On top of that, you'll have graph retrieval, which is gonna pull all of the relationships between two entities involved in the query. And then you'll also get row data from an SQL query in the event that a table exists that could support the retrieval. So what I have built, I built the Context Mesh Lite system. It's light because it exists fully in Supabase. So it's literally copy and paste the code, put it in Supabase, and then boom, run it. So what I built is the RAG battle arena, and this is a small program that takes 50 questions and throws it at both Context Mesh inside of Supabase as well as Qdrant standard vector database. And it looks at the responses and basically looks at the retrievals and sees does the answer to this query exist inside of the retrieval. And then it just compares the two and then gives it a score. So we're gonna go ahead and run it. All right, let's start the battle. All right, and the RAG arena battle is done. Now, I preface this by saying that Qdrant is a fantastic software and some of the best architecture for vector databases I've ever seen. What this does is it illustrates that even Context Mesh Lite, with its somewhat simple architecture inside of Postgres through Supabase, can provide enough context to be more accurate than a standard RAG system. The context rich answers allow an LLM that you connect it to to have all the information it might need to provide customer support, to provide internal intelligence to the team about any data, any information, be that customer data, be that internal policies. It really helps people in your organization to answer any question that might be needed because the LLM has full understanding of all of the data that's in your organization. That's Context Mesh Lite. Check it out at aiplusautomation. Com. Be well and do good things.