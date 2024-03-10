# Challenge:
# Give Discount
# Easy
# Problem Description
# Create a Python program that prints the discounted price.

# Example
# Test Input

# for a full price of 100 and a discount of 10%
# Expected Output

# 90.0





# define a function that calculates the amount after discount
def discounter(total, discount):

    # from the total amount and discount percentage,
    # calculate the amount after discount
    actual_discount = 0.1 * total

    # calculate the amount after discount
    final_amount = total - actual_discount

    # print the final amount
    print(final_amount)


# call the function
discounter(100, 10)