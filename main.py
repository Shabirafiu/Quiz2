"""
Define a function named which_shape.

The function will ask a number from the user.

It will decide the name of the shape according to that number, and return that name.

Sides & Shapes:

3 - Triangle
4 - Rectangle
5 - Pentagon
6 - Hexagon
7 and more - Polygon

"""


def which_shape():
    no_of_sides = int(input("Please enter a number: "))

    shape_name = " "

    if no_of_sides == 3:
        shape_name = "Triangle"
    elif no_of_sides == 4:
        shape_name = "Rectangle"
    elif no_of_sides == 5:
        shape_name = "Pentagon"
    elif no_of_sides == 6:
        shape_name = "Hexagon"
    else:
        shape_name = "Polygon"

    return shape_name

shape = which_shape()

print(shape)


