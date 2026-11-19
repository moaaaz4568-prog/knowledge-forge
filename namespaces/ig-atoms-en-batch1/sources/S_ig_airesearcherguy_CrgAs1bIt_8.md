---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CrgAs1bIt_8.txt"
words: 550
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CrgAs1bIt_8

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CrgAs1bIt_8.txt` — حساب: airesearcherguy — إنستجرام — فيديو CrgAs1bIt_8

---

A lot of people asked me for this one, so I finally found a way to create an AI-powered automation for Pinterest, sort of. What I mean by sort of is I wish that I could create a template and give it to you like I do with my other automations, but unfortunately I cannot replicate this in make. Com. I can only do it in Zapier, and the only way to share a template is to have their $400 a month plan, which I do not have. So instead I'm gonna show you step by step how to do this. The trigger is a scheduler. This is where you have it run on a schedule. This is really simple. You can do it every day, every hour, however you want. Now because I want this to post AI art to my Pinterest, I have put in here some formatters that will rotate through different variables. If you want to do the same, you would use utilities, and then the action would be choose random, and then you put a bunch of inputs. So this is my subject for the AI art. And then I have another formatter that chooses through actions. Then I have GPT create a prompt. Use the following subject and action information to create a relevant prompt for an AI text to image program. And then this takes the outputs. Temperature is set to one, and then the system prompt is you are a text to image AI prompt creator. Real simple. But then I have another formatter, and this one is a text formatter, and that just trims whitespace. Then custom request in webhooks, and then this is the JSON for the stable diffusion API, just like I have in my automations in make. Com. You have your API key, the model ID, prompt, which is the previous output, the negative prompt, height and width, upscale, that doubles the size of the image. Self-attention makes it a little bit crisper of an image. Enhanced prompt turns the prompt into a better prompt. One sample, inference steps, you got to do 21, 31, 41, or 51. Guided scale, default to 7. 5. Content type application JSON is the only header. And then we have paths, and the reason is because the stable diffusion API is either gonna return a success or processing. So path A, the status exactly matches success, and then the next step is to create a pin, and you just attach your account, and then the action, you choose the board, and then you take the output URL, and then whatever text and description. You might want to add another GPT module to create these. And then path B is in case the status is processing. Then we're gonna delay for five minutes, then we do another custom request, and this time the URL is the fetch results URL, and then the only data is your API key and the JSON, with the content type as application JSON and the headers. And then you can publish that to your Pinterest. And that is how you automate Pinterest pins through Zapier. And here's the result. We have two images right here, complete with my title and description. I could have also added a link.