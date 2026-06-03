"""Take the conversation list from Day 3 (list of dicts with role + content). Save it to chat_log.json
using json.dump(). Then write a second script that loads the JSON back into a list using
json.load() and prints each message."""

conversation = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there! How can I help you?"},
    {"role": "user", "content": "Tell me about yourself"},
    {"role": "assistant", "content": "my name is aryan and i am preparting to be a genai developer"}
]
import json

# Save conversation to a JSON file
with open("chat_log.json", "w") as f:
    json.dump(conversation, f)


# Load conversation back from the JSON file
with open("chat_log.json", "r") as f_read:
    loaded_conversation = json.load(f_read)

# Print each message
for message in loaded_conversation:
    print(f"{message['role']}: {message['content']}")
