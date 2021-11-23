print("Wellcome to the Favorite Teachers Program\n")

favTeachers = []

favTeachers.append(str(input("Who is your first favorite teacher: ")).title())
favTeachers.append(str(input("Who is your sedcond favorite teacher: ")).title())
favTeachers.append(str(input("Who is your third favorite teacher: ")).title())
favTeachers.append(str(input("Who is your fourth favorite teacher: ")).title())

print(f"\nYour favorite teachers ranked are: {favTeachers}")
sortedList = sorted(favTeachers)
print(f"Your favorite teachers alphabetically are: {sortedList}")
print(F"Your favorite teachers in reverse alphabetical order are: {sortedList[::-1]}")

print(f"\nYour top two teachers are: {favTeachers[0]} and {favTeachers[1]}")
print(f"Your next two favorite teachers are: {favTeachers[2]} and {favTeachers[3]}")
print(f"Your last favorite teacher is: {favTeachers[3]}")
print(f"You have a total of {len(favTeachers)} favorite teachers")

favTeachers.insert(0, str(input(f"\nOops, {favTeachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ")).title())

print(f"\nYour favorite teachers ranked are: {favTeachers}")
sortedList = sorted(favTeachers)
print(f"Your favorite teachers alphabetically are: {sortedList}")
print(F"Your favorite teachers in reverse alphabetical order are: {sortedList[::-1]}")

print(f"\nYour top two teachers are: {favTeachers[0]} and {favTeachers[1]}")
print(f"Your next two favorite teachers are: {favTeachers[2]} and {favTeachers[3]}")
print(f"Your last favorite teacher is: {favTeachers[4]}")
print(f"You have a total of {len(favTeachers)} favorite teachers")

favTeachers.remove(str(input("\nYou've decided you no longuer like a teacher. Wich teacher would you like to remove from your list: ")).title())

print(f"\nYour favorite teachers ranked are: {favTeachers}")
sortedList = sorted(favTeachers)
print(f"Your favorite teachers alphabetically are: {sortedList}")
print(F"Your favorite teachers in reverse alphabetical order are: {sortedList[::-1]}")

print(f"\nYour top two teachers are: {favTeachers[0]} and {favTeachers[1]}")
print(f"Your next two favorite teachers are: {favTeachers[2]} and {favTeachers[3]}")
print(f"Your last favorite teacher is: {favTeachers[3]}")
print(f"You have a total of {len(favTeachers)} favorite teachers")