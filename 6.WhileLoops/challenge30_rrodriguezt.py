import random
from types import resolve_bases

print("--------------------Power-Ball Simulator--------------------\n")

whiteBalls = int(input("How many white-balls to draw form for the 5 winning numbers (Normally 69): "))
if whiteBalls < 5:
    whiteBalls = 5

redBalls = int(input("How many red-balls to draw form for the 5 winning numbers (Normally 26): "))
if redBalls < 1:
    redBalls = 1

odds = 1
for n in range(5):
    odds = odds * (whiteBalls - n)
odds = (odds * redBalls) / 120
print(f"You have a 1 in {odds} chance of winning this lottery.")

ticketInterval = int(input("Purchase tickets in what interval: "))

winningNumbers = []
while len(winningNumbers) < 5:
    randNum = random.randint(1, whiteBalls)
    if randNum not in winningNumbers:
        winningNumbers.append(randNum)
winningNumbers = sorted(winningNumbers)
winningNumbers.append(random.randint(1, redBalls))

print("\n\n---------Welcome to the Power-Ball-----------\n")

print("Tonight's winning numbers are: ", end="")
for i in winningNumbers:
    print(i, end="")
print("\n")
input("Press 'Enter' to begin purchasing tickets!!!")

ticketsPurchased = 0
active = True
ticketsSold = []
count = 0
while active:
    while count < ticketInterval:
        lotteryNumbers = []
        while len(lotteryNumbers) < 5:
            randNum = random.randint(1, whiteBalls)
            if randNum not in winningNumbers:
                lotteryNumbers.append(randNum)
        lotteryNumbers = sorted(lotteryNumbers) 
        lotteryNumbers.append(random.randint(1, redBalls))

        if lotteryNumbers not in ticketsSold:
            ticketsPurchased =+ 1
            ticketsSold.append(lotteryNumbers)
            print(lotteryNumbers)
            if lotteryNumbers == winningNumbers:
                print("Winning ticket numbers: ", end="")
                for i in winningNumbers:
                    print(i, end="")
                print(f"\nPurchased a total of {ticketsPurchased}")
                break
            count += 1
    
        else:
            print("Losing ticket generated; disregard...")  

    if ticketsPurchased >= ticketInterval:
        print(f"{ticketsPurchased} tickets purchased so far with no winners...\n")

    active = str(input("Keep purchasing tickets (y/n): ")).lower() == "y"
    if active == False:
        print (f"\nYou bought {ticketsPurchased} tickets and still lost!")
        print("Better luck next time!")
    else:
        count = 0