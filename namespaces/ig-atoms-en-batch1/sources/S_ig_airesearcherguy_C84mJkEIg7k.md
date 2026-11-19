---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C84mJkEIg7k.txt"
words: 551
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C84mJkEIg7k

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C84mJkEIg7k.txt` — حساب: airesearcherguy — إنستجرام — فيديو C84mJkEIg7k

---

Now, once you have documents inside of your vector store, what do you do with them? Well, in make. Com, you can also call your vector store and get back chunks of data that you can use to feed AI for a number of different things. I use it in my personality vector, and here's how. Now that you have a Qdrant cluster filled with a vector store with tons of collections of data, what do you do with it? Well, I'll show you what I do with mine as an example of how you can use make. Com to query your vector store. In this particular scenario, I start with a WordPress watch posts trigger. So whenever I publish a new article on my website, it will be sent through this scenario. This transform to JSON is the system prompt for AI. This is where I tell AI, I'm going to give you all of this context and I want you to use it to generate content that sounds like me. All right, so here we have the make an API call, which is an embeddings, and this is because we need to embed the query for the vector store. So here, make an API call to OpenAI V1 embeddings. What we're embedding, what the query is going to be for the vector store is the title of the article. And then the text aggregator puts all of those embeddings together. Then the next module is a GPT-4 module where I basically tell it there are three expert databases that we can access, but I need to know which one to access. So based on this article title and the article excerpt, return which expert database this is in regarding. And the reason I do that is because I have three expert databases inside of my Qdrant cluster, one about AI, one about consumer psychology, behavioral psychology, and then one about copywriting and marketing. And I like to talk about all three of those things. So when I write an article and it has to do with one of those three things, this GPT module is going to determine based on that article which of those expert databases need to be queried. Then we have the first Qdrant query, right? So http your cluster URL slash collections and then the name of the collection. In this case, it's going to be the output of the previous module slash points slash search, and it's searching that collection for, and then here's the vectors joined, split and then joined so that all the spaces are out. And then it's searching that collection for the vectors, which are the vectorized title of the article, which happened over here. So remember, this is the vectors from the query. Now we are querying one of the knowledge bases, one of the expert knowledge base collections for that information. Then we have the conscience database. This is a database that's filled with personal questions and answers, world philosophies, etc. We also query that one. Then we have the social writing database. This is a database with a whole bunch of LinkedIn and Facebook posts from me, and it serves as kind of the writing sample or writing example database, which we pull from that as well.