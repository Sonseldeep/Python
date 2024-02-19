# Lambda Function
# Easy
# Problem Description
# Create a lambda function that takes two arguments and returns their sum.

# Create the lambda function and assign it to a variable named add.
# Take two integer inputs and assign them to n1 and n2 respectively.
# Call the lambda function with n1 and n2 as arguments and print the result.



# create the function
add = lambda n1, n2 : n1 + n2

# take two integer inputs
n1 = int(input())
n2 = int(input())

# call the function and print the result
result = add(n1,n2)
print(result)