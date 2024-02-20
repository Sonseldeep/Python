class Student:
  def check(self):
    if self.score >=40:
      return True
    else:
      return False
    

student1 = Student()
student1.name = "Ram"
student1.score =  25
result = student1.check()
print(result)
print(student1.name)
print(student1.score)
student2 = Student()

# Here, student1 and student2 are objects of the Student class.