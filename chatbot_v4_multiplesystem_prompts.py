import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPTS = {
    "tutor": """
You are a patient and friendly Python tutor.

Rules:
- Explain concepts in simple language.
- Use examples whenever possible.
- Encourage learning.
- Keep answers concise.
- After every answer, give one small practice question.
""",

    "coder": """
You are a senior Python software engineer.

Rules:
- Give concise answers.
- Focus on code.
- Show best practices.
- Explain only when necessary.
- Use clean and readable examples.
""",

    "casual": """
You are a friendly chat companion.

Rules:
- Be informal.
- Use humor occasionally.
- Keep the conversation fun.
- Talk like a friend.
""",

    "strict": """
You are a strict code reviewer.

Rules:
- Point out mistakes directly.
- No unnecessary praise.
- Focus on improving code quality.
- Suggest better alternatives.
"""
}
current_mode = "tutor"

def get_model_for_mode(mode):
    return genai.GenerativeModel(
        model_name="models/gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPTS[mode]
    )
model = get_model_for_mode(current_mode)

def print_banner():
    print("=" * 50)
    print(" Chatbot v4 - Multiple Personalities ")
    print("=" * 50)
    print(f"Current Mode: {current_mode}")
    print("Type /help for commands\n")


def save_conversation(history):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_log_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(history, f, indent=4)

    print(f"\nConversation saved to {filename}")


def generate_response(user_msg, history):
    messages = history + [
        {
            "role": "user",
            "parts": [user_msg]
        }
    ]
    response = model.generate_content(messages)
    return response.text

def main():
    global current_mode
    global model

    history = []

    print_banner()

    while True:

        try:
            user_input = input("You: ").strip()
            if user_input.lower() == "quit":
                save_conversation(history)
                print("Goodbye!")
                break
            if not user_input:
                continue
            if user_input in ["/help", "/?"]:
                print("\nCommands:")
                print("/help          Show commands")
                print("/reset         Clear memory")
                print("/save          Save conversation")
                print("/mode tutor    Tutor mode")
                print("/mode coder    Coder mode")
                print("/mode casual   Casual mode")
                print("/mode strict   Strict mode")
                print("quit           Exit chatbot\n")
                continue

            if user_input == "/reset":
                history = []
                print("\nConversation memory cleared.\n")
                continue
            if user_input == "/save":
                save_conversation(history)
                continue

            if user_input.startswith("/mode"):
                parts = user_input.split()  
                if len(parts) != 2:
                    print("Usage: /mode tutor")
                    continue
                new_mode = parts[1].lower()
                if new_mode not in SYSTEM_PROMPTS:
                    print(f"Available modes: {list(SYSTEM_PROMPTS.keys())}")
                    continue
                current_mode = new_mode
                model = get_model_for_mode(new_mode)
                history = []
                print(f"\nSwitched to {new_mode} mode.")
                print("Conversation memory reset.\n")

                continue
            ai_response = generate_response(user_input,history)
            print(f"\nAI: {ai_response}\n")
            history.append({
                "role": "user",
                "parts": [user_input]
            })
            history.append({
                "role": "model",
                "parts": [ai_response]
            })
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()