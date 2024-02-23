class Polygon:
  def __init__(self,sides):
    self.sides = sides
    
  def display_info(self):
    print("A polygon is a two dimensional shape with straight line")
    
  def getPerimeter(self):
    perimeter = sum(self.sides)
    return perimeter
  
class Triangle(Polygon):
  def display_info(self):
    print("AS triangles are polygon with 3 edge")
    
    super().display_info()
    
t1 = Triangle([1, 2, 3])
perimeter = t1.getPerimeter()
print(f"The Perimeter of the triangle is {perimeter}")
t1.display_info()
    