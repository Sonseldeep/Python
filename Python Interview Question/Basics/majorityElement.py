def find_majority_element(numList):
  for i in numList:
    count = numList.count(i)
    if count > len(numList) // 2 :
      return i
    
    
numbers = [1,7,8,7,7,7]
result = find_majority_element(numbers)
print(f"majority element is {result}")


# Thought Process

# As mentioned before, the majority element occurs more than n / 2 times in a list of size n.

# So, if we want to find the majority element, we first need to find the number of times each element occurs in the list.

# Python provides a built-in method count() to count the number of occurrences of the specified element.

# list.count(element)
# Now, let's see how we can solve this problem.

# Loop through each element of the list using a for loop.
# In each iteration of the loop, we will use the count() function to count the number of occurrences of every element.
# We will then use an if...else statement to check if the value of count() for each element is greater than n // 2 (where n is the size of our list).
# If the condition is true, we will return the element as the majority element.