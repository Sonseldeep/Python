# The set() function converts an iterable 
# (list, tuple, string, or dict) to a set. 

# convert list to set
result = set([1, 2, 3])
print(result) # {1, 2, 3}
 
# convert string to set
result = set("abca")
print(result) # {'a', 'b', 'c'}
 
# convert tuple to set
result = set((1, 2, 3, 2, 3))
print(result) # {1, 2, 3}
 
# convert dictionary to set
result = set({2: 4, 10: 20}) # {2, 10}
print(result)
