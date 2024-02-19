numbers = [1,2,3,4]
sqrNumber = {i: i ** 2 for i in numbers if i > 2}
print(sqrNumber)

# Here, we have added if number > 2 at the end of the dictionary comprehension. Now only the keys that are greater than 2 are included.