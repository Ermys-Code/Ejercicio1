import math

print("Wellcome to the Factorial Calculator App\n")

num = int(input("What number would you like to compute the factorial of? "))
print(f"{num}! =", end=" ")

for i in range(num-1):
    print(i + 1, end="*")
print(num)

print("Here is the result from the math library:")
print(f"The factorial of {num} is {math.factorial(num)}!")

print("Here is the result from my own algorithm:")

fac = 1
for i in range(1, num + 1):
    fac = fac * i
print(f"The factorial of {num} is {fac}!")

print(f"\nIt is shown twice that {num}! = {math.factorial(num)} (with excitement)")