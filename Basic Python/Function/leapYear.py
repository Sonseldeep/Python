def isLeapYear(year):
  if ( year % 4 ) ==0 and (year % 100)!=0 or (year % 400)==0:
    return True
  else:
    return False

yrs = int(input("enter year: "))

if True:
  print(f"{yrs} is leap year")
else:
  print(f"{yrs} is not leap year")