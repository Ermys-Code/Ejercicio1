
print("Welcome to the Even Odd Number Sorter App\n")

activeFlag = True

while activeFlag == True:
    numbers = str(input("Enter in a string of numbers separated by a comma (,): "))
    for i in numbers:
        if i == " ":
            numbers = numbers.replace(i, "")
    numList = numbers.split(",")

    evens = []
    odds = []

    print("\n----Resilt Summary----")
    for i in numList:
        if int(i) % 2 == 0:
            evens.append(int(i))
            print(f"\t{i} is even!")
        else:
            odds.append(int(i))
            print(f"\t{i} is odd!")

    evens = sorted(evens)
    odds = sorted(odds)

    print(f"\nThe following {len(evens)} numbers are even:")
    for i in evens:
        print(f"\t{i}")

    print(f"\nThe following {len(odds)} numbers are odds:")
    for i in odds:
        print(f"\t{i}")
    
    activeFlag = str(input("Would you like to run the program again (y/n): ")).lower() == "y"
print("Thank you for using the program. Goodbye.")