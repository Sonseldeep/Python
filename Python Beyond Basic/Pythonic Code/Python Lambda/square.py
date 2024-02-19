# Problem Description
# Create a lambda function that returns the square of a number passed as an argument.

# Create the lambda function and assign it to a variable named square.
# Take a float input from the user and assign it to the number variable.
# Call the lambda function with number as an argument and print the result.
# Example
# Test Input

# 2.5
# Expected Output

# 6.25


square = lambda x: x **2
number = float(input("enter any number: "))
result = square(number)
print(result)