LogOnInformation = {"mooman74":"alskes145", "meramo1986":"kehns010101", "nickyD":"world1star", "george2":"booo3oha", "admin00":"admin1234"}

print("Welcome to the Database Admin Program\n")

name = str(input("Enter your username: "))
if name in LogOnInformation.keys():
    pasw = str(input("Enter your password: "))
    if LogOnInformation[name] == pasw:
        print(f"\nHello {name}! Youre logged in!")
        if name == "admin00":
            print("\nHere is the current user database:")
            for key in LogOnInformation:
                print(f"\tUsername: {key}\t\tPassword: {LogOnInformation[key]}")
        else:
            change = str(input("Would you like to change your password: ")).lower()
            if change == "yes":
                newPasw = str(input("What would you like your new password to be: "))
                if len(newPasw) >= 8:
                    LogOnInformation[name] = newPasw
                    print(f"\n{name} your password is {newPasw}")
                else:
                    print(f"{newPasw} not the minimum eight characters.")
                    print(f"\n{name} your password is {pasw}")
            else:
                print("Goodbye!")
    else:
        print("Password incorrect!")
else:
    print("Username not in database, goodbye.")
