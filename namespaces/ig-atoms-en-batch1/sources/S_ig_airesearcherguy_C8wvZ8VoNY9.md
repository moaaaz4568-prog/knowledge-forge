---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C8wvZ8VoNY9.txt"
words: 476
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C8wvZ8VoNY9

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C8wvZ8VoNY9.txt` — حساب: airesearcherguy — إنستجرام — فيديو C8wvZ8VoNY9

---

How do you upload documents into your vector database using Make.com? So uploading documents into a vector database can actually be kind of complex. It involves taking a document, splitting up the text in that document, and then embedding each of those blocks of split up text using an AI service like OpenAI, then taking those embeddings and then putting those into your vector store. Well, I figured out how to do all of that using Make.com, uploading documents into a vector store that I created in Qdrant, and I'd like to show you how I did it. Now let's talk about how to upsert documents into your Qdrant vector data store using Make.com. So the trigger is a form. This is very simply just a form that takes a file. Once I submit a file, it is then downloaded into Make here and it triggers this flow. And then this first HTTP get a file module actually uploads that file into the Make.com system. This set multiple variables module is the first to help with the process of splitting the text into chunks. In order to upload it into a vector store, it needs to be split up. So first we turn that data into words again. So it comes out as base64, and then this two string to binary formula here takes that base64 and turns it back into text. And then here we also set the chunk size to 4, 000 characters. You can make this whatever you like, but I like to use 4, 000 character chunks. The repeater repeats however many times is necessary in order to make sure that the entire length of the text is broken up into 4, 000 character chunks. By using this length, so this spits out a number of however many characters the text is, and then we divide that by the chunk size, and that's how many times it'll repeat. And then this last set variable actually does the splitting, does the chunking. Then we take the results of that chunk split and transform it to a JSON because it needs to be in JSON format for the API call. This is a GPT API call, so make an API call to the v1 embeddings URL in order to embed that chunk of text in the JSON string. We use text embedding three small because it is the most inexpensive and efficient of the embedding models. And then this aggregator aggregates all the embeddings because there's going to be 1, 536 of them, all little strings of numbers. So we have to grab all of those and put them in one block, and that's what the text aggregator does. Then we have an increment function, and the reason is because the embeddings need to be labeled. And then we have this HTTP API call.