import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

def print_banner():
    print("=" * 50)
    print(" Chatbot v3 - powered by Gemini 2.5 Flash")
    print("=" * 50)
    print("Type your message, /help for commands, quit to exit.\n")


def generate_response_streaming(user_msg, history):
    messages = history + [{"role": "user", "parts": user_msg}]
    response_stream = model.generate_content(messages, stream=True)
    full_response = ""

    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text

    print()

    return full_response


def count_tokens_rough(history):
    """
    Rough estimate:
    1 token ≈ 4 characters
    """

    total = " ".join(
        msg.get("parts", "")
        for msg in history
    )

    return len(total) // 4


def save_conversation(history, filename=None):

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_log_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(history, f, indent=2)

    print(f"\nSaved to {filename}")

    return filename


def main():

    history = []
    print_banner()
    while True:
        try:
            user_input = input("You: ").strip()#removes spaces from the beginning and end of a string
            # Empty input
            if not user_input:#"Is user_input empty?"
                continue
            # Quit
            if user_input.lower() == "quit":
                save_conversation(history)
                print("\nBye!")
                break
            # Help
            if user_input.lower() in ("/help", "/?"):

                print("\nCommands:")
                print(" /help  - show commands")
                print(" /reset - clear conversation memory")
                print(" /save  - save conversation")
                print(" quit   - exit\n")
                continue
            # Reset memory
            if user_input.lower() == "/reset":

                history = []

                print("\nConversation cleared. Fresh start.\n")

                continue

            # Save manually
            if user_input.lower() == "/save":

                save_conversation(history)

                continue

            # Stream response
            print("\nAI: ", end="", flush=True)

            ai_response = generate_response_streaming(user_input,history)
            # Store memory
            history.append(
                {
                    "role": "user","parts": user_input}
            )

            history.append(
                {
                    "role": "model","parts": ai_response}
            )

            print(
                f"\n[debug] approx tokens: "
                f"{count_tokens_rough(history)}\n"
            )

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()