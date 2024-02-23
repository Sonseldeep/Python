# Python Inheritance
# Easy
# Problem Description
# Starting from the Person class we created in the last example,

# Derive a class named Student from Person.
# Inside the Student class, create the __init__() method that takes self and student_id as arguments.
# Create an attribute named id and assign student_id to it, and then call the __init__() method of Person using super().
# Create another method named display_info() inside Student. Inside the method, call the display_info() method of Person using super(), and then print the id attribute.
# Outside of classes

# Create an object of Student with 12 as argument.
# Call the display_info() method using the object.
# For hints, see the code outline

# Example
# Test Input

# Sophia
# 24
# Expected Output

# name: Sophia
# age: 24
# id: 12


# create the Person class
class Person:
    def __init__(self):
        person_name = input('Enter name: ')
        person_age = int(input('Enter age: '))
        self.name = person_name
        self.age = person_age
    
    def display_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')

# derive the Student class from Person
class Student(Person):
    # create the __init__() method
    def __init__(self, student_id):
        # create id attribute and assign student_id to it
        self.id = student_id
        # call the __init__ method of Person using super()
        super().__init__()


    # create the display_info() method
    def display_info(self):
        # call display_info() of Person using super()
        super().display_info()
        # print the id attribute
        print(f'id: {self.id}')

# create an object of Student with 12 as argument
s1 = Student(12)

# call display_info() using the object
s1.display_info()