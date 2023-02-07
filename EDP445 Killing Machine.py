print("Would you like to kill EDP445?")
response = None
while response not in {"yes", "no"}:
    response = input("Please enter yes or no: ")

    if response == ("yes"):
        print("You have successfully killed EDP445.")

    elif response == ("no"):
        print("You spared EDP445. (Why?)")
