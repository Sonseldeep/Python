# Challenge:
# Access Method of the Base Class
# Easy
# Problem Description
# Create a program to call the method of the base class using an object of the derived class.

# Create classes

# Create a base class named Animal. Inside the class, create a method named eat() that prints 'I can eat food'.
# Create a Dog class that inherits the Animal class. Inside the class, create a method named bark() that prints 'I can bark'.
# Outside of classes

# Create an object of the Dog class.
# Call the eat() method using this object.
# Example
# Expected Output

# I can eat food



# create the Animal class
class Animal:
    def eat(self):
        print('I can eat food')

# create the Dog class
class Dog(Animal):
    def bark(self):
        print('I can bark')

# create an object of Dog
d1 = Dog()

# call the eat() method using the object
d1.eat()