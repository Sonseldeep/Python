Multiple Arguments in Lambda
We can pass multiple arguments to a lambda function by separating them with commas. Let's take an example.

# program to find the product of two numbers

product = lambda x, y: x\*y

result = product(5, 10)
print(result) # 50

Here, our lambda function takes two arguments x and y. To take these arguments, we have separated them by commas. Then, the function returns the product of x and y.

Note: A lambda function can take any number of arguments but the body of the lambda can have only one expression.
