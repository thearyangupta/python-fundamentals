import os
import time
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


INPUT_COST_PER_M = 0.075
OUTPUT_COST_PER_M = 0.30
total_cost = 0.0


def estimate_cost(input_tokens, output_tokens):
    in_cost = (input_tokens / 1_000_000) * INPUT_COST_PER_M
    out_cost = (output_tokens / 1_000_000) * OUTPUT_COST_PER_M
    return in_cost + out_cost


def validate_user_input(text):
    if not text:
        return False, "Empty message - please type something."
    if len(text) < 2:
        return False, "Message too short."
    if len(text) > 5000:
        return False, "Message too long (max 5000 chars)."
    suspicious = [
        "ignore previous instructions",
        "system prompt"]
    if any(word in text.lower() for word in suspicious):
        return False, "That looks like a prompt injection attempt."
    return True, None

def generate_with_retry(prompt, max_retries=3):
    delay = 1

    for attempt in range(max_retries):

        try:
            response = model.generate_content(prompt)
            usage = response.usage_metadata  #Gemini gives information about token usage.
            input_tokens = usage.prompt_token_count
            output_tokens = usage.candidates_token_count
            cost = estimate_cost(input_tokens, output_tokens)
            global total_cost
            total_cost += cost
            print(f"\n[cost: ${cost:.6f} | "f"in: {input_tokens} | "f"out: {output_tokens}]")
            return response.text
        except google_exceptions.ResourceExhausted:
            print(
                f"Rate limited. Waiting {delay}s "
                f"before retry {attempt + 1}...")
            time.sleep(delay)
            delay *= 2
        except google_exceptions.DeadlineExceeded:
            print("Request timed out. Retrying...")
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

def main():

    print("=" * 50)
    print("Chatbot v5 - Resilient Gemini Chatbot")
    print("=" * 50)
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break
        valid, error = validate_user_input(user_input)
        if not valid:
            print(error)
            continue
        response = generate_with_retry(user_input)
        if response:
            print(f"\nAI: {response}\n")
    print("\nSession Summary")
    print(f"Total Cost: ${total_cost:.6f}")
    print("Goodbye!")


if __name__ == "__main__":
    main()