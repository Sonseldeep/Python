# Suppose we have to create a list of the first five powers of 2. For this, we would normally use a for loop and append each item to the end of the list

numbers = []
for i in range (1,6):
  numbers.append(2 ** i)
  
print(numbers)
# There is a concise way to accomplish this same task using list comprehension.