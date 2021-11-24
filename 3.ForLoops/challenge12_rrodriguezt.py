import cmath

print("Wellcome to the Quadratic Equation Solver App.\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

num = int(input("How many equations would you like to solve today: "))

for i in range(num):
    print(f"\nSolving the equation #{i}")
    print("-------------------------------------------------------------\n")
    coefA = float(input("Please enter your value of a (coefficient of x^2): "))
    coefB = float(input("Please enter your value of b (coefficient of x): "))
    coefC = float(input("Please enter your value of c (coefficient): "))

    print(f"The solutions to {coefA}x^2 + {coefB}x + {coefC} are:\n")
    print(f"\tx1 = ({(-coefB+cmath.sqrt(coefB**2-(4*coefA*coefC)))/(2*coefA)})")
    print(f"\tx2 = ({(-coefB-cmath.sqrt(coefB**2-(4*coefA*coefC)))/(2*coefA)})")

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")