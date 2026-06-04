"""Write safe_read_file(path) that tries to read a file. 
If file doesn't exist → returns "File not found".
If any other error → returns "Error reading file: {error message}".
If success → returns the file content."""


def safe_read_file(path):
    try:
        with open("file.txt","r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found") 
    except Exception as e:
        return f"Error reading file: {e}"