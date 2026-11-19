---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Czl4pFqoR28.txt"
words: 534
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Czl4pFqoR28

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Czl4pFqoR28.txt` — حساب: airesearcherguy — إنستجرام — فيديو Czl4pFqoR28

---

Did you know your custom GPTs can take actions? Meaning they can interface with other software through API calls. You want to know how to add that to your custom GPTs? Check it out. Let's go over to the explore tab first. This is where you're going to create a GPT. Right, I've already done that, so I'm going to push edit, right? Go under configure, go to actions, add action, go here to get weather data. This is a schema. I'm assuming that if you're watching this, you're probably not a developer like me, and you probably don't know how to write a schema. So just do that, then come back to ChatGPT. Tell ChatGPT, I am building a custom GPT. I would like to add an API call action. This requires a schema. Here is an example schema. API call I want to make is here. And then you grab the API call that you want to make. So I'm going to pretend like I want to create a custom GPT that can give me keyword suggestions. So I found this keyword suggestion API on RapidAPI. Just going to come over here and copy the code, come back over here and tell GPT this is the API call I want to make. Please write a schema. And after some long minutes, I have the schema. Then I'm going to go back to the explore tab, go edit my GPT, configure. I'm going to delete this. I don't need the weather. I want keywords. Add action. I'm going to paste that schema right here. Here's the thing. That's a RapidAPI API call, so it requires authentication. So got to come in here to API key and then choose custom because it's not a basic bearer. I'll show you that in a second. As you can see here, it is X Rapid API key. I'm going to copy that, paste that right here, and then paste my API key in here. Click save. Now here's the other thing you might have noticed that there are multiple headers, not just the API key, but there's another header in there. That's okay, not a problem. Check it out. So you hit the back key. Now we have our action. Now in the instructions, I can add that other header. You are a keyword suggestion bot. You get keywords from the keyword suggestion API. Each API call will require an additional header. Please assign the following values to the corresponding parameters. Language equals EN, country equals US. So not only do I have the additional header, but these are parameters that every API call has to include. I just tell it right here in the instructions to add that. Now if we go to the preview, please give me keyword suggestions for yoga mat. So as you can see, it's making the API call. Now it's going to ask me if I trust the information that's being passed back and forth. If I press always allow, it won't ask me that anymore. And boom, it made the API call. And that is how you add API calls as actions to your custom GPTs. Hope that helps. Cheers.