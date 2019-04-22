'''This program is for calculating Velocity (Initial, Final), Acceleration, Distance, and Time'''

import sys
from vadtformulas import vadtformulas

class options:
    def time(self):
        o = options
        v = vadtformulas()
        print("Which way would you like to solve for Time?")
        print("1. ")

    def distance_options(self):
        o = options()
        v = vadtformulas()
        print("Which way would you like to solve for Distance?")
        print("1. Using Initial Velocity, Final Velocity, and Time")
        print("2. Using Initial Velocity, Acceleration, and Time")
        self.dist_pick = input("Enter the option number here: ")
        if self.dist_pick == "1":
            v.ift_distance()
        elif self.dist_pick == "2":
            v.iat_distance()
        elif self.dist_pick.lower() == "exit" or self.dist_pick.lower() == "esc":
            sys.exit()
        else:
            print("Sorry, that was not understood. Please try again. \n")
            o.distance_options()
    def FinalVelocity_Options(self):
        o = options()
        v = vadtformulas()
        print("Which way would you like to solve for Final Velocity?")
        print("1. Using Initial Velocity, Acceleration, and Time")
        print("2. Using Initial Velocity, Acceleration, and Distance")
        self.fv_pick = input("Enter the option number here:")
        if self.fv_pick == "1":
            print("\n")
            v.iat_fv()
        elif self.fv_pick == "2":
            print("\n")
            v.iad_fv()
        elif self.fv_pick.lower() == "esc" or self.fv_pick.lower() == "exit":
            sys.exit()
        else:
            print("Sorry, that was not understood. Please try again \n")
            o.FinalVelocity_Options()
    def mode(self):
        o = options()
        print("\nYour options for calculations are:")
        print("1. Final Velocity (FV)")
        print("2. Distance (DIST)")
        self.pick = input("What would you like to calculate?")
        if self.pick.lower() == "1":
            print("\n")
            o.FinalVelocity_Options()
        elif self.pick.lower() == "2":
            print("\n")
            o.distance_options()
        elif self.pick.lower() == "esc" or self.pick.lower() == "exit":
            print("\n")
            sys.exit()
        else:
            print("Sorry, that was not understood. Please try again. \n")
            o.mode()

