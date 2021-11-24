print("Welcome to the Average Calculator App\n")

name = str(input("What is your name: ")).title()
num = int(input("How many grades would you like to enter: "))

gradeList = []
count = 0
while count < num:
    gradeList.append(int(input("Enter grade: ")))
    count += 1

gradeList.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for i in gradeList:
    print(f"\t{i}")

print(f"\n{name}'s Grade Summary:")
print(f"\tTotal Number of Grades: {len(gradeList)}")
print(f"\tHighest Grade: {gradeList[0]}")
print(f"\tLowest Grade: {gradeList[len(gradeList) - 1]}")
average = sum(gradeList) / len(gradeList)
print(f"\tAverage: {average}")

desired = int(input("\nWhat is your desired average: "))

a = sum(gradeList) / len(gradeList)
x = a * len(gradeList)
x = (desired * (len(gradeList) + 1)) - x

print(f"\nGood luck {name}!")
print(f"You will need to get a {x} on your next assignment to earn a {desired} average.")

print("\nLets see what your average could have been if you did better/worse on an assignment.")
toChange = int(input("What grade would you like to change: "))
newGrade = int(input(f"What grade would you like to change {toChange} to: "))

newGradeList = gradeList.copy()
newGradeList.remove(toChange)
newGradeList.append(newGrade)
newGradeList.sort(reverse=True)
print("\nNew Grades Highest to Lowest: ")
for i in newGradeList:
    print(f"\t{i}")

print(f"\n{name}'s New Grade Summary:")
print(f"\tTotal Number of Grades: {len(newGradeList)}")
print(f"\tHighest Grade: {newGradeList[0]}")
print(f"\tLowest Grade: {newGradeList[len(newGradeList) - 1]}")
newAverage = sum(newGradeList) / len(newGradeList)
print(f"\tAverage: {newAverage}")

print(f"\nYour new average would be a {newAverage} compared to your real average of {average}!")
print(f"That is a change of {round(newAverage - average, 2)} points!")

print("\nToo bad your original grades are still the same!")
print(gradeList)
print("You should go ask for extra credit!")