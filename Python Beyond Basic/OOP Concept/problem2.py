# Problem Description
# Create a class

# Create a class named Person.
# Inside this class, create the __init__() method that takes three arguments: self and name and age.
# Inside the __init__() method, create two attributes named current_name and current_age. Then, assign the name argument to the current_name attribute, and the age argument to the current_age attribute.
# Outside of the class

# Create an object named person1 of the Person class. While creating this object, use 'Phil' as the first argument and 19 as the second argument.
# Print the current_name attribute of the person1 object.
# Print the current_age attribute of the person1 object.



class Person:
    # create the __init__(self, name) method
    def __init__(self, name, age):
        # create the current_name attribute and assign name to it
        self.current_name = name
        
        # create the current_age attribute and assign age to it
        self.current_age = age
        

# create the object with 'Phil' and 19 as argument
person1 = Person('Phil',19)

print(person1.current_name)
print(person1.current_age)
