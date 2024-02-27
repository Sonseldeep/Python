# Challenge:
# Largest &amp; Smallest Element
# Easy
# Problem Description
# Create a Python program to find the sum of the largest and the smallest elements in a list.

# Example
# Test Input

# For a list [5, 6, 3, 8, 9]
# Expected Output

# 12




def calc_sum(numbers):
  minValue = min(numbers)
  maxValue = max(numbers)
  
  total = minValue + maxValue
  return total

number = [5,6,3,8,9]
result = calc_sum(number)
print(result)

# or we sort the list and return sum of 1st and last index element

number = [5,6,3,8,9]
number.sort()
sum = number[0] + number[-1]
print(sum)