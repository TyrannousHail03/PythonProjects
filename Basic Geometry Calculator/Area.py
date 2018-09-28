import math


class area:
    def parallelogram(self):
        # par stands for parallelogram
        par_base = int(input("Base: "))
        par_height = int(input("Height: "))
        par_area = par_base*par_height
        print("Area:  " + str(par_area) + "\n")

    def triangle(self):
        # tri stands for triangle
        tri_base = int(input("Base: "))
        tri_height = int(input("Height: "))
        tri_area = (1/2)*tri_base*tri_height
        print("Area: " + str(tri_area) + "\n")

    def trapezoid(self):
        # tra stands for trapezoid
        tra_height = int(input("Height: "))
        tra_base1 = int(input("Base #1: "))
        tra_base2 = int(input("Base #2: "))
        tra_area = ((1/2)*tra_height)*(tra_base1*tra_base2)
        print("Area: " + str(tra_area) + "\n")

    def circle(self):
        # cir stands for circle
        cir_radius = int(input("Radius: "))
        cir_area = math.pi*(cir_radius**2)
        print("Area: " + cir_area + "\n")

    def rhombus(self):
        # rho stands for rhombus
        rho_diagonal1 = int(input("Diagonal #1: "))
        rho_diagonal2 = int(input("Diagonal #2: "))
        rho_area = (1/2)*rho_diagonal1*rho_diagonal2
        print("Area: " + str(rho_area) + "\n")

    def kite(self):
        kite_diagonal1 = int(input("Diagonal #1: "))
        kite_diagonal2 = int(input("Diagnoal #2: "))
        kite_area = (1/2)*kite_diagonal1*kite_diagonal2
        print("Area: " + str(kite_area) + "\n")
