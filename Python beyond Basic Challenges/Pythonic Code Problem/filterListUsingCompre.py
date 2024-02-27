# Filter List Using Comprehension
# Easy
# Problem Description
# Create a program to create a list of odd numbers from a list of numbers using list comprehension.

# Create a list with the following data items 12, 17, 28, 19, 11, and assign it to the numbers variable.
# Create a new list and only print 17, 19, 11 (odd numbers) using list comprehension.
# Print newly created list

numbers = [12,17,28,19,11]
oddNumbers = [ i for i in numbers if i %2 !=0]
print(oddNumbers)