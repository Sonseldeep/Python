class Animal:
  def eat(self):
    print("I can eat")
    
class Dog(Animal):
  def bark(self):
    print("I can bark")
    
dog1 = Dog()
dog1.bark()
dog1.eat()