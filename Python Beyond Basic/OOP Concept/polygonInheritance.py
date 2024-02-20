class Polygon:
  def __init__(self,slides):
    self.slides = slides
  def display_info(self):
    print("A polygon is a two dimensional shape with straight lines.")
  def get_perimeter(self):
    perimeter = sum(self.slides)
    return perimeter
  
p1 = Polygon([1,2,3])
p1.display_info()
perimeter = p1.get_perimeter()
print(perimeter)