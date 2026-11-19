---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Cn0P87zuhjb.txt"
words: 409
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Cn0P87zuhjb

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Cn0P87zuhjb.txt` — حساب: airesearcherguy — إنستجرام — فيديو Cn0P87zuhjb

---

I just created an epic AI-powered creative assistant to help my whole team with things like writing blogs, sales pages, Facebook ads, and more. Let me show you how I did it. Alright, first I'll show you how it works. So I built this as a messenger bot, and basically you answer a few questions through the bot. It asks what you're writing today, blog article, sales page, Facebook page, Amazon listing optimization. You choose one, and then it asks you a handful of questions. So let me answer those and I'll show you the result. I still haven't quite figured out the formatting issue, but since this is an internal tool, I'm not super worried about it. But here I get a number of things from OpenAI. When I take all that data out of the email, I get headlines, an outline, questions, answers to those questions. This is really good information. Now let me show you how I built this. So it all starts with a Chatfuel chatbot, and this is where the first question leads you down the path. This is where the question, what are you writing today, comes in, and then based on what is clicked, so somebody clicks the sales page, for example, then it asks a number of questions about the product so that the AI has plenty of information to offer good suggestions. And then at the end of that module, there's going to be a JSON request, which is created in make. Com. Let me show you how. So over in Make, every single one of those different types of copy have their own scenario. So the one I was just looking at was the sales page. And when you create a JSON listener as the trigger in Chatfuel, it gives you a webhook, and that's what you paste down here, and then it'll push all this information into that webhook. And once that information is available, you have your OpenAI GPT prompts. This one asks to provide sales page headline ideas. This one asks to provide an outline for what the sales page should look like. This one asks for persuasive bullet points that can be included in the sales copy for the page. And then at the end, it is emailed. And now my whole team can get assistance from the AI just by answering a few questions every time they're going to take on a writing task.