# Problem Description
# Create a function that has arguments with default values.

# Create a function named func() that takes two arguments n1 and n2 respectively.
# Set default values of n1 and n2 to 10 and 100 respectively.
# Inside the function, print n1 and n2.
# Outside the function

# Take integer input and assign it to n.
# Call the function so that the first argument takes the value of n, and the second argument takes the default value.


def func(n1 = 10,n2=100):
    print(n1)
    print(n2)


# take integer input
n = int(input())

# call the function
result = func(n)
