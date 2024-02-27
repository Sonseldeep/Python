# Problem Description
# Create a program to print the value present at the given key. If the key is out of bounds, print Key is not available.

# Create a dictionary of three items: {'Nepal' : 'Kathmandu', 'Sweden' : 'Stockholm', 'Italy' : 'Rome'}
# Take string input from the user and store it in the key variable.
# Print the value present at that key if the key is present in the dictionary.
# However, if the key is not in the dictionary, print Key is not available.
# Note: Use exception handling to solve this problem.


try:
    countries = {'Nepal' : 'Kathmandu', 'Sweden' : 'Stockholm', 'Italy' : 'Rome'}
    

   
    key = input("enter the key  to get value: ")

   
    print(countries[key])

except:
    if key  not in countries:
        print("Key is not available")
