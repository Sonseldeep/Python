# Challenge:
# Check Whether the String is Palindrome or Not
# Easy
# Problem Description
# Create a Python program to check whether a string is a palindrome or not.

# Example
# Test Input

# For a string 'hannah'
# Expected Output

# String is Palindrome


string1 = 'racecar'

reverse = string1[::-1]

if string1 != reverse:
  print("String is not Palindrome")
else:
  print("String is  Palindrome")
  
  
# function to check palindrome string
def is_palindrome(text):

    # reverse the string using slicing and
    # store it in the rev_text variable
    rev_text = text[::-1]

    # compare the reversed string with the original string
    if text == rev_text:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')


# call the function with the string parameter
text = 'hannah'
is_palindrome(text)