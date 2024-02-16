
string1 = (input())


character1 = (input())

count = 0

# use for loop to iterate through string1
for i in string1:
    # check if character is present in the string or not
    if i == character1:
        count = count + 1
print(count)