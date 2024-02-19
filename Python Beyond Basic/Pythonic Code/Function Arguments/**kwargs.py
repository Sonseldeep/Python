# It's also possible to pass a variable number of keyword arguments in Python. To accept these arguments in the function definition, we use ** before the argument name

def print_info( **person):
  print(person)
  
print_info()
print_info(name = "Sandeep")
print_info(age = 21)


# Here, **person in the function definition means that person can accept any number of keyword arguments, and the person argument will always be a dictionary.