import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_response(user_msg, history):
    """history is a list of dicts: [{"role": "user", "parts": "..."}]"""
    messages = history + [{"role": "user", "parts": user_msg}]
    response = model.generate_content(messages)
    return response.text    


#for finding out how many tokens used

def count_tokens_rough(history):
    """Quick heuristic: 1 token ~= 4 characters in English."""
    total = " ".join([msg["parts"] for msg in history])
    return len(total) // 4



def main():
    history = []
    print("Chatbot v3 (manual memory) - type 'quit' to exit.\n")
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == "quit":
                with open("chat_log.json", "w") as f:
                    json.dump(history, f, indent=2)
                print("\nBye! Saved to chat_log.json")
                break
            if not user_input.strip():
                continue
            ai_response = generate_response(user_input, history)
            print(f"\nAI: {ai_response}\n")
            # Add BOTH user message AND AI response to history
            history.append({"role": "user", "parts": user_input})
            history.append({"role": "model", "parts": ai_response})
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(f"[debug] approx tokens: {count_tokens_rough(history)}")
if __name__ == "__main__":
    main()