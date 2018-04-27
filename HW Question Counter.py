import sys

# Short Intro
print("Welcome to TyrannousHail03's HW Question Counter.")

# Defines the count variable
questionCount = 0

# Confirms that user would like to continue using program
def confirmation():
    confirm = input("Would you like to continue?")
    if confirm.lower() == "yes" or confirm.lower() == "y":
        print("\n")
    if confirm.lower() == "no" or confirm.lower() == "n":
        print("The program will now exit.")
        sys.exit()
    else:
        print("\n Sorry that was not understood. Please try again.")

confirmation()

def confirmation2():
    confirm2 = input("Would you like to continue?")
    if confirm2.lower() == "yes" or confirm2.lower() == "y":
        print("\n")
        mode()
    if confirm2.lower() == "no" or confirm2.lower() == "n":
        print("The program will now exit.")
        print("The total number of HW Question you have to do is: " + str(questionCount))
        sys.exit()
    else:
        print("\n Sorry that was not understood. Please try again. \n")
        confirmation2()

def defined():
    defIn1 = int(input("\nWhat is the lowerst number of the defined range?"))
    defIn2 = int(input("What is the highest number of the defined range?\n"))
    evensCount = 1
    while defIn1 != defIn2:
        evensCount += 1
        defIn1 += 1
    global questionCount
    questionCount += evensCount
    confirmation2()


def others():
    othersIn1= int(input("\nWhat is the lowest number in the range?"))
    othersIn2= int(input("What is the highest number in the range?"))
    othersCount = 0
    while othersIn1 != othersIn2:
        othersCount += 1
        othersIn1 += 1
    global questionCount
    questionCount = othersCount
    confirmation2()


def eo():
    eoIn1 = int(input("\n What is the lowest number in the range?"))
    eoIn2 = int(input("What is the highest number in the range?"))
    eoCount = 0
    while eoIn1 <= eoIn2:
        eoIn1 += 4
        eoCount += 1
    global questionCount
    questionCount += eoCount
    confirmation2()

# Checks to see if the user needs to go through evens or odds, or every other of either.
def mode():
    print("What mode do you want to count in?")
    print("Your options are: Defined, Evens/Odds, or Every other Odd/Even")
    modeCheck = input("Enter: 'def' for Defined, 'e' for Evens, 'o' for Odds, 'eoo' "
                      "for Every Other Odd, and 'eoe' for every other even.")
    if modeCheck.lower() == "def":
        defined()
    if modeCheck.lower() == "e" or modeCheck.lower() == "o":
        others()
    if modeCheck.lower() == "eoo" or modeCheck.lower() == "eoe":
        eo()
mode()
