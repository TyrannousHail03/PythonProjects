import sys


# Confirms that the user wants to continue using the program
def confirmation():
    confirmation_input = input("Welcome to TyrannousHail03's Six Trig Function Calculator. Would you like to continue?")
    if confirmation_input.lower() == "yes" or confirmation_input == "y":
        print("Please define the sides of the triangle below, as prompted:")
    elif confirmation_input.lower() == "no" or confirmation_input == "n":
        print("The program will now exit.")
        sys.exit()
    else:
        print("Sorry, that was not understood. Please try again.")
        confirmation()


confirmation()

# Gives a visual representation of the triangle for the user to base their answers off of
print("     /|    ")
print(" C  / |  A ")
print("   /__|    ")
print("     B     ")

hypotenuse = int(input("Enter the value of the hypotenuse (Side C): "))
adjacent = int(input("Enter the value of the side adjacent to the angle you are solving for: "))
opposite = int(input("Enter the value of the opposite side to the angle you are solving for: "))

# Basic Trig Functions
sin = f"sin = {opposite}/{hypotenuse}"
cos = f"cos = {adjacent}/{hypotenuse}"
tan = f"tan = {opposite}/{adjacent}"

# Inverse Trig Functions
csc = f"csc = {hypotenuse}/{opposite}"
sec = f"sec = {hypotenuse}/{adjacent}"
cot = f"cot = {adjacent}/{opposite}"


# Gives the user the data they want based off the data provided:
def answers():
    answers_input = input("\nWhich trig function would you like to find?")
    if answers_input.lower() == "sin" or answers_input.lower() == "sine":
        print(sin)
        again()
    if answers_input.lower() == "cos" or answers_input.lower() == "cosine":
        print(cos)
        again()
    if answers_input.lower() == "tan" or answers_input.lower() == "tangent":
        print(tan)
        again()
    if answers_input.lower() == "csc" or answers_input.lower() == "cosecant":
        print(csc)
        again()
    if answers_input.lower() == "sec" or answers_input.lower() == "secant":
        print(sec)
        again()
    if answers_input.lower() == "cot" or answers_input.lower() == "cotangent":
        print(cot)
        again()
    elif answers_input.lower() == "quit":
        sys.exit()
    else:
        print("Sorry that was not understood. Please try again. To quit the program, simply type quit.")
        answers()


def again():
    again_input = input("Would you like to find another answer?")
    if again_input.lower() == "yes" or again_input.lower() == "y":
        answers()
    if again_input.lower() == "no" or again_input.lower() == "n":
        sys.exit()
    else:
        print("Sorry, that was not understood. Please try again.")
        again()

answers()

# Version 1.0.3 Release Notes:
# 1. Rewrote variables with formatted strings
# 2. Fixed formatting
# 3. Added if __name__ = "__main__": implementation
# 4. Changed side input to be int from start
