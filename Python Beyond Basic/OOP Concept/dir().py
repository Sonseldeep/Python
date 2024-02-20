# The dir() function lists out all the attributes and methods of the given object
number =1 
result = number.__add__(100)
print(result)
# print(dir(number))
# This means, an integer (which is an object) can access all these methods and attributes.
# At the surface, it may look like the + operator is working like how it works in mathematics, but internally it's calling the __add__() method for addition.