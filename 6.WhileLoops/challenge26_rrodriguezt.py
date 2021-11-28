print("Welcome to the Factor Generator App")

activeFlag = True

while activeFlag == True:
    num = int(input("\nEnter a number to determinate all factors of that number: "))

    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print("\nFactors of {num} are:")
    for i in factors:
        print(i)
    
    print("\nIn summary:")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]} * {factors[-i - 1]} = {factors[i] * factors[-i -1]}")

    chose = str(input("\nRun again (y/n): ")).lower()
    if chose == "n":
        activeFlag = False

print("Thank you for using the program. Have a great day.")