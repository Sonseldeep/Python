# The tuple() function converts 
# iterable (list, string, dict, or set) to a tuple

result = (1,2,3)
changeResultType = tuple(result)
print(changeResultType)

name = tuple("Sandeep")
print(name)

dict= {
  'name': 'Ram',
  'age' : 20,
}

changeDict = tuple(dict)
print(changeDict)