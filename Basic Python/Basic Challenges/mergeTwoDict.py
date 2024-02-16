# Program Description
# Write a program to merge two dictionaries.

# Create a dictionary A with items {12: 'Kathmandu', 11: 'London', 3: 'Sydney'}.
# Create another dictionary B with items {10: 'New York', 2: 'Delhi'}.
# Merge these two dictionaries using update() and print it.



# create two dictionaries
A = {12: 'Kathmandu', 11: 'London', 3: 'Sydney'}
B = {10: 'New York', 2: 'Delhi'}

# merge the two dictionaries using update()
A.update(B)

# print the merged dictionary
print(A)