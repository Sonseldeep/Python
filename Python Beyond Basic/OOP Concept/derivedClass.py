class Animal:
  def eat(self):
    print('can eat')
    
class Dog(Animal):
  def bark(self):
    print('can bark')

class Cat(Animal):
  def meow(self):
    print('mewo meow')
    
dog1 = Dog()
dog1.bark()
dog1.eat()


cat1 = Cat()
cat1.eat()
cat1.meow()