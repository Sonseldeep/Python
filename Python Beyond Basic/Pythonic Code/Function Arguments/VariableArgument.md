Introduction
We know that the number of arguments in the function call and the function definition must match otherwise, we will get an error.

def greet(message):
print(message)

greet('Hi', 'Hello')
Output

TypeError: greet() takes 1 positional argument but 2 were given
One way to fix this problem is by placing second parameter in the function definition like this:

# def greet(message, message1):

# print(message)

# greet('Hi', 'Hello')

Output

Hi

# The other way to solve this problem is by using a variable argument so that the function can take any number of arguments.

Next, we will see how to use a variable argument.

Example: Variable Argument
def greet(\*messages):
print(messages)

# calling greet() with 1 argument

greet('Hi')

# calling greet() with 2 arguments

greet('Hi', 'Hello')

# calling greet() without any arguments

greet()
Output

('Hi')
('Hi', 'Hello')
()
In the function definition, we have used _messages as parameter. The _ before the argument name suggests that it's a variable argument and it will always be a tuple.

Function call: greet('Hi')

In the function definition, messages will be ('Hi').

Function call: greet('Hi', 'Hello')

In the function definition, messages will be ('Hi', 'Hello').

Function call: greet()

In the function definition, messages will be an empty tuple, ().

Next, we will create a function that numbers.
