def bubble_sort(data):
 
    for i in range(len(data) - 1):
        swapped = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
        
    return data

data_list = [4, 6, 99, 45, 0]

sorted_list = bubble_sort(data_list)
print(sorted_list)

      