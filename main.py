trainingData = {
    "hello" : "Hello! How can I help?",
    "meow" : "Are you a cat?"
    # ... Add more pairs here to make it smarter
}

print("Hi! I'm WaffleBot. Ask me a question or type quit to exit! 😺")

while True:
    question = input().lower()
    if question in trainingData:
        response = trainingData[question]
        print(response)
    elif question == "quit":
        print("Bye! 🐈")
        break
    else:
        print("Sorry! I don't understand that yet 😿. Try asking me a different question")
