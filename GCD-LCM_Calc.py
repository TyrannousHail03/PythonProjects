import sys


def startCalc():
    print("Welcome to TyrannousHail03's GCD and LCM Calculator")
    start = input("Would you like to continue?").lower()
    if start == "yes" or start == "y":
        print("\n")
    elif start == "no" or start == "n":
        print("The program will now exit.")
        sys.exit()
    else:
        print("Sorry, that was not understood. Please try again.\n")
        startCalc()


def gcd(number1, number2):
    global b
    c = 1
    if number1 > number2:
        a = number1
    else:
        a = number2
    while c != a:
        if number1 % c == 0 and number2 % c == 0:
            b = c
        c = c + 1
    print(f"\nGCD = {b}")


def lcm(number1, number2):
    d = int(number1 * number2 / b)
    print(f"LCM = {d}")


if __name__ == "__main__":
    startCalc()
    number1 = int(input("What is the first number you want to calculate?"))
    number2 = int(input("What is the second number you want to calculate?"))
    gcd(number1, number2)
    lcm(number1, number2)

# 