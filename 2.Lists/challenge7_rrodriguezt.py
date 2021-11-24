numStrings = ["15", "100", "55", "42"]
numInts = [15, 100, 55, 42]
numFloats = [50.5, 30.6, 80.1, 10.2]
numList = [[1,2,3], [4,5,6], [7,8,9]]

print("\t\tSummary Table")

print(f"\nThe variable numStrings is a {type(numStrings)}")
print(f"It contains the elements: {numStrings}")
print(f"The element {numStrings[0]} is a {type(numStrings[0])}")

print(f"\nThe variable numInts is a {type(numInts)}")
print(f"It contains the elements: {numInts}")
print(f"The element {numInts[0]} is a {type(numInts[0])}")

print(f"\nThe variable numFloats is a {type(numFloats)}")
print(f"It contains the elements: {numFloats}")
print(f"The element {numFloats[0]} is a {type(numFloats[0])}")

print(f"\nThe variable numList is a {type(numList)}")
print(f"It contains the elements: {numList}")
print(f"The element {numList[0]} is a {type(numList[0])}")

print(f"\nNow sorting numStrings and numInts...")
print(f"Sorted numStrings: {sorted(numStrings)}")
print(f"Sorted numInts: {sorted(numInts)}")

print(f"\nStrings are sorted alphabetically while integers are sorted numerically!")