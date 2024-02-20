# The id of an object is always unique and constant for this object during its lifetime.

# number = 5
# print(id(number))

# number2 = 10
# print(id(number2))

num1 = 5
num2 = num1
print(id(num1))
print(id(num2))

# Here, we can see that the id of number1 and number2 is the same. It means these two variables are referring to the same object. Python does this for memory optimization.