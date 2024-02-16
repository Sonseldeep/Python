# Program Description
# Write a program that uses a loop to take 3 key-value inputs from the user and create a dictionary using these keys and values.

# Create an empty dictionary named my_dict.
# Use for loop to iterate from 1 to 3, including 3.
# Inside the loop, take inputs for key and value and store them in my_dict.
# Print the updated my_dict.

# Step  1: Initialize an empty dictionary
my_dict = {}

# Step  2: Use a for loop to iterate from  1 to  3
for i in range(1,  4):
    # Step  3: Prompt the user to enter a key and a value
    key = input("Enter key #{}: ".format(i))
    value = input("Enter value for key '{}': ".format(key))
    
    # Step  4: Store the key-value pair in my_dict
    my_dict[key] = value

# Step  5: Print the updated my_dict
print( my_dict)
