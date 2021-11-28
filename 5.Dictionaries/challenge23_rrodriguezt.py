print("Welcome to the Yes or No Issue App\n")

issue = str(input("What is the yes or no issue you will be voting on today: "))
voters = int(input("What is the number of voters you will allow on the issue: "))
pasw = str(input("Enter a password for polling results: "))

votersCounter = 0
yCount = 0
nCount = 0
results = {}

for i in range(voters):
    name = str(input("\nEnter your full name: ")).title()
    if name in results.keys():
        print("You can not vote twice.")
    else:
        votersCounter += 1
        print(f"Here is our issue: {issue}")
        vote = str(input("What do you think...yes or no: ")).lower()
        if vote[0] == "y":
            yCount += 1
            results[name] = "Yes"
        elif vote[0] == "n":
            nCount += 1
            results[name] = "No"
        else:
            print("That is not a yes or no answer, but okay...")
            results[name] = vote
        print(f"Thank you {name}! YOur vote of {vote} has been recorded.\n")

print(F"\nThe following {votersCounter} people voted:")
for value in results.keys():
    print(value)

print(f"\nOn the following issue: {issue}")
if yCount > nCount:
    print(f"Yes wins! {yCount} votes to {nCount}.")
elif yCount < nCount:
    print(f"No wins! {nCount} votes to {yCount}.")
else:
    print(f"This is a tie! {yCount} votes to {nCount}.")

if str(input("\nTo see the voting results enter the admin password: ")) == pasw:
    for key, value in results.items():
        print(f"Voter: {key}\t\tVote: {value}")
else:
    print("Sorry, that is not the correct password. Goodbye...")

print("\nThank you for using the Yes or NO Issue Polling App.")