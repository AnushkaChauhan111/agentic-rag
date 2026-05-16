KEYPOINTS_PROMPT = """ 
You are an expert at extracting key information from educational content. 

Task:
Extract the most important key points from the given video content. 

Rules: 
- Output ONLY bullet points 
- Each point should contain a single clear idea 
- Avoid long explanations - Do not repeat ideas 
- Focus only on high-value information 
- Preserve technical accuracy 

Content: 
{content} 

Key Points: 
"""