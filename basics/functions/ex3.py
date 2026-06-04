# Exercise 3 — functions calling functions 
# Build these 3 functions that call each other:
# 1. validate_input(text) — returns True if text is not empty and longer than 2 chars, else returns
# False.
# 2. process_question(text) — calls validate_input(). If invalid, returns "Error: question too short".
# Else returns "Processing: {text}".
# 3. main() — calls process_question() with 3 different inputs (one invalid, two valid) and prints each
# result

def validate_input(text):
    return len(text) > 2

def process_question(text):
    if not validate_input:
        print("error")
    else:
        print("processing")

def main():
    inputs = ["hi","helloo","yesss"]
    for input in inputs:
        result = process_question(text)
        print(result)