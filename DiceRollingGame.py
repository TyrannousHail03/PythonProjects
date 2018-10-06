'''This program rolls a pair of dice and asks the user to guess the sum of the dice. If the user guesses correctly, they win.
   This program was initially written during my run through of CodeAcademy's Python course.'''

from random import randint
from time import sleep


def get_user_guess():
    guess = int(input("What is your guess?"))
    return guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print("Maximum Value: %d" % max_val)
    guess = get_user_guess()
    if guess > max_val:
        print("Sorry, that number is too high.")
    else:
        print("Rolling... ")
        sleep(2)
        print("1st Roll: %d" % first_roll)
        sleep(1)
        print("2nd Roll: %d" % second_roll)
        total_roll = first_roll + second_roll
        print("Total Roll: %d" % total_roll)
        sleep(1)
        if guess == total_roll:
            print("Congratulations, you've won!")
        else:
            print("Sorry, you have lost.")


roll_dice(6)

