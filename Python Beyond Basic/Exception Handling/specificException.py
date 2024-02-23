try:
  num1 = int(input("enter num1: "))
  num2 = int(input("enter num2: "))
  
  result = num1 / num2
  print(result)
  num = [1,2,3,4]
  index = int(input("enter index: "))
  print(num[index])
except IndexError:
  print("Invalid index")
  
except ZeroDivisionError:
  print("cant be 0 as num2")

except IndexError:
  print("Invalid index")