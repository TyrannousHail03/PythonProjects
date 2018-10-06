# This was written for a quick checksum check


def again():
    print("\nWould you like to do another comparison? ")
    button = msvcrt.getch()


def compare():
    string1 = input("String #1: ")
    string2 = input("String #2: ")
    if string1 == string2:
        print("It's a match!")
    else:
        print("Not a match.")
    again()


compare()
