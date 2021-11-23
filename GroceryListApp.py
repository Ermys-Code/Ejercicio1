import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

shoppingList = ["Meat", "Cheese"]

print(f"Wellcome to the Grocery List App")
print(f"Current Date anf Time: {month}/{day} {hour}:{minute}")
print(f"You currently have {shoppingList[0]} and {shoppingList[1]} on your list")

shoppingList.append(str(input("\nType of food to add to the grocery list: ")).title())
shoppingList.append(str(input("Type of food to add to the grocery list: ")).title())
shoppingList.append(str(input("Type of food to add to the grocery list: ")).title())

print(f"\nHere is your grocery list:")
print(shoppingList)
print(f"Here is your grocery list sorted")
shoppingList = sorted(shoppingList)
print(shoppingList)

print(f"\nSimulating grocery shopping...")

while(len(shoppingList) > 2):
  print(f"\nCurrent grocery list: {len(shoppingList)} items")
  print(shoppingList)
  buyed = str(input("What food did you just buy: ")).title()
  print(f"Removing {buyed} from list...")
  shoppingList.remove(buyed)

print(f"\nCurrent grocery list: {len(shoppingList)} items")

print(f"\n{shoppingList}")

print(f"\nSorry, the store is out of {shoppingList.pop(1)}")
shoppingList.append(str(input("What food would you like instead: ")).title())

print(f"\nHere is what remains on your grocery list:")
print(shoppingList)