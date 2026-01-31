'''
Jackson Duchow
Vehicle and Car classes
Their are two classes, a master class Vehicle and a subclass Automobile that inherits from Vehicle. Both take inputs from the user and displays them
'''

class Vehicle:
    #initializes the type attribute of the vehicle
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    #initializes all the attributes of the car
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    #displays all the information about the car
    def display_info(self):
        print(f"Vehicle Type: {self.vehicle_type.title()}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make.title()}")
        print(f"Model: {self.model.title()}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof.title()}")


#intro statement
print("Welcome to the Vehicle Information App!")
vehicle_type = input("Enter the vehicle type (Car, Truck, Plane, Boat, or Broomstick): ")
#checks if the vehicle is a car to gather more information
if vehicle_type.lower() == 'car':
    #gathers all the information about the car from the user
    year = input("Enter the car's year: ")
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    while doors != '2' and doors != '4':
        doors = input("Invalid input. Please enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sunroof): ")
    while roof.lower() != 'solid' and roof.lower() != 'sunroof':
        roof = input("Invalid input. Please enter the type of roof (Solid or Sunroof): ")
    user_car = Automobile(vehicle_type, year, make, model, doors, roof)
    user_car.display_info()
else:
    #for non-car vehicles, just create a Vehicle object and display the type
    user_vehicle = Vehicle(vehicle_type)
    print(f"Vehicle Type: {user_vehicle.vehicle_type.title()}")