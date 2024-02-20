class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def return_another_person(self):
    person = Person('Sandeep',21)
    
    return person
person1 = Person("Ovan",21)

anotherPerson = person1.return_another_person()
print(anotherPerson.name)
print(anotherPerson.age)