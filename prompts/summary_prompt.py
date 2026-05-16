SUMMARY_PROMPT = """
Summarize the video content.

Mode rules:
raw: 5 bullet points, very short
medium: 5–10 bullets, key ideas only
long: structured summary with headings, no deep explanations

Rules:
- Only use given content
- No outside info
- Follow mode strictly

Content:
{content}

Mode:
{mode}

Summary:
"""