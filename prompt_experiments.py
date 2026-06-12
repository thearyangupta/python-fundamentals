import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def test_few_shot():
    prompt = """
Here are examples:

Q: What is 2+2?
Difficulty: easy

Q: Solve x^2 - 4 = 0
Difficulty: medium

Q: Prove the Pythagoras theorem
Difficulty: hard

Now categorize:

Q: What is the capital of France?
Difficulty:
"""

    response = model.generate_content(prompt)

    print("\n=== FEW SHOT OUTPUT ===")
    print(response.text)

def test_chain_of_thought():
    prompt = """
If train A leaves Mumbai at 3pm at 60 kmph and train B leaves Delhi at
5pm at 80 kmph going opposite directions, when do they meet?

Let's think step by step:
1. Identify the distance
2. Calculate travel distances
3. Form an equation
4. Solve
"""

    response = model.generate_content(prompt)

    print("\n=== CHAIN OF THOUGHT OUTPUT ===")
    print(response.text)

PROMPT_EXTRACT = """
Given an exam question, extract structured information.

Return ONLY valid JSON.

{
    "topic": "string",
    "subtopic": "string",
    "difficulty": "easy | medium | hard",
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
        return {
            "error": "Could not parse JSON",
            "raw_response": raw
        }
    
def test_temperature():
    prompt = "Write a short story about an AI helping a student."

    print("\n=== TEMPERATURE 0.0 ===")

    response = model.generate_content(prompt,
            generation_config=genai.types.GenerationConfig(
            temperature=0.0,
            max_output_tokens=200
        )
    )
    print(response.text)
    print("\n=== TEMPERATURE 0.7 ===")
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.7,
            max_output_tokens=200
        )
    )
    print(response.text)

def main():
    print("=" * 50)
    print("DAY 5 - PROMPT ENGINEERING EXPERIMENTS")
    print("=" * 50)
    test_few_shot()
    test_chain_of_thought()
    result = analyze_question(
        "Who was the first President of India?"
    )
    print("\n=== JSON EXTRACTION OUTPUT ===")
    print(json.dumps(result, indent=2))
    test_temperature()


if __name__ == "__main__":
    main()