---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_0.txt"
words: 780
sha1: d722810e47bb85f95913b9bf4a5011d1586b357c
lang: en
account: airesearcherguy
quality: ocr+carousel-10
---

# S_igocr_airesearcherguy_CopnagzrgcW

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_0.txt`
> الأجزاء: 10 — `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/airesearcherguy/CopnagzrgcW_9.txt`

<!-- image 0 -->
Level up your
automation game
with some Make.com
explainers
GPT-3 LinkedIn Post Creator
Ignore
Topic Rotator
LinkedIn
LinkedIn
<!-- image 1 -->
The Topic Rotator:
Tools
Variable name
Topic Rotator
Variable lifetime
One cycle
Variable value
switch( ( floor( random( 5 ) ) + 1 ) ; 1 : topic1 ; 2 : topic2 ; 3 : topic3 ; 4 : topic4 ; 5 : topic5 )
Cancel OK
Topic Rotator
Set variable
First, understand that you can input formulas in Make, much like excel or Google sheets
<!-- image 2 -->
The Topic Rotator:
Tools
Variable name
Topic Rotator
Variable lifetime
One cycle
Variable value
switch( ( floor( random * (5 - 1 + 1) ) + 1); 1; "topic1"; 2; "topic2"; 3; "topic3"; 4; "topic4"; 5; "topic5" ) )
Cancel OK
The formula in this example:
{{switch((floor(random * (5 - 1 + 1)) + 1); 1; "topic1"; 2; "topic2"; 3; "topic3"; 4; "topic4"; 5; "topic5")}}
Rotates through the numbers at random. Each number correlates to a topic.
<!-- image 3 -->
The Topic Rotator: (الدوار الموضوع: )
You don't need to know the formula...just understand why it works. (ما تشتيش تعرف المعادلة...فهم بس ليش تشتغل. )
If you want more formulas, YouTube is your friend (لو تبي معادلات أكثر، يوتيوب صديقك
<!-- image 4 -->
Pulling variables:
Search items
Collapse all
Topic Rotator 2 - Set variable
Topic Rotator A l...
Prompt
The prompt to generate completions for.
Max Tokens
2000
The maximum number of tokens to generate in the completion.
Defaults to 16.
Temperature
tokens to generate in the completion.
Next, understand that you can pull variables from a previous module into your current module...
<!-- image 5 -->
Pulling variables:
Search items
Collapse all
Topic Rotator 2 - Set variable
Topic Rotator A l...
Prompt
The prompt to generate completions for.
Max Tokens
2000
The maximum number of tokens to generate in the completion.
Defaults to 16.
Temperature
BUT, sometimes that requires running the scenario for the previous module first...so the data is there to pull.
<!-- image 6 -->
The OpenAI Module:
OpenAI GPT-3
text-davinci-003
Prompt
Prompt: Write a thought-provoking, well articulated LinkedIn post on the topic: "2. Posts resonate."
"Write it using the tone and personality of the examples provided.
Example Posts for tone and personality:
1) Example Post
Constraints: Do not include pretext or context, only return the LinkedIn post. LinkedIn post cannot exceed 3,000 characters.
The prompt to generate completions for.
Max Tokens
2000
The maximum number of tokens to generate in the completion.
Defaults to 16.
Temperature
1
What sampling temperature to use. Higher values mean the
Cancel OK
text-davinci 003 Enter your prompt
Max tokens always < 4000 (4k total for input and output)
Temp between 0.1 & 1...the higher the more "creative"
<!-- image 7 -->
The OpenAI Module:
OpenAI GPT-3
text-davinci-003
Prompt
Prompt: Write a thought-provoking, well articulated LinkedIn post on the topic "Success Stories".
Use it writing the tone and personality of the examples provided.
Example Posts for tone and personality:
1/ Example Post
Constraints: Do not include pretext or context, or start the LinkedIn post. LinkedIn post cannot exceed 3,000 characters.
The prompt to generate completions for.
Max Tokens
2000
The maximum number of tokens to generate in the completion.
Defaults to 16.
Temperature
1
What sampling temperature to use. Higher values means the model is more random.
Cancel OK
The prompt is what you tell the A.I. to get an output.
You can, and should, modify it (if you bought one of the templates) to fit your needs.
You won't break the A.I. by telling it to give you specific output. Play around with it.
<!-- image 8 -->
The HTTP Module:
HTTP
Body type
Raw
Content type
JSON (application/json)
Request content
{
  "key": "YOUR API KEY",
  "model_id": "YOUR MODEL ID OF CHOICE",
  "prompt": "Create a 100. Type Rotator image of a 96. Subject Rotator that is 97. Action Rotator in a 98. Setting Rotator in the art style 99. Style Rotator",
}
le Diffusion API C
Make a request
This makes an API call.
API calls get data and functionality from OTHER websites.
The API key is important as that gives the module access to the API, so you'll want to obtain your API key from the API service.
<!-- image 9 -->
The HTTP Module:
HTTP
Body type
Raw
Content type
JSON (application/json)
Request content
{
  "key": "YOUR API KEY",
  "model_id": "YOUR MODEL ID OF CHOICE",
  "prompt": "Create a 100. Type Rotator image of [Subject Rotator] that is 97. Action Rotator [Setting Rotator] in the art style [Style Rotator]",
}
le Diffusion API C
Make a request
Other than the API key, you typically won't modify much in the "Body" where the "JSON" code is that dictates what data/functions you'll retrieve from the API.
But, sometimes you will. Just don't mess with the format (where the curly brackets are)