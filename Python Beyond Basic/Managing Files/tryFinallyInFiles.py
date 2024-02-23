try:
  f = open('message.txt','r')
  content = f.read()
  print(content)
  
finally:
  f.close()