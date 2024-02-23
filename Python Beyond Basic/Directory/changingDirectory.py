import os
print(f"current working directory: {os.getcwd()}")

os.chdir('/Desktop/Python/Basic Python')
print(f"After changing directory: {os.getcwd()}")