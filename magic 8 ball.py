from random import randint
running = True
question = ""
response = ["it is certain.", "it is decidedly so.", "without a doubt.", "yes, definitely.", "you may rely on it.", "as I see it, yes.", "most likely.", "outlook good.", "yes.", "signs point to yes", "reply hazy, try again.", "ask again later.", "better not tell you now.", "cannot predict now.", "concentrate and ask again.", "don't count on it.", "my reply is no.", "my sources say no.", "outlook not so good.", "very doubtful."]

print("Welcome to the Magic 8-Ball Parlor! Ask any question you'd like. Type 'quit' to leave.")

while running == True:
    question = input("Your question: ")
    if "?" in question:
        print("My response: " + str(response[randint(0,19)]))
    elif "quit" in question:
        print("Goodbye!")
        running = False
    else:
        print("Make sure your question ends with a question mark. Please ask again.")
        continue
