def isEven(n):
  if (n & 1) == 0:  #bitwise operator 
    print("even")
  else:
    print("odd") # n & 1 == 1 ---> Odd
number = int(input("enter number: "))
isEven(number) 