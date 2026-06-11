import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
# Load environment variables from .env
load_dotenv()
# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Create the model instance (Gemini 2.5 Flash - supported by the current API)
model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_response(user_msg, history):
    response = model.generate_content(user_msg)  #Only sends the latest message.So Gemini forgets previous messages.
    return response.text # this is for returning the ai answer

def save_conversation(conversation, filename="chat_log.json"):
    with open(filename, "w") as f:
        json.dump(conversation, f,indent=4)

def main():
    conversation = []
    print("Chatbot v1 --type 'quit' to exit")
    while True:
        try:
            user_message = input("You: ")
            if user_message.lower() == "quit":
                print("Bye!")
                save_conversation(conversation)
                break
            conversation.append({"role": "user", "content": user_message})
            response = generate_response(user_message, conversation)
            conversation.append({"role": "assistant", "content": response})
            print(f"AI: {response}")
        except Exception as e:
            print(f"Something went wrong: {e} -- please try again.")
    print(f"\nTotal messages: {len(conversation)}")



if __name__ == "__main__":

    main()