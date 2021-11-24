users = ["eramom", "footea", "davisv", "papinukt", "allenj"]

print("Welcome to the Shipping Accounts App\n")

name = str(input("Hello, what is your username: ")).lower()

if name in users:
    print(f"\nHello {name}. Welcome back to your account.")
    print("Current shipping prieces are as follows:\n")
    print("Shiping orders 0 to 100:\t\t$5.10 each")
    print("Shiping orders 100 to 500:\t\t$5.00 each")
    print("Shiping orders 500 to 1000:\t\t$4.95 each")
    print("Shiping orders over 1000:\t\t$4.80 each")

    num = int(input("\nHow many items would you like to ship: "))
    price = 0
    cost = 0
    if num <= 100:
        cost = 5.1
        price = num * cost
    elif num > 100 and num <= 500:
        cost = 5.0
        price = num * cost
    elif num > 500 and num <= 1000:
        cost = 4.95
        price = num * cost
    else:
        cost = 4.8
        price = num * cost
    print(f"To ship {num} items it will cost you ${round(price, 2)} at ${cost} per item.")

    place = str(input("\nWould you like to place this order (y/n): ")).lower()
    if place == "y":
        print(f"Okay. Shipping your {num} items.")
    else:
        print("Okay, no order is being placed at this time.")
else:
    print("Sorry, you do not have an account with us. Goodbye")