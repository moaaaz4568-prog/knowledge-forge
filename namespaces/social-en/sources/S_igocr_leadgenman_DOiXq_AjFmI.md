---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_0.txt"
words: 265
sha1: 936869138fc8b9aa9c5fc83489221b28ba0822ea
lang: en
account: leadgenman
quality: ocr+carousel-7
---

# S_igocr_leadgenman_DOiXq_AjFmI

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_0.txt`
> الأجزاء: 7 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DOiXq_AjFmI_7.txt`

<!-- image 0 -->
Key Nodes in n8n
Essential Nodes for
Process Automation
<!-- image 1 -->
Code
Allows you to run custom JavaScript or Python code to manipulate data, perform calculations, or integrate complex logic.
Use cases:
• Transform data: Convert JSON format to XML before sending it to another API.
• Validate data: Check if a field meets specific conditions (e.g., valid email) before continuing the workflow.
Code Node
<!-- image 3 -->
Edit
Fields
Modifies, renames, or deletes fields from the
incoming data, or adds new static/dynamic fields.
Use cases:
• Normalize data: Rename first_name to
nombre to standardise formats.
• Add metadata: Insert a timestamp field with
the current time for each record.
Edit Fields
manual
→
<!-- image 4 -->
IF
Splits the workflow into different branches based on conditions.
Use cases:
• Filter records: Separate "active" clients from "inactive" ones to send them different emails.
• Error validation: If an API returns an error, send an alert; if not, continue the process.
If
true
false
<!-- image 5 -->
Switch
Similar to if, but evaluates multiple conditions and
directs the workflow into different branches
based on matches.
Use cases:
• Classify products: Route items differently
depending on their category.
• Handle HTTP status codes: Process 200, 404, or
500 API responses differently.
Switch
mode: Rules
Switch
<!-- image 6 -->
Loop Over Items
Iterates over an array or list of elements, executing operations on each of them.
Use cases:
• Process multiple files: Upload each file from a list to Google Drive one by one.
• Send personalized emails: Loop through a list of recipients and generate a unique message for each.
Loop Over Items
done
loop
<!-- image 7 -->
Follow for more:
LEAD GEN MAN