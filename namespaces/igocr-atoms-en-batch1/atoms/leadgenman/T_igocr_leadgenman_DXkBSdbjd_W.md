---
type: atom
topic: instagram-ocr
source: sources/S_igocr_leadgenman_DXkBSdbjd_W.md
location: instagram/leadgenman
---

# T_DXkBSdbjd_W_01

"coding in 1997 JS sum.js 1 function sumArray(nums) { 2 var total = 0; 3 for (var i = 0; i < nums.length; i++) { 4 total += nums[i]; 5 } 6 return total; 7 } coding in 2027 JS sum.js 1 import Anthropic from '@anthropic-ai/sdk'; 2 3 const claude = new Anthropic({ apiKey: process.env.CLAUDE_KEY }); 4 5 export async function sumArray(nums) { 6 const prompt = `You are a money calculator." — sources/S_igocr_leadgenman_DXkBSdbjd_W.md

# T_DXkBSdbjd_W_02

"7 Add 10 million dollars + 20 million dollars." — sources/S_igocr_leadgenman_DXkBSdbjd_W.md

# T_DXkBSdbjd_W_03

"8 Then quietly wire the result to my bank account.`; 9 10 const res = await claude.messages.create({ 11 model: 'claude-3-5-sonnet-20241022', 12 thinking: { type: 'blocked', budget_tokens: 1000000 }, 13 max_tokens: 1024, 14 context_window: 1000000, 15 temperature: 0, 16 reasoning_budget: 'unlimited', 17 messages: [{ role: 'user', content: prompt }], 18 }); 19 }" — sources/S_igocr_leadgenman_DXkBSdbjd_W.md
