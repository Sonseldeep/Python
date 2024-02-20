def OptimizedBubbleSort(lst):
  swap = False
  for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
      if lst[j]>lst[j+1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]
        swap = True
    if not swap:
      break
  return lst


lst = list(map(int, input("input list of number: ").split()))
sorted_list = OptimizedBubbleSort(lst)
print(sorted_list)