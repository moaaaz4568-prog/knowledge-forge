---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DT0BvLtgn66.txt"
words: 265
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DT0BvLtgn66

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DT0BvLtgn66.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DT0BvLtgn66

---

Who the fuck is Giga Nigga? What the fuck? Who the fuck is Giga Nigga? Peter, when I write private or public, what actually happens in the back end? What changes happen under the hood? Think of it like this: the compiler turns your code into a big map of symbols, classes, fields, methods. When you add public or private, the compiler tags that symbol with a visibility flag. Okay. Then what? Then every time your code tries to access a field or call a method, the compiler first resolves which exact member is this, and immediately runs an access check. If the caller isn't allowed, the compiler refuses to build the program. So most access control happens before your app even runs. So private isn't like a lock on memory? Exactly. The data is still stored normally in memory. Private doesn't hide bytes, it just prevents other code from being allowed to generate instructions that touch those bytes. And inheritance? What happens there? Two big backend things. One, memory layout: derived objects usually contain the base object's fields inside them, so they can be treated like the base type. Two, method dispatch: if a method is overrideable, the runtime uses a method table so calls can jump to the derived version based on the object's real type. So the keywords are basically rules for the compiler, and inheritance is how memory and calls are wired. Exactly. Public, private, protected mostly affects what code the compiler is allowed to generate. Inheritance affects how objects are laid out and how overridden methods are called at runtime.