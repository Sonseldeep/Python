# You are given a non-empty list. How do you convert that list into a set?

# If you remember, Set does not allow duplicate elements (unlike List). So, while converting a list to a set, all the duplicate elements which are in the list are deleted.

# For example

# Let's take a list of countries,

# countries = ['USA', 'Japan', 'Nepal', 'Japan']
# If we convert the countries to a set, the duplicate element 'Japan' will be removed.

# So the obtained Set will be {'Nepal', 'Japan', 'USA'}.


countries = ['USA', 'Japan', 'Nepal', 'Japan']

print(set(countries))