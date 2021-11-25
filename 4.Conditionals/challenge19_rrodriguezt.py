import random

print("Welcome to the Guess My Number App\n")

name = str(input("Hello! What is your name: ")).title()
print(f"Well {name}, I am thinking of a number between 1 and 20.\n")

num = random.randint(1, 20)
guess = -1
count = 0

for i in range(5):
    guess = int(input("Take a guess: "))
    count += 1
    if guess < num:
        print("Your guess is too low.\n")
    elif guess > num:
        print("Your guess is too high.\n")
    else:
        break

if guess == num:
    print(f"Good job {name}! You guessed my number in {count} guesses!")
else:
    print(f"Game Over. The number I was thinking of was {num}")

