lambda function is just like a regular function with couple of differences:
----> a lambda function doesn't have name
----> body of lambda function can gave only one expression

Before we learn about lambda functions, let's see an example of a regular function. Then, we will see how we can write the same code using a lambda function.

def double(n):
return n\*2

print(double(10))

Here, the double() function takes a single argument and returns its double.

Now, we will see how we can write the same function using lambda

            double = lambda n: n*2
            print(double(10))

We use the lambda keyword to define lambda functions. The variable before the : is the argument and the variable after the : is the return value.

In the program, the lambda function is assigned to the double variable. Now, to call this lambda function, we have used this code: double(value).
