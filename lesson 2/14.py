# Program 14: while loops

running = True
guessNumber = 0
guess = ""

print("What is my favorite fruit?")
guess = input()
while guess != "banana":
    guessNumber = guessNumber + 1
    if guessNumber > 19:
        print("Twenty tries and you still didn't guess it? It's banana.")
        break
    guess = input("Guess again.\n")

if guessNumber < 19:
    print("Goob job, it was banana.")
if guessNumber == 19:
    print("Good job, it was banana. You got it on your last guess too.")
