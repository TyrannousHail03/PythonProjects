# This was written for a quick checksum check
import sys


def again():
    again_input = input("\nWould you like to do another comparison? ").lower()
    if again_input == "y" or again_input == "yes":
        compare()
    elif again_input == "n" or again_input == "no":
        sys.exit()
    else:
        print("Sorry, that was not understood. Please try again.\n")
        again()


def compare():
    string1 = input("String #1: ").lower()
    string2 = input("String #2: ").lower()
    if string1 == string2:
        print("It's a match!")
    else:
        print("Not a match.")
    again()


compare()
