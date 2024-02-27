# Challenge:
# Cube of a Number Using Lambda
# Easy
# Problem Description
# Create a program to find the cube of a number using a lambda function.

# Create the lambda function and assign it to a variable named num_cube.
# Take one integer input and assign it to number.
# Call the lambda function with number as argument and print the result.


get_cube = lambda x: x ** 3
number = int(input('enter the number: '))

result = get_cube(number)
print(result)