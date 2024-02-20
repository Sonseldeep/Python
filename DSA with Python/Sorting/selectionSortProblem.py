# Can you write the selection sort program on your own?

# Create a function named selection_sort() that takes a list as its argument.
# Sort the list in ascending order within the function and return the sorted list.
# Print the sorted list outside the function.

def selectionSort(lst):
  for i in range(0, len(lst)):
    min = i
    for j in range(i+1,len(lst)):
      if lst[j]<lst[min]:
        min = j
    lst[i],lst[min] = lst[min],lst[i]
  return lst

lst = [9,8,0,10,-7,19]
result = selectionSort(lst)
print(result)