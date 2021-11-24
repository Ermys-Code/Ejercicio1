print("Welcome to the Fibonacci Calculator App\n")

num = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

print(f"\nThe first {num} numbers of the Fibonacci sequence are: ")
calc = [1, 1]
fList = [1]
for i in range(num - 1):
    i = calc[1] 
    calc[1] = calc[0] + calc[1]
    calc[0] = i
    fList.append(i)
    print(i)

print(f"\nThe corresponding Golden Ratio values are: ")
firstNum = 1
secondNum = 0
rList = []
for i in range(num - 1):
    newValue =  fList[firstNum] / fList[secondNum]
    print(newValue)
    firstNum += 1
    secondNum += 1
    rList.append(newValue)

print(f"\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")