def insertionDescending(lst):
  for i in range (1,len(lst)):
    key = lst[i]
    j = i - 1
    while j >=0 and key > lst[j]:
      lst[j+1] = lst[j]
      j = j - 1
    lst[j+1] = key
    
  return lst

lst = [1,15,6,8,2,5]
print(f"unsorted list: {lst}")
result = insertionDescending(lst)
print(f"sorted list: {result}")