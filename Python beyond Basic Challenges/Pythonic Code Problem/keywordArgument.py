# Challenge:
# Keyword Arguments
# Medium
# Problem Description
# Write a program to create a function that takes two arguments and call the function with keyword arguments.

# Create a function named print_numbers() that takes two arguments: arg1 and arg2.
# Inside the function, print arg1, then arg2 in different lines.
# Outside the function

# Take two integer inputs and assign them to n1 and n2.
# Call the function using keyword arguments such that arg1 takes the value of n1 and arg2 takes the value of n2. The order of arguments shouldn't matter.
# Example
# Test Input

# 2
# 4
# Expected Output

# 2
# 4


def print_numbers(arg1, arg2):
  print(f"{arg1}\n{arg2}\n")
  
n1 = int(input("input n1: "))
n2 = int(input("input n2: "))

print_numbers(arg2 = n2, arg1 = n1 )