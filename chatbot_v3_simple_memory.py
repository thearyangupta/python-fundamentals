import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")
# Start a chat session - this object holds memory automatically
chat = model.start_chat(history=[])
print("Chatbot v3 - I remember what we talked about. Type 'quit' to exit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "quit":
        print("Bye!")
        break
    if not user_input.strip():
        continue
    try:
        response = chat.send_message(user_input)
        print(f"\nAI: {response.text}")
    except Exception as e:
        print(f"Something went wrong: {e}")
print(f"\nTotal exchanges: {len(chat.history) // 2}")