Default Arguments in print()

By the way, default arguments are used in the print() function as well. Let's take an example,

print('Hello','there')
Output

Hello there

# If you have noticed, there is a space between 'Hello' and 'there' by default. It's because of the default argument named sep which stands for separator. The default value of sep is ' '.

Let's see what will happen if we change the value of the sep argument.

# print('Hello', 'there', sep = '###')

Output

Hello###there
Since the separator is '###' now, we can see three # characters between the strings.
