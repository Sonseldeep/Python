# Problem Description
# Create a program to find the sum of the square root of two numbers using a lambda function.

# Create the lambda function and assign it to a variable named compute.
# The function should take two arguments and return the sum of the square roots of the arguments.
# Take two integer inputs and assign them to n1 and n2 respectively.
# Call the lambda function with n1 and n2 as arguments and print the result.

import math
compute = lambda x, y : (math.sqrt(x) + math.sqrt(y))

n1 = int(input())
n2 = int(input())


result = compute(n1,n2)
print(result)