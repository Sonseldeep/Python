# Program Description
# Write a program to replace 'yt' in 'Python' with the string entered by the user.

# Create a string named language with the value "Python".
# Take string as an input for ch variable.
# Use the replace() method to replace "yt" with user-entered string stored in ch.
# Print the new string.
# Hint: Use the string replace() method. This method takes two arguments.

# oldValue - a substring we want to replace
# newValue - a substring that replaces the oldValue


language = 'Python'

# take string as input for ch variable
ch = input()

# use the replace() method to replace 'yt'
new_string = language.replace("yt",ch)

print(new_string)
