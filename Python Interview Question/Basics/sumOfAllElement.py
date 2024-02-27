# Question
# Find the sum of all the elements of a list in Python. For example, if we have a list of numbers,

# numbers = [5, 6, 7, 8, 23, 51]
# Then, after adding all the elements, the sum will be 100.

# Assumption: We will assume the given list only consists of integer values.

def find_sum(num_list):
  sum = 0
  for i in num_list:
    sum += i
  return sum 

num_list = [5, 6, 7, 8, 23, 51]
result = find_sum(num_list)
print(f"sum is  {result}")


# or built in functions called sum

numbers = [5,6,7,8,23,51]

result = sum(numbers)
print(result)

