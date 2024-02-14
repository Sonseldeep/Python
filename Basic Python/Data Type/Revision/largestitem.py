numbers = [10, 45, 61, -6,0,98]
largest = numbers[0]

for num in numbers:
  if num > largest:
    largest = num
print(largest)

# or we can wse max() function to get largets
print(max(numbers))