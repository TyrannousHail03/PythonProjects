import math


class volume:
    def __init__(self):
        print("")

    def rect_prism(self):
        rectPrism_length = int(input("Length: "))
        rectPrism_width = int(input("Width: "))
        rectPrism_height = int(int("Height: "))
        rectPrism_volume = rectPrism_length*rectPrism_height*rectPrism_width
        print("Volume: " + str(rectPrism_volume) + "\n")

    def other_prisms(self):
        prisms_base = int(input("Base Area: "))
        prisms_height = int(input("Height: "))
        prisms_volume = prisms_base*prisms_height
        print("Volume: " + str(prisms_volume) + "\n")

    def cylinder(self):
        cyl_radius = int(input("Radius: "))
        cyl_height = int(input("Height: "))
        cyl_volume = math.pi*(cyl_radius**2)*cyl_height
        print("Volume: " + str(cyl_volume) + "\n")

    def pyramid(self):
        pyr_base = int(input("Base Area:"))
        pyr_height = int(input("Height: "))
        pyr_volume = (1/3)*pyr_base*pyr_height
        print("Volume: " + str(pyr_volume) + "\n")

    def cone(self):
        cone_radius = int(input("Radius: "))
        cone_height = int(input("Height: "))
        cone_volume = (1/3)*math.pi*(cone_radius**2)*cone_height
        print("Volume: " + str(cone_volume) + "\n")

    def sphere(self):
        sph_radius = int(input("Radius: "))
        sph_volume = (4/3)*math.pi*(sph_radius**3)
        print("Volume: " + str(sph_volume) + "\n")

    if __name__ == '__main__':
        print("")
