def Greeting():
  text = 'Hello'
  print(text)
  Greeting()


Greeting()

# Here, we have called the Greeting() function from inside the Greeting() function itself.

# Hence, the Greeting()function is called again and again. This is an example of infinite recursion.

