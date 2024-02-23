try:
  result = 5 / 0
  print(result)
  my_list = [1,2,3]
  print(my_list[9])

except ZeroDivisionError:
  print("Numerator is 0")  # once exception is executed it blocks the other statement 
  
except IndexError:
  print("Invalid Index")