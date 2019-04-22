import sys
from vadtoptions import options

def initiate():
    o = options()
    print("Welcome to TyrannousHail03's Physics VADT Calculator")
    confirmation = input("Would you like to continue?")
    if confirmation.lower() == "y" or confirmation.lower() == "yes":
        o.mode()
    elif confirmation.lower() == "n" or confirmation.lower() == "no":
        sys.exit()
    else:
        print("\nSorry, that was not understood. Please try again.")
        initiate()


initiate()
