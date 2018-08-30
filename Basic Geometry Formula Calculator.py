import sys

def CylinderVolume():
    print("You have reached the CylinderVolume() function")


def mode():
    userMode = input("")
    print("You have reached the mode() function")

print("Welcome to TyrannousHail03's Basic Geometry Formula Calculator. Would you like to continue?")

def startConfirmation():
    confirmation = input("Y/N ")
    if confirmation.lower() == "y":
        mode()
    elif confirmation.lower() == "n":
        print("Program exiting...")
        sys.exit()
    else:
        print("Sorry, that was not understood. Please try again.")
        startConfirmation()

startConfirmation()