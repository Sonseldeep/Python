def selection_sort(lst):
    
    for i in range(len(lst)):
    
        min_index = i
    
        for j in range(i + 1, len(lst)):

            # to find the largest element, change < to > 
            if lst[j] > lst[min_index]:
                min_index = j
    
        lst[min_index], lst[i] = lst[i], lst[min_index]
    
    return lst
lst = [9,0,8,10,2]
result = selection_sort(lst)
print(result)