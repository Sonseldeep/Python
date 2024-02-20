
def bubble_sort(lst):

    
  for i in range (len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j]<lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swap = True
  return lst


  



# take integer inputs and convert it to a list    
data_list = list(map(int, input().split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)