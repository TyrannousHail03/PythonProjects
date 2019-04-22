import math
class vadtformulas:
    def __init__(self):
        self.vinit = None
        self.vfinal = None
        self.time = None
        self.distance = None
        self.acceleration = None
    def ift_distance(self):
        self.vinit = int(input("\n What is the Initial Velocity? "))
        self.vfinal = int(input("What is the Final Velocity? "))
        self.time = int(input("What is the Time? "))
        self.distance = 0.5 * (self.vinit + self.vfinal) * self.time
        print("Distance: " + str(self.distance) + "m" + "\n")
    def iat_distance(self):
        self.vinit = int(input("\nWhat is the Initial Velocity? "))
        self.acceleration = int(input("What is the Acceleration? "))
        self.time = int(input("What is the Time? "))
        self.distance = (self.vinit * self.time) + (0.5 * self.acceleration * (self.time**2))
        print("Distance: " + str(self.distance) + "m" + "\n")
    def iad_fv(self):
        self.vinit = int(input("What is the Initial Velocity? "))
        self.acceleration = int(input("What is the Acceleration? "))
        self.distance = int(input("What is the Distance? "))
        self.vfinal = math.sqrt((self.vinit ** 2) + (2 * (self.acceleration * self.distance)))
        print("Final Velocity: " + str(self.vfinal) + "m/s" + "\n")
    def iat_fv(self):
        self.vinit = int(input("What is the Initial Velocity? "))
        self.acceleration = int(input("What is Acceleration? "))
        self.time = int(input("What is the Time? "))
        self.vfinal = self.vinit + (self.acceleration * self.time)
        print("Final Velocity: " + str(self.vfinal) + "m/s" + "\n")