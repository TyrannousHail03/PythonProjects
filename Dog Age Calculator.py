import sys


def small():
    small_list = [0, 15, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]
    small_input = input("How old is your dog?")
    small_age = int(small_input)
    if small_age > 16:
        print("Sorry, this calculator does not calculate above 16 human years in this version.")
        sys.exit()
    small_set2 = small_list[small_age]
    print("Your dog's age is: " + str(small_set2))


def medium():
    medium_list = [0, 15, 24, 28, 32, 36, 42, 47, 51, 56, 60, 65, 69, 74, 78, 83, 87]
    medium_input = input("How old is your dog?")
    medium_age = int(medium_input)
    if medium_age > 16:
        print("Sorry, this calculator does not calculate above 16 human years in this version.")
        sys.exit()
    medium_set2 = medium_list[medium_age]
    medium_set2 = str(medium_set2)
    print("Your dog's age is: " + str(medium_set2))


def large():
    large_input = input("How old is your dog?")
    large_set = [0, 15, 24, 28, 32, 36, 45, 50, 55, 61, 66, 72, 77, 82, 88, 93, 120]
    large_age = int(large_input)
    if large_age > 16:
        print("Sorry, this calculator does not calculate above 16 human years in this version.")
        sys.exit()
    large_set2 = large_set[large_age]
    large_set2 = str(large_set2)
    print("Your dog's age is: " + str(large_set2))


def dog():
    dog1 = input('What size dog do you have?')
    if dog1.lower() == 'small':
        print("Okay, you have a small dog.")
        small()
    elif dog1.lower() == 'medium':
        print("Okay, you have a medium dog.")
        medium()
    elif dog1.lower() == 'large':
        print("Okay, you have a large dog.")
        large()
    else:
        print("Sorry, I did not understand that.")
        dog()


dog()
