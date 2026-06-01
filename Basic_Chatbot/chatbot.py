# Function for chatbot replies
def chatbot():

    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit.\n")

    # Loop runs continuously
    while True:

        # User input
        user_input = input("You: ").lower()

        # Predefined replies
        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a simple chatbot.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

# Call the function
chatbot()
