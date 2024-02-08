# Problem Description
# Write a program to compute the factorial of a number.

# The factorial of a positive integer n is equal to:

# factorial = 1 * 2 * 3 * ... * n
# Step 1

# Define a function named compute_factorial() that takes a single parameter n.
# Inside the function, compute the factorial.
# Return the factorial.
# Step 2

# Outside of the function:

# Get an integer input from the user and store it in the number variable.
# Call compute_factorial() with number as an argument, and assign the returned value to the total variable.
# Print the total variable.
# We will assume that the user will enter a non-negative integer.

def compute_factorial(number):
  if number<0:
    return " does not exist for negative numbers"
  result = 1
  for i in range(1,number+1):
    result *= i
  return result

number = int(input("enter number"))
total = compute_factorial(number)
print("The factorial of",number,"is",total)