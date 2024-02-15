def primeCheck(number):
    for i in range(2,number):
        if ( number % i == 0):
            return False
            break
    return True

n1 = 50
n2 = 100

for number in range(n1, n2+1):
    result = primeCheck(number)
    
    if result:
        print(number)