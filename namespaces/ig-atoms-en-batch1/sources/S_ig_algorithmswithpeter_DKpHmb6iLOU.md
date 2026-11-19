---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DKpHmb6iLOU.txt"
words: 272
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DKpHmb6iLOU

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DKpHmb6iLOU.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DKpHmb6iLOU

---

Hey Peter, I was using this app called Telegram and it says your chats are end-to-end encrypted. What does that even mean? Also, I kinda wish I had that feature for my conversations with Quagmire. Yeah Brian, some things are better off encrypted forever. But seriously, end-to-end encryption means that only the sender and receiver can read the message. Not even Telegram can peek. So how do they do that? Do they hide the text behind a picture of Joe's legs or something? I mean, that would scare off most hackers. But no, it's all math, baby. Telegram uses a protocol called MTProto. When you start a secret chat, your device and the recipient's device generate a pair of public and private keys. Then they use something called the Diffie-Hellman key exchange to agree on a shared secret. That secret is never sent over the internet, it's derived independently on both ends. Alright, sounds safe. But what if someone intercepts the data in the middle? They'd see total gibberish, like Meg trying to explain crypto. The data is encrypted using symmetric encryption AES-256 and protected in transit using RSA-2048. Plus Telegram adds hashing with SHA-256 to detect tampering. Basically, even if someone grabs the data without the secret key, it's useless. And what about the normal chats? Good catch. Not all Telegram chats are end-to-end encrypted. Only secret chats are. Regular chats are stored encrypted on Telegram's servers and decrypted on demand. Still secure, but Telegram technically can access them. So you're saying my 2 a.m. texts to Lois are safe? Well, from hackers, yes. From Peter Griffin screenshots, not so much.