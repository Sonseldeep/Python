# Given the list of size n, create another list where elements only start with consonant letters using list comprehension.

# For example,

# If you are given a list,

# ['apple', 'banana', 'pineapple', 'mango', 'watermelon']
# The code should return,

# ['banana', 'pineapple', 'mango', 'watermelon']
# Here, the code should remove the element apple from the list as it starts with the vowel 'a'.

lst = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']
print(lst)
print('------------------------------')

newLst = [ i for i in lst if i[0] not in 'aeiouAEIOU']
print(newLst)
