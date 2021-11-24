print("Welcome to the Binary/Hexadecimal Converter App\n")

num = int(input("Compute binary and hexadecimal values up to the following decimal number: "))

newValue = 1
numberList = []
for i in range(num):
    numberList.append(newValue)
    newValue += 1

binaryList = []
hexList = []
for i in numberList:
    binaryList.append(bin(i))
    hexList.append(hex(i))

print("Generating lists.....Complete!\n")

print("Using slices, we will now show a portion of each list.")
startValue = int(input("What decimal number would you like to start at: "))
stopValue = int(input("What decimal number would you like to stop at: "))

print(f"\nDecimal values from {startValue} to {stopValue}:")
for i in range(startValue - 1, stopValue):
    print(numberList[i])

print(f"\nBinary values from {startValue} to {stopValue}:")
for i in range(startValue - 1, stopValue):
    print(binaryList[i])

print(f"\nHexadecimal values from {startValue} to {stopValue}:")
for i in range(startValue - 1, stopValue):
    print(hexList[i])

input(f"\nPress Enter to see all values from 1 to {len(numberList)}")
print("Decimal----Binary----Hexadecimal")
print("-------------------------------------------------")
for i in range(num):
    print(f"{numberList[i]}----{binaryList[i]}----{hexList[i]}")