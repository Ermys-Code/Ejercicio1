print("Wellcome to the Grade Store App\n")

grade1 = int(input("What is your first grade (0-100):"))
grade2 = int(input("What is your second grade (0-100):"))
grade3 = int(input("What is your third grade (0-100):"))
grade4 = int(input("What is your fourth grade (0-100):"))

gradeList= [grade1, grade2, grade3, grade4]

print(f"\nYour grades are: {gradeList}")

gradeList = sorted(gradeList)
print(f"\nYour grades from highest to lowest are: {gradeList[::-1]}")

print(f"\nThe lowest two grades will now be dropped.")
print(f"Removed grade: {gradeList.pop(0)}")
print(f"Removed grade: {gradeList.pop(0)}")

print(f"\nYour remaining grades are: {gradeList}")
print(f"Nice work! Your highest grade is a {gradeList[1]}")