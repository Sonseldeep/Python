# Problem Description
# The easiest way to find the number of items a list has is by using the built-in len() function.

# Can you find the length of a list without using this function?

# Suppose we have a list like this: [10, 20, 30, 40]
# Your task is to find the length of this list programmatically.
# For more hints, see the code outline

numbers = [10, 20, 30, 40]

length = 0


for i in numbers:
    length += 1


print(length)