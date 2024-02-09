# Problem Description
# Get two string inputs from the user and store them in text1 and text2 respectively.
# Create a new string that will contain the first four characters of the text1 string and the last four characters of the text2 string. Store the resultant string in the result variable.
# Print the new string.



text1 = input()
text2 = input()


result  = text1[ :4] + text2[-4: ]


print(result)