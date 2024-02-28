# Challenge:
# Remove Vowels From a String
# Easy
# Problem Description
# Create a Python program to remove all the vowels from a string.

# Example
# Test Input

# For the string 'A quick brown fox jumps over the lazy dog'
# Expected Output

# qck brwn fx jmps vr th lzy dg

def remove_vowels(string):
  vowels = "aeiouAEIOU"
  new_string = ''
  for char in string:
    if char not in vowels:
      new_string += char
      
  print(new_string)
  
string = 'A quick brown fox jumps over the lazy dog'
  
remove_vowels(string)
  