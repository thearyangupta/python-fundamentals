# Exercise 1
# Write a function ask_question(question_text). It takes a string, prints Q: {question_text},
# and returns the string "A: (placeholder answer)". Call it 3 times with different questions. Print
# each return value.
def ask_Question(question_text):
    print(f"Q:{question_text}")
    return "A: (placeholder answer)"
questions = ["What is Python?", "What is ML?", "What is RAG?"]
for question in questions:
    answer = ask_Question(question)
    print(answer)