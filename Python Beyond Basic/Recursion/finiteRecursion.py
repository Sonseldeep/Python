def sum(n):
  if n !=0:
    n = n + sum(n-1)
  return n
result = sum(5)
print(result)