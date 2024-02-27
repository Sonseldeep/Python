class Square:
  def __init__(self,length):
    self.length = length
    
  def compute_area(self):
    return self.length ** 2
  def compute_perimeter(self):
    return 4 * self.length
  
length = int(input("enter the length of the square: "))
  
s1 =  Square(length)
area = s1.compute_area()
print(f"area: {area} ")

perimeter = s1.compute_perimeter()
print(f"Perimeter: {perimeter} ")