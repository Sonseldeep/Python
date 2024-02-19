def greeting(text="Namaskar"):
  print(text)
greeting()
greeting("Hi")

def add(x=0,y=0):
  result = x + y
  print( result)
add(1)

# applying lambda function as default argument

sum = lambda x=0,y=0: x + y
result2= sum (9)
print(result2)