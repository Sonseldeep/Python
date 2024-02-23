try:
  numbers = [1,2,3] 
  # there is no any exception
  # so it skip except block
  # directly goes to finally block and returns
  
except:
  print("something is wrong")
  
finally:
  print("Please run this code")