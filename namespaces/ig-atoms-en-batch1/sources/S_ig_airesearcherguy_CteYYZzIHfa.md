---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CteYYZzIHfa.txt"
words: 326
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CteYYZzIHfa

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CteYYZzIHfa.txt` — حساب: airesearcherguy — إنستجرام — فيديو CteYYZzIHfa

---

I found a no-code way to do vector embedding searches. It was one of those situations where you're searching all over the internet for the answer to something and stumble upon a random help forum where somebody shares a golden nugget. Let me show you. First of all, because I don't ever use Zapier, I didn't even realize that it has a search embeddings in OpenAI module. So we start with a text formatter. We're gonna use split text. And here I pasted the research paper, The Joy of Ranking, which is all about how Amazon's search ranking algorithm works. I used a period as the separator because I wanted full sentences. And when it separated, it chunked it out like this. Then I connected the OpenAI search embeddings module, and I chose a query. You just make a query based on the input. And then under documents, you put the output from the text formatter. And what it does is it embeds and vectorizes the documents, the text formatter output, and then based on your query brings back the most logical answers. And they're ranked by a score. Now the search itself may not be that valuable because all it really does is pull mainly any text that has an exact match or close exact match to your query. But the next module is a conversation module with ChatGPT. Here we use the same query, but we put the top five ranking results from the embedding search in the system instructions. And my query got a very robust answer, and it was based on information from that document. So this is a no-code way to build a Q&A bot based on embeddings search. Now, unfortunately, this doesn't create a vector database, so every time you run it, it's going to re-embed and re-vectorize all of your inputs. But the embeddings price was just dramatically decreased, so for small tasks, this could be really cool. Cheers.