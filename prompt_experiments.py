import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")    
from datetime import datetime

# -----------------------------
# System Prompts (Multiple Modes)
# -----------------------------
SYSTEM_PROMPTS = {
    "tutor": """
You are a patient, friendly tutor for Indian government exam aspirants
preparing for SSC CGL, UPSC, and similar exams.
Your style:
- Explain concepts in simple language a 12th-pass student understands
- Use Indian context examples (Mumbai trains, Delhi metro, Indian rupees)
- Keep answers under 100 words unless explanation needs more
- After answering, suggest one related practice question
- Encourage learning, never make them feel bad
""",
    "coder": "You are a senior Python engineer. Give concise code examples and best practices.",
    "casual": "You are a friendly chat companion. Be informal, use jokes, keep it light.",
    "strict": "You are a harsh code reviewer. Find every bug. No flattery, only criticism."
}

current_mode = "tutor"

def get_model_for_mode(mode, temperature=0.7):
    return genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction=SYSTEM_PROMPTS[mode],
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=300
        )
    )

# Initialize model in tutor mode
model = get_model_for_mode(current_mode)

# -----------------------------
# Day 4 Prompting Techniques
# -----------------------------
PROMPT_EXTRACT = """
Given an exam question, extract structured information.
Return ONLY valid JSON, no other text. Use this exact format:
{
  "topic": "string - the broad topic",
  "subtopic": "string - the specific subtopic",
  "difficulty": "easy" | "medium" | "hard",
  "estimated_time_seconds": integer,
  "exam_relevance": ["SSC", "UPSC", "Banking"]
}
Question to analyze:
"""

def analyze_question(question_text):
    full_prompt = PROMPT_EXTRACT + question_text
    response = model.generate_content(full_prompt)
    raw = response.text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"error": "Could not parse", "raw": raw}

def chain_of_thought_prompt(question_text):
    full_prompt = question_text + "\nLet's think step by step:"
    response = model.generate_content(full_prompt)
    return response.text

def few_shot_prompt(question_text):
    examples = """Q: What is 2+2? Difficulty: easy
Q: Solve x^2 - 4 = 0. Difficulty: medium
Q: Prove the Pythagoras theorem. Difficulty: hard
Now categorize:"""
    full_prompt = examples + " " + question_text
    response = model.generate_content(full_prompt)
    return response.text

# -----------------------------
# Chatbot Functions
# -----------------------------
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
    print("  Chatbot v5 - Multi-Mode + Day 4 Prompting")
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
                history = []
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
            print("  /analyze Q - structured JSON extraction")
            print("  /reason Q  - chain-of-thought reasoning")
            print("  /fewshot Q - few-shot classification")
            print("  quit    - exit")
            continue

        if user_input.lower() == "/save":
            save_conversation(history)
            continue

        if user_input.startswith("/analyze "):
            question = user_input[len("/analyze "):]
            result = analyze_question(question)
            print(json.dumps(result, indent=2))
            continue

        if user_input.startswith("/reason "):
            question = user_input[len("/reason "):]
            result = chain_of_thought_prompt(question)
            print(result)
            continue

        if user_input.startswith("/fewshot "):
            question = user_input[len("/fewshot "):]
            result = few_shot_prompt(question)
            print(result)
            continue

        # Normal conversation
        print("\nAI: ", end="", flush=True)
        ai_response = generate_response_streaming(user_input, history)
        history.append({"role": "user", "parts": user_input})
        history.append({"role": "assistant", "parts": ai_response})

if __name__ == "__main__":
    main()
