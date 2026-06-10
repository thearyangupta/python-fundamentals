import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")    
from datetime import datetime

def get_model_for_mode(mode):
    return genai.GenerativeModel(
        "gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPTS[mode]
    )


# -----------------------------
# Chatbot Functions
# -----------------------------
def generate_response_streaming(user_msg, history):
    """Yields response chunks as they arrive."""
    messages = history + [{"role": "user", "parts": user_msg}]
    response_stream = model.generate_content(messages, stream=True)
    full_response = ""
    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text
    print()
    return full_response

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
    print("  Chatbot v4 - Multi-Mode + Gemini 2.5 Flash")
    print("=" * 50)
    print("Type your message, /help for commands, quit to exit.\n")

# -----------------------------
# Main Loop
# -----------------------------
def main():
    print_banner()
    history = []

    while True:
        user_input = input("You: ")

        # Exit
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Mode switching
        if user_input.startswith("/mode "):
            new_mode = user_input.split()[1]
            if new_mode in SYSTEM_PROMPTS:
                current_mode = new_mode
                model = get_model_for_mode(new_mode)
                history = []  # reset memory
                print(f"Switched to {new_mode} mode.\n")
            else:
                print(f"Unknown mode. Options: {list(SYSTEM_PROMPTS.keys())}\n")
            continue

        # Commands
        if user_input.lower() == "/reset":
            history = []
            print("Conversation cleared. Fresh start.\n")
            continue

        if user_input.lower() in ("/help", "/?"):
            print("\nCommands:")
            print("  /reset  - clear conversation memory")
            print("  /save   - save conversation with timestamp")
            print("  /mode X - switch personality (tutor, coder, casual, strict)")
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
