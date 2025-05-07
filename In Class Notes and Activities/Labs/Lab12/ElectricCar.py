from Car import Car
from __future__ import annotations

class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_size: int = 40) -> None:
        '''Initialize the ElectricCar class with make, model, year, and battery size.'''
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self) -> None:
        '''Describe the battery size of the electric car.'''
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("Electric cars don't have gas tanks!")

    def __repr__(self) -> str:
        '''Return a string representation of the electric car.'''
        return f"{self.year} {self.make} {self.model} with a {self.battery_size}-kWh battery."
    
    def update_battery(self, battery_size: int) -> None:
        '''Update the battery size of the electric car.'''
        if battery_size >= self.battery_size:
            self.battery_size = battery_size
        else:
            print("You can't roll back a battery size!")



class Battery:
    def __init__(self, battery_size: int = 40) -> None:
        '''Initialize the Battery class with battery size.'''
        self.battery_size = battery_size

    def get_range(self) -> int:
        '''Get the range of the electric car based on battery size.'''
        if self.battery_size == 40:
            return 150
        elif self.battery_size == 65:
            return 225
        else:
            return 300

    def __repr__(self) -> str:
        '''Return a string representation of the battery.'''
        return f"Battery size: {self.battery_size} kWh."
    