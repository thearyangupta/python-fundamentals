"My Python learning journey, May 2026. Final-year CS student in India, building
toward a GenAI dev role. Follow along."

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
