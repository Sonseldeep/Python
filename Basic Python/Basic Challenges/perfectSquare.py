# Program Description
# Write a program to check if a number is a perfect square or not.

# Import math module.
# Get an integer input and store it in the number variable.
# Find the square root of the number using sqrt() function and assign it to square_root variable.
# Use the % operator with 1 to get the remainder of the calculated square root and assign it to check_remainder.
# If the remainder is equal to 0, print Perfect Square.
# Else print Not a Perfect Square.

# import math module
import math

number = int(input())

# use sqrt() to find the square root of the number
square_root = math.sqrt(number)

# get remainder of the square root by using % with 1 
check_remainder = square_root % 1

# if the remainder is equal to 0, print "Perfect Square" Else print "Not a Perfect Square"
if check_remainder !=0:
    print("Not a Perfect Square")
else:
    print("Perfect Square")