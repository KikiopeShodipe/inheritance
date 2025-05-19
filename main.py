# Define the parent class Vehicle
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        # Initialize the vehicle's name, max speed, and mileage
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def display_details(self):
        # Display the vehicle's details
        print("Vehicle Details:")
        print(f"Vehicle Name: {self.name}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} km/l")
# Define the child class Bus that inherits from Vehicle
class Bus(Vehicle):
    pass  # Inherits all properties and methods from Vehicle
# Take input from the user
name = input("Enter the name of the bus: ")
max_speed = input("Enter the maximum speed (in km/h): ")
mileage = input("Enter the mileage (in km/l): ")
# Create an instance of the Bus class using user input
school_bus = Bus(name, max_speed, mileage)
# Call the method to display bus details
school_bus.display_details()
 