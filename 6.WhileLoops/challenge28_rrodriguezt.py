import time

print("Welcome to the Prime Number App")

activeFlag = True

while activeFlag == True:
    print("\nEnter 1 to determinate if a specific number is prime")
    print("Enter 2 to determinate all prime numbers within a set range.")
    choice = str(input("Enter your choice 1 or 2: "))

    if choice == "1":
        num = int(input("\nEnter a number to determine if it is prime or not: "))
        primeStatus = True
        for i in range(2, num):
            if num % i == 0:
                primeStatus = False
                break
        if primeStatus == True:
            print(f"{num} is prime!")
        else:
            print(f"{num} is not prime!")
    elif choice == "2":
        low = int(input("\nEnter the lower bound of your range: "))
        upp = int(input("Enter the upper bound of your range: "))
        primes = []
        startTime = time.time()
        for i in range(low, upp +1):
            if i > 1:
                primeStatus = True
                for n in range(2, i):
                    if i % n == 0:
                        primeStatus = False
                        break

            else:
                primeStatus = False
            if primeStatus == True:
                primes.append(i)
        endTime = time.time()
        deltaTime = round(endTime - startTime, 4)
        print(f"\nCalculations took a total of {deltaTime} seconds.")
        print(f"The following numbers between {low} and {upp} are prime:")
        input("Press enter to continue.")
        for i in primes:
            print(i)
    else:
        print("\nThis is not a valid option.")
    
    activeFlag = str(input("Would you like to run the program again (y/n): ")).lower() == "y"

print("\nThank you for using the program. Have a nice day.")