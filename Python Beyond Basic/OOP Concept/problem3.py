
# Challenge:
# Classes and Objects
# Easy
# Problem Description
# Create a class

# Create a class named Triangle.
# Create the __init__() method that takes four arguments self, a, b and c. The a, b and c arguments represent sides of a triangle.
# Inside the __init__() method, create three attributes s1, s2 and s3 and assign values a, b and c to the attributes.
# Create a method named get_perimeter() to compute perimeter and return it. If you don't know, the perimeter is equal to the sum of the sides.
# Outside of the class

# Take three integer inputs from the user to represent the sides of a triangle.
# Create an object of the Triangle class using the given inputs.
# Call the get_perimeter() method using the object and print the perimeter.


class Triangle:
    
    # initialize attributes
    def __init__(self, a, b, c):
        self.s1 = a
        self.s2 = b
        self.s3 = c
    
    # method to compute perimeter
    # Hint: you don't need to pass additional arguments to solve this problem
    def get_perimeter(self):
        perimeter = self.s1 + self.s2 + self.s3
        return perimeter  

# take three integer inputs
a = int(input())
b = int(input())
c = int(input())

# create an object of Triangle
t1 = Triangle(a, b, c)

# call the get_perimeter() method using the object
result = t1.get_perimeter()

print(result)