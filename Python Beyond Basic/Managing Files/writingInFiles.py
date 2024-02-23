with open('message.txt','w') as f:
  
 
  content = f.write("New message are included and previous is being deleted, is true?")
  print(content)
  
# Important: We need to be careful when working with files in writing mode because we may accidentally erase old data without realizing.