# Question
# Given a list of size n, convert it to a string.

# For example,

# If you are given a list,

# ['Hello', 'world', 'from', 'Python']
# display this as,

# 'Hello world from Python'

lst = ['Hello', 'world', 'from', 'Python']
newList = ' '.join(lst)
print(newList)

# Thought Process
# Python provides an inbuilt method to convert a given list to a string.

# In Python, there is a string method join() that is used to join the list elements to the string. For example,

# words = ['Hello', 'world', 'from', 'Python']

# sentence = ' '.join(words)
# Here, ' ' before join() specifies the word separator. This means each element of the list is separated by a space.

# And the iterable (list) is used as the parameter to the method.