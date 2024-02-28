# Challenge:
# Number of Vowels and Consonants
# Easy
# Problem Description
# Create a Python program to count the number of vowels and consonants in a string.

# Example
# Test Input

# For the string 'A quick brown fox jumps over the lazy dog'
# Expected Output

# Vowels: 11
# Consonants: 22

def count(string):
  vowels = 'aeiouAEIOU'
  vowels_count = 0
  consonant_count = 0
  
  for char in string:
    
    if char in vowels:
      vowels_count += 1
      
    elif char  ==' ':
      continue
    
    else:
      consonant_count += 1
      
  print(f"vowels count is {vowels_count} and consonants count is {consonant_count}")
  
string = 'A quick brown fox jumps over the lazy dog'
count(string)
  
 