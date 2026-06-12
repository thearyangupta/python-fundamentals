import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
SYSTEM_PROMPTS = {
    "tutor": """
You are a patient tutor.
Explain concepts simply.
Give examples.
Encourage learning.
""",

    "coder": """
You are a senior Python engineer.
Give concise explanations.
Focus on code and best practices.
""",

    "casual": """
You are a friendly chat companion.
Be relaxed and conversational.
""",

    "strict": """
You are a strict reviewer.
Point out mistakes directly.
Focus on improvement.
"""
}

current_mode = "tutor"
INPUT_COST_PER_M = 0.075
OUTPUT_COST_PER_M = 0.30
total_cost = 0.0

def get_model(mode):
    return genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction=SYSTEM_PROMPTS[mode]
    )
model = get_model(current_mode)

def estimate_cost(input_tokens, output_tokens):
    in_cost = (input_tokens / 1_000_000) * INPUT_COST_PER_M
    out_cost = (output_tokens / 1_000_000) * OUTPUT_COST_PER_M
    return in_cost + out_cost

def validate_user_input(text):
    if not text:
        return False, "Empty message."
    if len(text) < 2:
        return False, "Message too short."
    if len(text) > 5000:
        return False, "Message too long."
    suspicious = [
        "ignore previous instructions",
        "system prompt"
    ]

    if any(
        phrase in text.lower()
        for phrase in suspicious):
        return False, "Prompt injection attempt detected."
    return True, None

def save_conversation(history):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = (f"chat_log_{timestamp}.json")
    with open(filename, "w") as f:
        json.dump(history,f,indent=2)

    print(f"Saved to {filename}")

def generate_with_retry_streaming(
    user_msg,
    history,
    max_retries=3
):
    global total_cost
    delay = 1
    messages = history + [
        {
            "role": "user",
            "parts": user_msg
        }
    ]

    for attempt in range(max_retries):
        try:
            response_stream = model.generate_content(messages,stream=True)
            full_response = ""
            print("\nAI: ", end="", flush=True)
            for chunk in response_stream:
                if chunk.text:
                    print(chunk.text,end="",flush=True)
                    full_response += chunk.text
            print()
            try:
                usage = response_stream.usage_metadata
                input_tokens = (usage.prompt_token_count)
                output_tokens = (usage.candidates_token_count)
                cost = estimate_cost(input_tokens,output_tokens)
                total_cost += cost
                print(f"\n[cost: ${cost:.6f} "f"| in: {input_tokens} "f"| out: {output_tokens}]")
            except:
                pass
            return full_response        
        except google_exceptions.ResourceExhausted:
            print(f"Rate limited. "f"Waiting {delay}s...")
            time.sleep(delay)
            delay *= 2
        except google_exceptions.DeadlineExceeded:
            print(f"Timeout. Retrying...")
            time.sleep(delay)
            delay *= 2
        except google_exceptions.InvalidArgument as e:
            print(f"Bad input: {e}")
            return None
        except google_exceptions.PermissionDenied as e:
            print(f"Permission denied: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    print(f"All {max_retries} retries failed.")
    return None

def print_banner():
    print("=" * 60)
    print(" Chatbot v3 - Gemini")
    print("=" * 60)
    print("Commands:")
    print("/help /reset /save/mode /cost quit\n")

def main():
    global model
    global current_mode
    history = []
    print_banner()
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            save_conversation(history)
            print(f"\nTotal Cost: "f"${total_cost:.6f}")
            print("Goodbye!")
            break
        if user_input in ("/help", "/?"):
            print("\n/reset"
                "\n/save"
                "\n/cost"
                "\n/mode tutor"
                "\n/mode coder"
                "\n/mode casual"
                "\n/mode strict"
                "\nquit")
            continue
        if user_input == "/reset":
            history = []
            print("Memory cleared.")
            continue
        if user_input == "/save":
            save_conversation(history)
            continue
        if user_input == "/cost":
            print(f"Total cost: "f"${total_cost:.6f}")
            continue
        if user_input.startswith("/mode "):
            parts = user_input.split()
            if len(parts) != 2:
                print("Usage: /mode tutor")
                continue
            new_mode = parts[1]
            if new_mode not in SYSTEM_PROMPTS:
                print(f"Available modes: "
                      f"{list(SYSTEM_PROMPTS.keys())}"
                )
                continue
            current_mode = new_mode
            model = get_model(current_mode)
            history = []
            print(f"Switched to "f"{current_mode}")
            continue
        valid, error = (validate_user_input(user_input))
        if not valid:
            print(error)
            continue
        ai_response = (generate_with_retry_streaming(user_input,history))
        if ai_response:
            history.append(
                {"role": "user","parts": user_input})
            history.append(
                {"role": "model","parts": ai_response})
            
if __name__ == "__main__":
    main()