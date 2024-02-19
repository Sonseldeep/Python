# Problem Description
# Create a dictionary using dictionary comprehension.

# Take an integer input from the user and store it in variable n.
# Create a dictionary with keys from 1 to n. The value of the key must be 10 times the value of the key.
# Also, add a condition to the dictionary comprehension so that the key must be greater than or equal to 3.
# Print the dictionary.
# We will assume that the user will always enter a positive integer.

# Example
# Test Input

# 4
# Expected Output

# {3: 30, 4: 40}

n = int(input("enter the upper bound: "))

# create the dictionary using comprehension
numbers = {
    i: 10*i 
    for i in range ( 1, n+1)
    if i >= 3
}

print(numbers)
