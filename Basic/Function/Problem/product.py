# Problem Description
# Write a program to find the product of two numbers.

# Step 1

# Define a function named get_product() that accepts two parameters: number1 and number2.
# Inside the function, multiply number1 and number2 and return the result.
# Step 2

# Outside of the function:

# Get two integer inputs from the user and store them in n1 and n2.
# Call the get_product() function with arguments n1 and n2 respectively and store the return value in the total variable.
# Print the total variable.

# create the get_product() function
def get_product(number1, number2):
    result = number1 * number2
    return result

# get integer inputs from the user
n1 = int(input())
n2 = int(input())

# call the function with n1 and n2 as arguments
# and print the return value
print(get_product(n1,n2))