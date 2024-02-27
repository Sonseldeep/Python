
# Challenge:
# Addition of Coordinates
# Medium
# Problem Description
# Create a program to find the sum of two coordinates by creating objects.

# Create a class

# Create a class named Coordinate with attributes x and y.
# Use the __init__() method with two arguments to initialize these attributes.
# The class must also have a method named add_coordinates() that adds x and y attributes of two objects, then creates a new Coordinate object with these values, and returns the new Coordinate object.
# Outside the class

# Create two coordinates (objects of the Coordinate class) named c1 and c2.
# The x and y attributes of c1 should be 5 and 6 respectively.
# The x and y attributes of c2 should be 7 and 9 respectively.
# Call add_coordinates() using the c1 object with c2 as an argument, and store the result to the c3 variable.
# Print the x attribute of c3.
# Print the y attribute of c3.
# For hints, see the code outline
# create the Coordinate class

class Coordinate:

    # initialize x and y attributes inside __init__()
    def __init__(self,x,y):
        self.x = x
        self.y = y


    # define the add_coordinates() method
    def add_coordinates(self, result):
        xPart = self.x + result.x
        yPart = self.y + result.y
       

# create objects c1 and c2
c1 = Coordinate(5,6)
c2 = Coordinate(7,9)

# call the add_coordinates() method
c3 = Coordinate(c1.x + c2.x, c1.y + c2.y)


# print attributes of the c3 object
print(c3.x)
print(c3.y)