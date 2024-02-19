def greet( *text):
  print(text)
  
greet("hi")
greet("hi",'hello')
greet()

# In the function definition, we have used *text as parameter. The * before the argument name suggests that it's a variable argument and it will always be a tuple.

# Function call: greet()

# In the function definition, messages will be an empty tuple, ().