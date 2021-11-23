print(f"Wellcome to the Basketball Roster Program")

roster = []

roster.append(str(input("Who is your point guard: ")).title())
roster.append(str(input("Who is your shooting guard: ")).title())
roster.append(str(input("Who is your small forward: ")).title())
roster.append(str(input("Who is your power forward: ")).title())
roster.append(str(input("Who is your center: ")).title())

print("\n\tYour starting 5 for the upcoming basketball season")
print(f"\t\tPoint Guard:\t\t{roster[0]}")
print(f"\t\tShooting Guard:\t\t{roster[1]}")
print(f"\t\tSmall FOrward:\t\t{roster[2]}")
print(f"\t\tPower Forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t{roster[4]}")

print(f"\nOh no, {roster[2]} is injured.")
injuredPlayer = roster.pop(2)
print(f"Your roster only has {len(roster)} players.")
addedPlayer = str(input(f"Who will take {injuredPlayer}'s spot: ")).title()
roster.insert(2, addedPlayer)

print(f"\n\tYour starting 5 for the upcoming basketball season")
print(f"\t\tPoint Guard:\t\t{roster[0]}")
print(f"\t\tShooting Guard:\t\t{roster[1]}")
print(f"\t\tSmall FOrward:\t\t{roster[2]}")
print(f"\t\tPower Forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t{roster[4]}")

print(f"\nGood luck {addedPlayer} you will do great!")
print(f"Your roster now has {len(roster)} players.")