# Program Description
# Write a program to check if two strings are equal or not.

# Take two string inputs and assign them to str1 and str2 respectively.
# Convert both strings to lowercase and check if they are equal using ==
# If two strings are equal print Equal else print Not Equal.


# take string input for str1 and str2
str1 = input()
str2 = input()

# convert str1 and str2 to lowercase and compare them
if str1.lower() == str2.lower():
    print("Equal")
else:
    print("Not Equal")