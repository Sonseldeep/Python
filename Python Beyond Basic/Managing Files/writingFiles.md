To write contents to a file, we must open it in the write mode using 'w' as the second argument to the open() function.

# open file for writing

# with open('python.txt', 'w') as f:

# perform file operation

# Here, the python.txt file is opened for writing.

There are two things we need to remember while writing to a file.

If we try to open a file that doesn't exist, a new file is created.
If a file already exists, its content is erased, and new content is added to the file.

# Important: We need to be careful when working with files in writing mode because we may accidentally erase old data without realizing.
