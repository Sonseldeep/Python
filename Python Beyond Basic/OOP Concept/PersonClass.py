class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
  def displayInfo(self):
    print(f"name: {self.name}, age: {self.age}")
    
  
p1 = Person("Sandeep",18)
p1.displayInfo()

    