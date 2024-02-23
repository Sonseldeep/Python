# Problem Description
# Write a program that sorts only the first n elements of a list using the insertion sort algorithm.

# Create the function perform_partial_sort() to sort the first n elements in ascending order.
# This function takes two arguments: a list and the number of elements to sort.
# Within the function, use insertion sort to arrange the elements.
# Return the sorted portion and print it.
# For example, if the number of elements to sort is 3, only first three elements are sorted and printed.

# Example
# Test Input

# 5 6 2 9 1 3 
# 3

def partialInsertion(lst,n):
  for i in range (1       ,n):
    key = lst[i]
    j = i - 1
    while j >= 0  and key < lst[j]:
      lst[j+1] = lst[j]
      j = j - 1
    lst[j+1 ] = key
  return lst[:n]


n = int(input("enter number: "))

lst = [1,15,6,8,2,5]
print(f"unsorted list: {lst}")
result = partialInsertion(lst,n)
(lst)
print(f"sorted list: {result}")

