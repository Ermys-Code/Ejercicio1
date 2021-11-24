print("Welcome to the Right Triangle Solver App\n")

legOne = float(input("What is the first leg of the triangle: "))
legTwo = float(input("What is the second leg of the triangle: "))

hypotenuse = round((legOne**2 + legTwo**2) ** 0.5, 3)
area = round((legOne * legTwo) / 2, 3)

print(f"\nFor a triangle with legs of {legOne} and {legTwo} the hypotenuse is {hypotenuse}")
print(f"For a triangle with legs of {legOne} and {legTwo} the area is {area}")