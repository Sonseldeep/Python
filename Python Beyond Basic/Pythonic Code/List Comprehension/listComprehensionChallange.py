# Problem Description
# Create a list using list comprehension and print the list.

# Take an integer input from the user and store it in variable n.
# Create a list of numbers from 1 to n using list comprehension.
# Print the list.
# Note: We will assume that the user will enter a positive integer.

# Example
# Test Input

# 4
# Expected Output

# [1, 2, 3, 4]
n = int(input("enter the number range: "))
numbers = [ i for i in range (1, n+1)]
print(numbers)