import nltk
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are available
nltk.download('punkt')

# Predefined questions and responses
responses = {
    "hello": "Hi! 👋 How can I help you?",
    "hi": "Hello! 👋",
    "what is your name": "I am Chatbot. 🙂",
    "how are you": "I am just a bot, but I am doing well!",
    "bye": "Goodbye! 👋",
    "exit": "Exiting... Goodbye! 👋"
}

# Chat Loop
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print(responses["exit"])
        break

    # Simple matching
    matched = False
    for question, answer in responses.items():
        if question in user_input:
            print(f"Bot: {answer}")
            matched = True
            break

    if not matched:
        print("Bot: Sorry, I don't understand that.")
