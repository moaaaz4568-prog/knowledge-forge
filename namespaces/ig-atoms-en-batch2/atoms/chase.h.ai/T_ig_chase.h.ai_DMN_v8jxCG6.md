---
type: atom
topic: instagram-transcripts
source: sources/S_ig_chase.h.ai_DMN_v8jxCG6.md
location: instagram/chase.h.ai
---

# T_DMN_v8jxCG6_01

"Let me take you through an AI agent build that I just sold to a client this week for $5,000. Now on the surface, this looks super crazy, right? You got all this stuff going on, but I promise you it's actually pretty simple. So this particular AI agent lives inside of Slack and it's client-facing. And the big thing about it is it's trained on all of my client's internal documentation." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md

# T_DMN_v8jxCG6_02

"And that's what you see going on here in the red, this very complicated part. All that's happening here is it's taking files from Google Drive, it's extracting all the text, and then it's sending it to a vector database inside of Supabase. Now what's a vector database? That's just a fancy database that is perfect for large language models to be able to use and query. And for that, we use Supabase." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md

# T_DMN_v8jxCG6_03

"You can actually have a pretty robust free trial, and it's the program that we use to actually create the database and hook it up to our AI agent. So this AI agent is also using a re-ranking system with the RAG. In this case, I'm using Cohere. Check it out yourself. Actually really cheap to use. All that means is when we are using RAG for our AI agent, it's gonna pull in about 10 to 20 documents." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md

# T_DMN_v8jxCG6_04

"You can pull up to 100. And then the re-ranking system is gonna take those documents and then actually rank them based on which ones actually make sense to answer the question. Now you might think RAG would do that automatically, but it actually doesn't because it actually overemphasizes like speed and cost. So that's why we put the re-ranking system in there." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md

# T_DMN_v8jxCG6_05

"And then down here we have a cleanup system. So this makes sure that, hey, every single day this schedule trigger is gonna run and it's gonna see, hey, did we delete any documents inside of Google Drive? If yes, it goes ahead, it identifies which file IDs are orphaned. That's what you see here in the code, and then it deletes them." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md

# T_DMN_v8jxCG6_06

"And so taking all that together, we get a pretty robust RAG system that while on the surface looks very complicated, is actually pretty simple in its execution. And even better, it's something we can kind of copy and paste and have an 80% solution whenever we want to sell another RAG agent for another client." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md

# T_DMN_v8jxCG6_07

"And understanding these RAG agents is crucial because honestly, RAG itself probably counts for 50% of the automations and agents I sell. So if you want to get your hands on similar RAG templates like this, just comment RAG below and I'll send it to you for free." — sources/S_ig_chase.h.ai_DMN_v8jxCG6.md
