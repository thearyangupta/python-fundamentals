import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT_TUTOR = """
You are a patient and friendly Python tutor.

Rules:
- Explain concepts in simple language.
- Use examples whenever possible.
- Encourage learning.
- Keep answers concise.
- After every answer, give one small practice question.
"""

model = genai.GenerativeModel(
    "models/gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT_TUTOR
)


def print_banner():

    print("=" * 50)
    print(" Chatbot v4 - Tutor Mode")
    print("=" * 50)
    print("Type your message.")
    print("Commands:")
    print("/help")
    print("/reset")
    print("/save")
    print("quit")
    print()

def save_conversation(history):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"chat_log_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(history, f, indent=4)

    print(f"\nSaved to {filename}")

    return filename

def generate_response_streaming(user_msg,history):

    messages = history + [
        {
            "role": "user",
            "parts": user_msg
        }
    ]
    response_stream = model.generate_content(messages,stream=True)

    full_response = ""

    for chunk in response_stream:

        if chunk.text:

            print(
                chunk.text,
                end="",
                flush=True
            )
            full_response += chunk.text
    print()
    return full_response

def main():

    history = []
    print_banner()
    while True:
        try:
            user_input = input("You:").strip()
            if user_input.lower() == "quit":
                save_conversation(history)
                print("\nBye!")
                break
            if not user_input:
                continue
            if user_input.lower() in ("/help","/?"):
                print("\nCommands:")
                print("/help  - show commands")
                print("/reset - clear memory")
                print("/save  - save chat")
                print("quit   - exit\n")

                continue

            if user_input.lower() == "/reset":
                history = []
                print("\nConversation memory cleared.\n")
                continue

            if user_input.lower() == "/save":
                save_conversation(history)
                continue
            print("\nTutor AI: ",end="",flush=True)
            ai_response = (generate_response_streaming(user_input,history))
            # Store Memory
            history.append(
                {
                    "role": "user",
                    "parts": user_input
                }
            )

            history.append(
                {
                    "role": "model",
                    "parts": ai_response
                }
            )
            print()
        except Exception as e:
            print(f"\nSomething went wrong: {e}\n")

if __name__ == "__main__":
    main()