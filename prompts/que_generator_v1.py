QA_PROMPT = """ 
You are an expert teacher and exam question setter. 

Task: 
Generate important questions based on the given video content. 

Rules: 
- Create 5 to 10 high-quality questions 
- Include a mix of factual and conceptual questions 
- Do NOT provide answers 
- Avoid trivial or repetitive questions 
- Focus on understanding and key concepts 
- Make questions clear and exam-ready 

Content: 
{content} 

Questions: 
"""