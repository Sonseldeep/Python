# Challenge:
# Use of super()
# Medium
# Problem Description
# Create a program that calls a method of the base class from inside a method of a derived class using the super() function.

# Create classes

# Create a base class named Animal. Inside the class, create a method named eat() that prints 'I can eat food'
# Inherit a class named Dog from the Animal class.
# Inside the Dog class, create a method named bark() that prints 'I can bark' and a method named eat() that calls the eat() method of the Animal class using super().
# Outside of classes

# Create an object of the Dog class and call the eat() method using the object.
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
        print("I can bark")
        super.eat()


# create an object of the Dog class
d = Dog()

# call the eat() method using the object
d.eat()