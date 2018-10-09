# This was written for a quick checksum check
import sys

def again():
    again_input = input("\nWould you like to do another comparison? ")
    if again_input.lower() == "y" or again_input.lower() == "yes":
        compare()
    elif again_input.lower() == "n" or again_input.lower() == "no":
        sys.exit()
    else:
        print("Sorry, that was not understood. Please try again.\n")
        again()

def compare():
    string1 = input("String #1: ")
    string2 = input("String #2: ")
    if string1 == string2:
        print("It's a match!")
    else:
        print("Not a match.")
    again()

compare()
