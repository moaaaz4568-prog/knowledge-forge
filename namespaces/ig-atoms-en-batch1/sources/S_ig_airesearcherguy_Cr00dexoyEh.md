---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Cr00dexoyEh.txt"
words: 283
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Cr00dexoyEh

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Cr00dexoyEh.txt` — حساب: airesearcherguy — إنستجرام — فيديو Cr00dexoyEh

---

How I use my automation bots in real life. Wait, what is this? It's an email from the government of Portugal in Portuguese, which I cannot read. Now I could use Google Translate, or. The user asked a question about an unclear message regarding the payment of taxes. The response explains that payment can be made through different channels, such as Multibanco, home banking, MB Way, institutions, or CTT branches. The message also informs about the possibility of signing up for direct debit and provides links to the Portal das Finanças for further information. The user is also advised to contact the e-BAUCÃO or the CAP for additional support. Lastly, the message encourages the use of the Portal das Finanças for simplified procedures. How I built that was first, I created a button in the Make. Com Android app. I could have used a trigger in Google Photos, but that's on a timer and I didn't feel like having to wait every time. So now I just push the button, it pulls however many photos I tell it to pull. Here I limit it to one, and I just make sure that the only photo in that album at any time is the one I want translated. This one grabs that media item ID and then feeds it to Google Cloud Vision, which uses OCR to scrape the text. Then I use GPT 3. 5. The system prompt is, you are a translator assistant. Summarize the information provided by the user that's in a foreign language and explain it in English. Then I pull the transcription, then I feed that to Google Cloud Text to Speech, and then that gets pushed through Telegram.