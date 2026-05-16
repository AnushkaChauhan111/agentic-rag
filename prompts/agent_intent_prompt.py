INTENT_PROMPT = """
Classify intent:
summary, keypoints, qa_gen, rag_qa, unknown

Rules:
- comma-separated output only
- no explanation
- unclear → unknown

Query: {query}
Output:
"""