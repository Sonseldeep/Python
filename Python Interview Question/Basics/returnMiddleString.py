# Challenge:
# Print the Middle Letter
# Easy
# Problem Description
# Create a Python program to print the middle letter of a string.

# Example
# Test Input

# for the string 'hello'
# Expected Output

# l

def get_middle(word):
    middle = int(len(word) / 2)
    if len(word) % 2 == 0: 
        return ''
    else: # If the length is odd
        return word[middle] # Return the middle character

# Test the function
print(get_middle("hello")) # Expected output: l
