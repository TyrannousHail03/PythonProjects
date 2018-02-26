import sys

def startCalc():
  print("Welcome to TyrannousHail03's GCD and LCM Calculator")
  start = input("Would you like to continue?")
  if start.lower() == "yes" or start.lower() == "y":
    print("\n")
  elif start.lower() == "no" or start.lower() == "n":
    print("The program will now exit.")
    sys.exit()
  else:
    print("Sorry, that was not understood. Please try again.")
    startCalc()

startCalc()

number1 = input("What is the first number you want to calculate?")
number2 = input("What is the second number you want to calculate?")
number1 = int(number1)
number2 = int(number2)

def gcd():
  a = 0
  global b
  c = 1
  if number1 > number2:
    a = number1
  else:
    a = number2
  while c != a:
    if number1%c == 0 and number2%c == 0:
      b = c
    c = c + 1
  print("\nGCD = " + str(b))

def lcm():
  d = number1 * number2 / b
  print("LCM = " + str(d))

gcd()
lcm()
# Add if statement in getNumbers to make sure input = integer
# For expanded version, write a function to store the numbers in a list...
