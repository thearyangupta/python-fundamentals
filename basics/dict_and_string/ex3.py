"""
Create a list called conversation. Append 4 dicts to it, each with the keys "role" (either "user" or
"assistant") and "content" (the message). Then loop through the list and print each message in format:
"[role]: content".
"""
conversation = [
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What is the largest planet in our solar system?"},
    {"role": "assistant", "content": "The largest planet in our solar system is Jupiter."}
]
for message in conversation:
    print(f"{message['role']}: {message['content']}")