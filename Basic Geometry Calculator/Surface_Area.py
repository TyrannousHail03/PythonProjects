import math


class Surface_Area:
    def __init__(self):
        print("")

    def rect_prism(self):
        rectLength = int(input("Length: "))
        rectWidth = int(input("Width: "))
        rectHeight = int(input("Height: "))
        rectSA = (2*rectLength*rectHeight)+(2*rectWidth*rectHeight)+(2*rectWidth*rectLength)
        print("Surface Area: " + str(rectSA) + "\n")

    def other_prism(self):
        ot_perim = int(input("Perimeter: "))
        ot_height = int(input("Height: "))
        ot_ba = int(input("Base Area: "))
        ot_SA = (ot_perim*ot_height)+(2*ot_ba)
        print("Surface Area: " + str(ot_SA) + "\n")

    def cylinder(self):
        cyl_radius = int(input("Radius: "))
        cyl_height = int(input("Height: "))
        cyl_SA = (2*math.pi*cyl_radius*cyl_height)+(2*math.pi*(cyl_radius**2))
        print("Surface Area: " + str(cyl_SA) + "\n")

    def pyramid(self):
        pyr_perim = int(input("Perimeter: "))
        pyr_lat = int(input("Lateral: "))
        pyr_ba = int(input("Base Area: "))
        pyr_SA = (1/2)*pyr_perim*pyr_lat+pyr_ba
        print("Surface Area: " + str(pyr_SA) + "\n")

    def cone(self):
        cone_radius = int(input("Radius: "))
        cone_lat = int(input("Lateral: "))
        cone_SA = (math.pi*cone_radius*cone_lat)+(math.pi*(cone_radius**2))
        print("Surface Area: " + str(cone_SA) + "\n")

    def sphere(self):
        sph_radius = int(input("Radius: "))
        sph_SA = 4*math.pi*(sph_radius**2)
        print("Surface Area: " + str(sph_SA) + "\n")