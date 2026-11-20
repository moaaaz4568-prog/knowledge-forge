---
type: atom
topic: instagram-transcripts
source: sources/S_ig_leadgenman_DTHsEFTEXrE.md
location: instagram/leadgenman
---

# T_DTHsEFTEXrE_01

"Let's build a news AI agent inside Anytone without you having to write a single line of code. First of all, head over to anytone. Io and log in or sign up with your account. Then the first thing you will search is AI agent. So it will look something like this, where the first thing we need to add is the brain of our AI agent, which is the chat model." — sources/S_ig_leadgenman_DTHsEFTEXrE.md

# T_DTHsEFTEXrE_02

"You can use any of these LLM models, but I usually start with OpenAI chat model. Then comes the part of memory. Memory allows our AI agent to recall past conversation and past history. So in this example, I'm using simple memory. And now to fetch news from the web, we need to have some sort of an API key. So let's search for news API key. So let's select this one news API." — sources/S_ig_leadgenman_DTHsEFTEXrE.md

# T_DTHsEFTEXrE_03

"Get your API key from here and in order to connect this with our AI agent, we are going to use an HTTP request node. Why we use HTTP request tool? Because it allows our AI agent and the API to talk in same language. So first of all, we need to select the method. So go back to news API and as you can see, the method is GET." — sources/S_ig_leadgenman_DTHsEFTEXrE.md

# T_DTHsEFTEXrE_04

"So we don't need to configure anything with the method, but we do need to add the URL here. So grab this URL which has the API key inside it and paste it here. That's all you need to do. And in order to send this news to our Gmail, we will include Gmail as a tool. Search for Gmail as a tool, connect your Gmail account and the operation is send." — sources/S_ig_leadgenman_DTHsEFTEXrE.md

# T_DTHsEFTEXrE_05

"Now for subject line and the email body, we want the AI to select on its own. So click on these stars. Awesome, that's all you need to do. Now let us click on open chats so that we can talk or chat with our AI agent. We can say, get me top five AI news from the last seven days. As you can see, our AI agent is now running." — sources/S_ig_leadgenman_DTHsEFTEXrE.md

# T_DTHsEFTEXrE_06

"It is fetching the current news by using this API key, formatting the answer by using ChatGPT and lastly invoking this Gmail as a tool to send out news to our Gmail. And there you go, top five AI news in the last seven days. I know the formatting can be much better, but this is just to show you how you can create an AI agent inside Anytone without you having to write a single line of code." — sources/S_ig_leadgenman_DTHsEFTEXrE.md
