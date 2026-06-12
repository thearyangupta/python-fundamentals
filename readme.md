"My Python learning journey, May 2026.CS student in India, building
towards a GenAI dev role. Follow along"

"There are two branches in it
1st- Main,
2nd - Basic

Main contains the information about the repository,
Basic contains the code and the progress i am making towards a  GenAI dev role"


## Week 1 — Python Fundamentals for GenAI
In Week 1, I focused on building the foundation of my chatbot project and practicing core Python skills:
- **Chatbot Skeleton (chatbot_v1.py)**  
  - Loops forever asking for user input.  
  - Handles the `quit` command by saving the conversation to `chat_log.json` and printing the total message count.  
  - Uses `generate_response()` (currently a placeholder) to reply to user messages.  
  - Stores both user and assistant messages in a structured list of dictionaries.  
  - Wraps the loop in `try/except` to catch errors and continue running instead of crashing.
- **JSON Handling**  
  - Learned to save conversation logs with `json.dump()` and reload them with `json.load()`.  
  - Practiced persisting structured data like chat history.
- **Error Handling**  
  - Intentionally triggered errors (`NameError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`).  
  - Wrapped each in specific `try/except` blocks to provide friendly messages instead of crashing.  
  - Built `safe_read_file(path)` to safely read files and return clear error feedback.
- **Utility Functions**  
  - `get_integer_input(prompt)` — keeps asking until the user enters a valid integer.  
  - `safe_read_file(path)` — returns file content or a helpful error message.
### 📘 Reflection
Week 1 gave me hands‑on practice with loops, functions, file I/O, JSON, and exception handling. These are the building blocks for the chatbot. In Week 2, I’ll replace the placeholder response with a real Gemini API call to make the chatbot interactive with GenAI.
## Week 2 - First LLM Calls + Memory + System Prompts
What I Built
Developed a production-style conversational AI chatbot using Google's Gemini 1.5 Flash API.
### 📘 Features
Real Gemini API integration
Conversation memory using manual history management
Multiple AI personalities through system prompts:
Tutor
Coder
Casual
Strict
Streaming responses for improved user experience
Input validation and prompt-injection protection
Automatic retry handling with exponential backoff
Token usage and API cost tracking
Conversation saving with timestamps
### 📘Built-in commands:
/help
/reset
/save
/cost
/mode
### 📘Technologies Used:
Python
Gemini 1.5 Flash
python-dotenv
JSON
Error Handling & Retry Logic
### 📘Reflection:
Week 2 was the point where my chatbot became a real AI application. I learned that building with LLMs involves much more than making API calls. Features such as conversation memory, system prompts, error handling, retries, and cost tracking are essential for creating reliable AI systems. The most valuable lesson was understanding the difference between simply using an AI model and engineering an application around it. By the end of the week, I had built a Gemini-powered chatbot capable of maintaining conversations, adapting its personality, handling failures gracefully, and tracking usage costs.