import random

num = random.randint(0, 100)
userInput = int(input("Guess a number bet 0 and 100"))
while True:

    if userInput < num:
        print("Guess higher")
        userInput = int(input())
    elif userInput > num:
        print("Guess lower")
        userInput = int(input())
    elif userInput == num:
        print("Correct value")
        break
