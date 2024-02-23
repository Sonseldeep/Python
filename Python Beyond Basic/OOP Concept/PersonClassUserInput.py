class Person:
  def __init__(self):
    FullName = input("Name: ")
    Age = int(input("Age: "))
    
    self.name = FullName
    self.age= Age
    
  def Display(self):
    print(f"\nname: {self.name}\n age: {self.age}\n")
    
p1 = Person()
p1.Display()