def show_messages(messages):
    """Print each text message in the list."""
    for message in messages:
        print(message)
 
 
def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
 
 
messages = [
    "Hi! Are we still meeting today?",
    "Running ten minutes late.",
    "Don't forget to bring the notes.",
]
sent_messages = []
 
send_messages(messages, sent_messages)
 
print("\nMessages:")
print(messages)
print("\nSent messages:")
print(sent_messages)
 