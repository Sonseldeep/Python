def count_swap(list):
  count = 0
  for i in range (len(lst)):
    min =i
    for j in range (i+1,len(lst)):
      if lst[j]<lst[min]:
        min = j
    if lst[i] != lst[min]:
      lst[i],lst[min] = lst[min],lst[i]
      count += 1
    
  
  return count

lst = list(map(int, input().split()))

result = count_swap(lst)

print(result)
