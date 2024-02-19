def fact(n):
  if n !=1:
    return n * fact(n-1)
  return n

number = int(input("enter number: "))
print(fact(number))