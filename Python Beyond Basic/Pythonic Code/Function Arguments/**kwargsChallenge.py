# Problem Description
# Create a program where a function can accept a variable number of keyword arguments.

# Create a function

# Create a function named greet() that can take a variable number of keyword arguments.
# Print the argument
# Outside the function

# Take two string inputs and assign it to variable formal and informal respectively.
# Call the greet() function like this: greet(formal = formal, informal = informal)

def greet(**text):
    # print the argument
    print(text)

formal = input("Text: ")
informal = input("Text: ")
greet(formal = formal, informal = informal)