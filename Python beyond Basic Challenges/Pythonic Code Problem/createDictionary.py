# Create a Dictionary
# Easy
# Problem Description
# Create a program to create a dictionary using dictionary comprehension.

# Create a list with the following data items 1, 2, 3, 4, and assign it to the numbers variable.
# Create a new dictionary using comprehension where the keys are items of the list, and their corresponding values are equal to key+1.
# Print the dictionary.

numbers = [1,2,3,4]
dict = { i: i+1 for i in numbers}

print(dict)