import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")
from datetime import datetime


def generate_response_streaming(user_msg, history):
# AI response will come in small pieces/chunks instead of waiting for the entire answer
    messages = history + [{"role": "user", "parts": user_msg}]
    response_stream = model.generate_content(messages, stream=True)
    full_response = ""
    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)  # flush=True ensures immediate output
            full_response += chunk.text
    print()  # newline at end
    return full_response
"""
Why flush=True? Python normally buffers print output until newline. With streaming, we want each chunk
to appear immediately. flush=True forces that."""   

def save_conversation(history, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_log_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(history, f, indent=2)
    print(f"Saved to {filename}")
    return filename

def print_banner():
    print("=" * 50)
    print("  Chatbot v3 - powered by Gemini 1.5 Flash")
    print("=" * 50)
    print("Type your message, /help for commands, quit to exit.\n")

def main():
    print_banner()
    history = []

    while True:
        user_input = input("You: ")

        # Exit
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Commands
        if user_input.lower() == "/reset":
            history = []
            print("Conversation cleared. Fresh start.\n")
            continue

        if user_input.lower() in ("/help", "/?"):
            print("\nCommands:")
            print("  /reset  - clear conversation memory")
            print("  /save   - save conversation with timestamp")
            print("  quit    - exit")
            continue

        if user_input.lower() == "/save":
            save_conversation(history)
            continue

        # Normal conversation
        print("\nAI: ", end="", flush=True)
        ai_response = generate_response_streaming(user_input, history)
        history.append({"role": "user", "parts": user_input})
        history.append({"role": "assistant", "parts": ai_response})
if __name__ == "__main__":
    main()
