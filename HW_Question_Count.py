import sys

# Short Intro
print("Welcome to TyrannousHail03's HW Question Counter.")

# Defines the count variable
questionCount = 0


# Confirms that user would like to continue using program
def confirmation():
    confirm = input("Would you like to continue?").lower()
    if confirm == "yes" or confirm == "y":
        print("\n")
    elif confirm == "no" or confirm == "n":
        print("The program will now exit.")
        sys.exit()
    else:
        print("\nSorry that was not understood. Please try again.\n")
        confirmation()


def goAgain():
    confirm2 = input("Would you like to continue?").lower()
    if confirm2 == "yes" or confirm2 == "y":
        print("\n")
        mode()
    if confirm2 == "no" or confirm2 == "n":
        print(f"The total number of HW Question you have to do is: { str(questionCount)}")
        sys.exit()
    else:
        print("\n Sorry that was not understood. Please try again. \n")
        goAgain()


def defined(int1, int2):
    evensCount = 1
    while int1 != int2:
        evensCount += 1
        int1 += 1
    global questionCount
    questionCount += evensCount
    goAgain()


def others(int1, int2):
    othersCount = 0
    while int1 != int2:
        othersCount += 1
        int1 += 1
    global questionCount
    questionCount = othersCount
    goAgain()


def eo(int1, int2):
    eoCount = 0
    while int1 <= int2:
        int1 += 4
        eoCount += 1
    global questionCount
    questionCount += eoCount
    goAgain()


# Checks to see if the user needs to go through evens or odds, or every other of either.
def mode():
    print("What mode do you want to count in?")
    print("Your options are: Defined, Evens/Odds, or Every other Odd/Even")
    modeCheck = input("Enter: 'def' for Defined, 'e' for Evens, 'o' for Odds, 'eoo' "
                      "for Every Other Odd, and 'eoe' for every other even.")
    int1 = int(input("\nWhat is the lowest number in the range?"))
    int2 = int(input("What is the highest number in the range?"))
    if modeCheck.lower() == "def":
        defined(int1, int2)
    if modeCheck.lower() == "e" or modeCheck.lower() == "o":
        others(int1, int2)
    if modeCheck.lower() == "eoo" or modeCheck.lower() == "eoe":
        eo(int1, int2)


if __name__ == "__main__":
    confirmation()
    mode()
