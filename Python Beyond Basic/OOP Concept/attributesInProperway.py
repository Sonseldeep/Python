class Student:
  def __init__(self,name,score):
    self.name = name
    self.score = score
    
  def passFail(self):
    if self.score >=42:
      return True
    else:
      return False

student1 = Student("Sandeep",97)
result = student1.passFail()
print(f"Did {student1.name} pass: {result}")

student2 = Student("Ram", 41)
result = student2.passFail()
print(f"Did {student2.name} pass: {result}")
