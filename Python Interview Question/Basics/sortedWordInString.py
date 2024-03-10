# Challenge:
# Sorted Words in a String
# Easy
# Problem Description
# Create a Python program to sort the words in a string alphabetically.

# Example
# Test Input

# for the string 'python is easy'
# Expected Output

# easy
# is
# python




sentence = 'python is easy'

# split the string into words
# by default, python splits by space
# and returns a list of splitted elements
words = sentence.split()

# sort the list of words
# sort() is a built-in function and
# it sorts the list in ascending order
words.sort()
# loop through each word and print it
for i in words:
    print(f"{i}")