class Complex:
  def __init__(self,real,img):
    self.real = real
    self.img = img
    
  def add (self,number):
    result_real = self.real + number.real
    result_img = self.img + number.img
    
    result = Complex(result_real, result_img)
    return result
n1 = Complex(2,4)
n2 = Complex(-4,2)
n3 = n1.add(n2)
print(f'add: {n3.real} + {n3.img}i')
    