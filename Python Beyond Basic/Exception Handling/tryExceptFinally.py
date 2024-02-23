try:
  print(1/0)
  
except ZeroDivisionError:
  print("numerator cant be zero")
  
finally:
  print("try again")