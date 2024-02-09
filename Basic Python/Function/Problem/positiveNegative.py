# Problem Description
# Write a program that checks if a user entered a positive or a negative number.

# Define a function named is_positive_or_negative() with a single parameter number.
# Inside the function, check whether number is positive or negative.
# If number is positive or zero, return True.
# Else, return False.



# define the is_positive_or_negative() function
def is_positive_or_negative(number):
    if number >= 0:
        return True
    else: 
        return False

# take integer input from the user
input_number = int(input())

# call the function
print(is_positive_or_negative(input_number))