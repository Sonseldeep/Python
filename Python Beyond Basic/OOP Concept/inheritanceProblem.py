# Problem Description
# Create the Vehicle class

# Create a class named Vehicle.
# Inside this class, create a method named get_vehicle_features().
# Inside this method, print 'Initializing vehicle features'.
# Create the Car class

# Derive a class named Car from the Vehicle base class.
# Inside this class, create a method named get_car_features().
# In this method, print 'Initializing car features'.
# Outside of the classes

# Create an object of the Car class.
# Access the get_vehicle_features() method using the object.
# Then, access the get_car_features() method using the object.



# create the Vehicle class
class Vehicle:
    # define get_vehicle_features()
    def get_vehicle_features(self):
        print('Initializing vehicle features')


# derive the Car class from Vehicle 
class Car(Vehicle):
    # define get_car_features()
    def get_car_features(self):
        print('Initializing car features')

# create an object of the Car class
car1 = Car()

# call get_vehicle_features() using the object
car1.get_vehicle_features()

# call get_car_features() using the object
car1.get_car_features()