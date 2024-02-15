pass Statement
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future.

We cannot use an empty body or comment in such scenarios because it would cause an error.

n = 10

if n > 10: # write code later

print("Hello")
Output

IndentationError: expected an indented block after 'if' statement on line 3
To solve this problem, we use the pass statement. The pass statement is used as a placeholder that is used to create an empty code block.

Here's how we can resolve the issue in the above program.

n = 10

# notice the use of pass inside the if statement

if n > 10:
pass

print("Hello")
Output

Hello

main.py

Run

12

# Write code here

Output

Previous Lesson
