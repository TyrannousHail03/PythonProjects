import sys


def small(age):
    small_list = (0, 15, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80)
    print(f"Your dog's age is: {small_list[age]}")


def medium(age):
    medium_list = (0, 15, 24, 28, 32, 36, 42, 47, 51, 56, 60, 65, 69, 74, 78, 83, 87)
    print(f"Your dog's age is: {medium_list[age]}")


def large(age):
    large_set = (0, 15, 24, 28, 32, 36, 45, 50, 55, 61, 66, 72, 77, 82, 88, 93, 120)
    print(f"Your dog's age is: {large_set[age]}")


def dog():
    dog1 = input('What size dog do you have?')
    age = int(input("How old is your dog?"))
    if age > 16:
        print("Sorry, this calculator does not calculate above 16 human years in this version.")
        sys.exit()
    if dog1.lower() == 'small':
        small(age)
    elif dog1.lower() == 'medium':
        medium(age)
    elif dog1.lower() == 'large':
        large(age)
    else:
        print("Sorry, that was not understood.")
        dog()


if __name__ == "__main__":
    dog()

# Changed lists of size ages to Tuples to increase processing speed
# Simplified input operations
# Got rid of dog size confirmations
