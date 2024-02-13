# the list() fn. converts an iterable ( tuples,string,dict,set) to 
# list 

#convert tuple to list:

value = (1,2,3)
change = list(value)

print(change)
print(type(change))
print(value)
print(type(value))

name = "sandeep"
changeName = list(name)
print(changeName)
print(type(changeName))

result = {1,2,3,4,4,3,2,1}
changeResult = list((result))
print(changeResult)
print(type(changeResult))