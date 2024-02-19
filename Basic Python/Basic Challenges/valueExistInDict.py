my_dict = {"a": "juice", "b": "grill", "c": "corn"}

# take user input for data
data = input("enter data: ")

flag= False
for i in my_dict.values():
  if i == data:
    flag = True
    break
  
if flag:
  print("Value found")
else:
  print("Value not found")