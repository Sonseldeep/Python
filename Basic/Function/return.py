# note:
#   return statement indicates that 
#   end the execution of function
# Basically, when a return statement is encountered,
# the function ends immediately,
# and the control returns back 
# to the function call.
def greet(name):
  print(f"hello {name}")
  return
  print("How do you do?")
  
greet("Ram")
print("Next statement")