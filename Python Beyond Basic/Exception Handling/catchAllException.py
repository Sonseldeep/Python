try:
  result = 1/0
  lst = [1,2,3]
  print(result)
  print(lst[5])

except:
  print("Error")

finally:
  print("try again")