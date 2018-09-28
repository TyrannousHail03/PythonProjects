import sys
from Area import area
from Volume import volume
from Surface_Area import Surface_Area

a = area()
v = volume()
sa = Surface_Area()


def surfaceareaMode():
    print("\nWhat polygon type would you like to find the area of?")
    surfaceAreaMode_input = input("Rectangular Prism, Other Prism, Cylinder, Pyramid, Cone, Sphere | ")
    print("You have selected the " + surfaceAreaMode_input + "mode. \n")
    if surfaceAreaMode_input.lower() == "rectangular prism" or surfaceAreaMode_input.lower() == "rp":
        sa.rect_prism()
    elif surfaceAreaMode_input.lower() == "other prism" or surfaceAreaMode_input.lower() == "ot":
        sa.other_prism()
    elif surfaceAreaMode_input.lower() == "cylinder" or surfaceAreaMode_input.lower() == "cy":
        sa.cylinder()
    elif surfaceAreaMode_input.lower() == "pyramid" or surfaceAreaMode_input.lower() == "py":
        sa.pyramid()
    elif surfaceAreaMode_input.lower() == "cone" or surfaceAreaMode_input.lower() == "co":
        sa.cone()
    elif surfaceAreaMode_input.lower() == "sphere" or surfaceAreaMode_input.lower() == "sp":
        sa.sphere()
    elif surfaceAreaMode_input.lower() == "exit" or surfaceAreaMode_input.lower() == "ex":
        sys.exit()
    else:
        print("Sorry, that was not understood, please try again. \n")
        surfaceareaMode()
    moreQuestions()


def volumeMode():
    print("\nWhat polygon type would you like to find the volume of?")
    volumeMode_input = input("Rectangular Prism, Other Prism, Cylinder, Pyramid, Cone, Sphere | ")
    print("\nYou have selected the " + volumeMode_input + "mode. \n")
    if volumeMode_input.lower() == "rectangular prism" or volumeMode_input.lower() == "rp":
        v.rect_prism()
    elif volumeMode_input.lower() == "other prism" or volumeMode_input.lower() == "ot":
        v.other_prisms()
    elif volumeMode_input.lower() == "cylinder" or volumeMode_input.lower() == "cy":
        v.cylinder()
    elif volumeMode_input.lower() == "pyramid" or volumeMode_input.lower() == "py":
        v.pyramid()
    elif volumeMode_input.lower() == "cone" or volumeMode_input.lower() == "co":
        v.cone()
    elif volumeMode_input.lower() == "sphere" or volumeMode_input.lower() == "sp":
        v.sphere()
    elif volumeMode_input.lower() == "exit" or volumeMode_input.lower() == "ex":
        sys.exit()
    else:
        print("Sorry, that was not understood, please try again. \n")
        volumeMode()
    moreQuestions()

def areaMode():
    print("\nWhat polygon type would you like to find the area of?")
    areaMode_input = input("Parallelogram, Triangle, Trapezoid, Circle, Rhombus | ")
    print("\nYou have selected the " + areaMode_input + "mode. \n")
    if areaMode_input.lower() == "parallelogram" or areaMode_input.lower() == "p":
        a.parallelogram()
    elif areaMode_input.lower() == "triangle" or areaMode_input.lower() == "tri":
        a.triangle()
    elif areaMode_input.lower() == "trapezoid" or areaMode_input.lower() == "tra":
        a.trapezoid()
    elif areaMode_input.lower() == "circle" or areaMode_input.lower() == "cir":
        a.circle()
    elif areaMode_input.lower() == "rhombus" or areaMode_input.lower() == "rho":
        a.rhombus()
    elif areaMode_input.lower() == "exit" or areaMode_input.lower() == "ex":
        sys.exit()
    else:
        print("Sorry, that was not understood, please try again. \n")
        areaMode()
    moreQuestions()

def moreQuestions():
    print("Would you like to solve more questions?")
    moreQuestions_input = input("Y/N: ")
    if moreQuestions_input.lower() == "y" or moreQuestions_input.lower() == "yes":
        mode()
    elif moreQuestions_input.lower() == "n" or moreQuestions_input.lower() == "no":
        sys.exit()
    else:
        print("Sorry, that was not understood, please try again. \n")
        moreQuestions()

def mode():
    print("\nPlease choose a mode:")
    mode_input = input("Area, Volume, Surface Area |  ")
    if mode_input.lower() == "area" or mode_input.lower() == "a":
        areaMode()
    elif mode_input.lower() == "volume" or mode_input.lower() == "v":
        volumeMode()
    elif mode_input.lower() == "surface area" or mode_input.lower() == "sa" or mode_input.lower() == "surfacearea":
        surfaceareaMode()
    elif mode_input.lower() == "exit" or mode_input.lower() == "ex":
        sys.exit()
    else:
        print("Sorry, that was not understood, please try again. \n")


def start():
    print("Welcome to TyrannousHail03's Basic Geometry Calculator \n")
    start_input = input("Would you like to continue?")
    if start_input.lower() == "yes" or start_input.lower() == "y":
        mode()
    elif start_input.lower() == "no" or start_input.lower() == "n":
        sys.exit()
    else:
        print("Sorry that was not understood. \n")
        start()


start()
