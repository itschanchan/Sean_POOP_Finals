from abc import ABC, abstractmethod

class Menu:
    
    def __init__(self, title: str):
        self.title = title
        
    def display_title(self):
        print(f'{self.title}')

# Abstract class for Vehicle
class Vehicle(ABC):
    
    def __init__(self, vehicle_type):
        self._vehicle_type = vehicle_type

    def __eq__(self, value):
        return self._vehicle_type == value._vehicle_type
    
    @abstractmethod
    def is_valid_vehicle(self, _vehicle_type):
        pass

# Concrete class for VehicleChecker that implements is_valid_vehicle
class VehicleChecker(Vehicle):

    def is_valid_vehicle(self, _vehicle_type):
        return _vehicle_type in ['car', 'bus', 'school bus', 'motorcycle', 'truck']

# Main Menu
title_screen = Menu('Welcome to Python Vehicle Checker!')
title_screen.display_title()

# User Input
vehicle_input = input('Enter your vehicle type: ')

# Create an instance of VehicleChecker and check if the input is a valid vehicle type
vehicle_checker = VehicleChecker('vehicle')
if vehicle_checker.is_valid_vehicle(vehicle_input):
    print(f'{vehicle_input.title()} is a vehicle.')
else:
    print(f'{vehicle_input.title()} is not a vehicle.')
