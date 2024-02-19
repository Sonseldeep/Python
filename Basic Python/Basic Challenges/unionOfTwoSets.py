# Program Description
# Write a program to get the union of two sets.

# Create a set named developers with elements "Mark", "George", "Ben".
# Create another set named designers with elements "Andy", "Jared", "Ben".
# Use the union() function to return a new set with distinct elements from all the sets.
# Print the new set that contains all elements of developers and designers set.


# create two sets developer and designer with required elements 
developers = {'Mark','George','Ben'}
designers = {'Andy','Jared','Ben'}

# use union() to get both set of developers and designers
union = developers.union(designers)
# union = developers | designers 
print(union)