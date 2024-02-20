class Student:
  def check_pass_fail(self):
    if self.score >=42:
      return True
    else:
      return False
    
student1 = Student()
student1.name = "Ram"
student1.score = 56
result = student1.check_pass_fail()
print(result)

student2 = Student()
student2.name = "Shree Krishna"
student2.score = 8
result = student2.check_pass_fail()
print(result)