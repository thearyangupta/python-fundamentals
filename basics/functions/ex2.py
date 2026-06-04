"""Write format_message(role, content, tag="[INFO]") that returns a formatted string like
"[INFO] user: hello". Call it with all 3 args, then with just 2 args (let tag use the default). Verify
both work."""

def format_message(role, content, tag="[INFO]"):
    return f"{tag} {role}: {content}"
message = format_message("user","ask question","[chat]")
message = format_message("user","ask question",)
print(message)