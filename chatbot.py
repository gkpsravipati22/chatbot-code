print("Welcome to SimpleChat!")
test_messages = ["Hello", "How are you?", "bye"]
for user_input in test_messages:
    print("You:", user_input)
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: You said:", user_input)
