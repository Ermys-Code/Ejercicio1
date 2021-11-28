import random

print("Welcome to the Guess My Word App")

gameDict = {"sports": ["basketball", "futball", "tennis", "snowboard", "handball", "running"], "colors": ["red", "blue", "yellow", "black", "white", "green"], "fruits": ["apple", "bannana", "orange", "kiwi", "strawberry", "watermelon"], "classes": ["math", "history", "science", "english", "spanish", "physics"]}

gameKeys= []
for key in gameDict.keys():
    gameKeys.append(key)

activeFlag = True

while activeFlag:
    gameCategoty = gameKeys[random.randint(0, 3)]
    gameWord = gameDict[gameCategoty][random.randint(0, 5)]
    
    blankWord = []
    for letter in gameWord:
        blankWord.append("-")

    print(f"\nGuess a {len(gameWord)} letter word form the following category: {gameCategoty.title()}")
    
    guess = ""
    guessCount = 0
    
    activeFlag2 = True
    while activeFlag2:
        print("".join(blankWord))
        guess = str(input("\nEnter your guess: "))
        guessCount += 1
        if guess == gameWord:
            print(f"Correct! You guessed the word in {guessCount} guesses.")
            activeFlag2 = False
        else:
            print("That is not correct. Let us reveal a letter to help you!")

            activeFlag3 = True
            while activeFlag3:
                letterIndex = random.randint(0, len(blankWord) - 1)
                if blankWord[letterIndex] == "-":
                    blankWord[letterIndex] = gameWord[letterIndex]
                    activeFlag3 = False
    activeFlag = str(input("Would you like to play again (y/n): ")).lower() == "y"

print("\nThank you for playing our game.")