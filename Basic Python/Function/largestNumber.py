def getLargest(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c
  
result = getLargest(1,2,3)

print(f"the greatest is {result}")