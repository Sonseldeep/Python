# Problem Description
# Create a function named print_items() that can take any number of arguments.

# Inside the function,

# use a for loop to print all the arguments passed during the function call
# Outside the function

# take two string inputs and store them in variables text1 and text2 respectively
# call the print_item() function with text1 as an argument
# call the print_item() function with text1 and text2 as arguments


def print_items(*text):
    # use a for loop to print individual items of the argument
    for i in text:
        print(i)

# take two string inputs
text1 = input("enter text: " )
text2 = input("enter text: " )

# call print_items with text1 as argument
print_items(text1)

# call print_items with text1 and text2 as arguments
print_items(text1,text2)