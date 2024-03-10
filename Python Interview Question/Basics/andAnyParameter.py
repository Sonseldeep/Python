# Challenge:
# Add Any Number of Parameters
# Easy
# Problem Description
# Create a Python program to add any number of parameters in a function.

# Example
# Test Input

# for function arguments 1, 2, 3, 4, 5
# Expected Output

# 15






# define a function that can add any number of arguments
def adder(*args):

    # initialize the sum variable
    sum = 0

    # loop through the arguments and add them to the sum variable
    for i in args:
        sum +=i

    # print the sum
    print(sum)


# call the function
adder(1, 2, 3, 4, 5)