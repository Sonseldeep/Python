# Question
# You are given two numbers but in string format. Now, you need to multiply them and return the multiplication, that too in a string format.

# For example, if the given strings are '12' and '10', your program should return '120'.

def multiply( a,b):
  num1 = int(a)
  num2 = int(b)
  
  product = num1 * num2
  result = str(product)
  
  print(result)
  
multiply('20','10')