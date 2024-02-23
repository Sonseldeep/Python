with open('message.txt','r') as f:
  content = f.read()
  print(content)
  
# this the better approach using with open 
# this code automatically call the f.close()