animals = ('cat','dog','rat')

# del animals[1]
# print(animals)

# we cannot modify tuples items
# however, we can delete tuple itself

del animals
print(animals) # ---> animals is not defined
                # since already it has been deleteed