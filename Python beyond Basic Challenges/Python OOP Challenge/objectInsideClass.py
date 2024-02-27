# Challenge:
# Object Inside Class
# Hard
# Problem Description
# Write a program to create an object of one class inside another class.

# Create Classes

# Create two classes: Engine with attribute power, and Vehicle with attributes: wheels and engine.
# Use the __init__() method with two arguments: self and power to create and initialize the power attribute of the Engine class.
# Use the __init__() method with two arguments self and wheels to initialize the wheels attribute of the Vehicle class.
# Inside the __init__() method of Vehicle, the engine attribute should be assigned with an object of the Engine class with the power attribute equal to 400.
# Create another method named get_power() inside the Vehicle class and print the power attribute of the engine attribute.
# Outside classes

# Create an object of the Vehicle class with wheels attribute equal to 4.
# Call the get_power() method of this object.
# For hints, see the code outline.

# Example
# Expected Output

# 400





class Engine:
  def __init__(self,power):
    self.power = power
  
  
class Vehicle:
  def __init__(self,wheels):
    self.wheels = wheels
    self.engine = Engine(400)
  
  def get_power(self):
    print(self.engine.power)
    
    
v1 = Vehicle(4)
v1.get_power()