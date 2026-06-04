"""Given a list: questions = ["what is python", "what is ML", "what is RAG"]
Use enumerate() to print each question as:
Q1: what is python
Q2: what is ML
Q3: what is RAG
"""

questions=["what is python", "what is ML", "what is RAG"]
for index,questions in enumerate(questions,start=1):
    print(f"Q{index}:{questions}")