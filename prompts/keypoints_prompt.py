KEYPOINTS_PROMPT = """
Extract key points.

Mode:
raw: 5 bullets, short takeaways
medium: 6–10 bullets, brief explanations
long: sections with headings, 2–4 bullets each

Rules:
- no repetition
- no outside info
- concise and accurate

Content:
{content}
Mode:
{mode}

Key Points:
"""