numbers = [1,2,3,4,1,2,3,4]
print(list(set(numbers)))

# Here, list(set(numbers)) first converts numbers to a set. Converting the list to a set will remove all the duplicate items.

# Now, converting this set back to the list will create a list without duplicate items.