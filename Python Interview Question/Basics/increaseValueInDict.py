# Increase Values in a Dictionary
# Easy
# Problem Description
# Create a Python program to increment the values of a dictionary by 1.

# Example
# Test Input

# for a dictionary {'Cody': 50, 'Jack': 57, 'Seth': 59, 'Roman': 67}
# Expected Output

# {'Cody': 51, 'Jack': 58, 'Seth': 60, 'Roman': 68}






# replace ___ with your code

# function that increments every player's score by 1
def incrementer(dictionary):

    # for loop that iterates through the dictionary
    # and increments the score by 1
    for key in dictionary:
        dictionary[key] += 1

    # print the updated dictionary
    print(dictionary)


# define the dictionary
player_scores = {
    'Cody': 50,
    'Jack': 57,
    'Seth': 59,
    'Roman': 67,
}

# call the function
incrementer(player_scores)