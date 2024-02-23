f = open('message.txt')
# note: while opening file or reading file, check your current directory if your files is in global directory no worry if not you have to go in that specific directory

content = f.read()
print(content)
f.close()
