# Write a program to count the length of the string without using the len() function.

# The length of a string is the number of characters in the string. In Python, the len() function gives the length of any string.

# But you need to write the code without using the len() function.

# For example,

# If the string is

# 'Python'
# Then the function needs to print 6

def count(string):
  count = 0
  for char in string:
    count += 1
    
  print(f"length of {string} is {count}")
  
string= 'python'
count(string)