
my_dict = {"a": "juice", "b": "grill", "c": "corn"}

data = input("enter the key: ")
flag = False

for i in my_dict.keys():
  if i == data:
    flag = True
    break
if flag:
  print("Key found")
else:
  print("Key not found")