Appending Content to Files

We use 'a' as the second argument to the open() function for append mode. Here's how this mode works:

# If we try to append content to a file that doesn't exist, a new file is created.

# If a file already exists, additional data is appended to the end of the file without erasing the previous data.

# Suppose, we have a file named python.txt with this content.

# opening file in append mode

with open('python.txt', 'a') as f:
f.write(' Appending data using the same write() method.')

# When we run the code, the python.txt file will have this content.

Learning about Python files. Appending data using the same write() method.

Here, we have used the same write() method. However, since we are opening the file in the append mode, this code appends the strings inside write() to the end of the python.txt file.
