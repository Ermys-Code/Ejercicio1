import random

dic = {"rock":0, "paper":1, "scissors":2}
dicList = list(dic.keys())
pScore = 0
cScore = 0
pPick = 0
cPick = 0
winner = ""

print("Welcome to a game of Rock, Paper, Scissors\n")

rounds = int(input("How many rounds would you want to play: "))

for i in range(rounds):
    print(f"\nRound {i + 1}")
    print(f"Player: {pScore}\tComputer: {cScore}")
    pPick = str(input("Time to pick...rock, paper, scissors: ")).lower()
    if pPick in dicList:
        pPick = dic[pPick]
        cPick = random.randint(0,2)
        print(f"Computer: {dicList[cPick]}")
        print(f"Player: {dicList[pPick]}")
        if cPick == pPick:
            print("It is a tie, how borring!")
            print("This round was a tie.")
        else:
            if pPick == 0 and cPick == 2 or pPick == 1 and cPick == 0 or pPick == 2 and cPick == 1:
                if pPick == 0:
                    print("Rock break Scissors")
                elif pPick == 1:
                    print("Paper cover Rock")
                elif pPick == 2:
                    print("Scissors cut Paper")
                print(f"You win round {i + 1}")
                pScore += 1
            elif cPick == 0 and pPick == 2 or cPick == 1 and pPick == 0 or cPick == 2 and pPick == 1:
                if cPick == 0:
                    print("Rock break Scissors")
                elif cPick == 1:
                    print("Paper cover Rock")
                elif cPick == 2:
                    print("Scissors cut Paper")
                print(f"Computer win round {i + 1}")
                cScore += 1
    else:
        print("That is not a valid game option")
        print("Computer gets the point")
        cScore += 1
if pScore > cScore:
    winner = "PLAYER!!!"
elif pScore < cScore:
    winner = "Computer :c"
else:
    winner = "The game was a tie."

print("\nFinal Game Results")
print(f"\tRounds Played: {rounds}")
print(f"\tPlayer Score: {pScore}")
print(f"\tComputer Score: {cScore}")
print(f"\tWinner: {winner}")