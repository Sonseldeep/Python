# Challenge:
# Before and After
# Easy
# Problem Description
# Create a Python program to print the numbers that come immediately before and after a given number.

# Example
# Test Input

# for an integer 5
# Expected Output

# (4, 5, 6)




# define a function to find the before and after of a given number
def before_and_after(n):

    # decrement the number by 1 to find the before number
    before = n-1

    # increment the number by 1 to find the after number
    after = n+1

    # return the tuple of before, n and after
    return (before,n,after)


# call the function
result = before_and_after(5)
print(result)


