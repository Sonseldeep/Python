class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def print_person_attributes(self, person):
        print(self.name)    # Ana
        print(self.age)     # 21
        print(person.name)    # Sara
        print(person.age)    # 20

# create an object
person1 = Person('Ana', 21)

# create another object
person2 = Person('Sara', 20)

# calling print_persons_attributes() using person1 object
# person2 is used as an argument
person1.print_person_attributes(person2)