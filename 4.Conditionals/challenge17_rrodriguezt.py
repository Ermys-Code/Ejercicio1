import random

print("Welcome to the Coin Toss App\n")

print("I will flip a coin a set numbers of times.")
num = int(input("How many times would you like me to flip the coin: "))
see = str(input("Would you like to see the result of each flip (y/n): ")).lower()

heads = 0
tiles = 0

print("\nFlipping!!!\n")

for i in range(num):
    flip = random.randint(0, 1)
    if flip == 0:
        heads += 1
        if see == "y":
            print("HEADS")
    else:
        tiles += 1
        if see == "y":
            print("TILES")
    if heads == tiles:
        print(f"At {i} flips, the number of heads and tiles were equal at {heads} each.")

print(f"\nResults of flipping a coin {num} times:\n")
print("Side\t\tCount\t\tPercentage")
print(f"Heads\t\t{heads}/{num}\t\t{round((heads/num) * 100, 2)}%")
print(f"Tiles\t\t{tiles}/{num}\t\t{round((tiles/num) * 100, 2)}%")