print("Welcome to the Voter Registration App\n")

name = str(input("Please enter your name: ")).title()
age = int(input("Please enter your age: "))

if age < 18:
    print("\nYou are not old enough to register to vote.")
else:
    print(f"\nCongratulations {name}! You are old enough to register to vote.\n")

    pariesList = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
    print("Here is a list of political parties to join.")
    print(f"\t- {pariesList[0]}")
    print(f"\t- {pariesList[1]}")
    print(f"\t- {pariesList[2]}")
    print(f"\t- {pariesList[3]}")
    print(f"\t- {pariesList[4]}")

    toJoin = str(input("\nWhat party would you like to join: ")).title()

    if toJoin in pariesList:
        print(f"COngratulations {name}! You have joined the {toJoin} party!")
        print(f"Youre a {toJoin} person!")
    else:
        print("That party is not valid.")

