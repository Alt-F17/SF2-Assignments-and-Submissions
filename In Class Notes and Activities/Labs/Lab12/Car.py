class Car:
    def __init__(self, make: str, model: str, year: int, odometer_reading = 0) -> None:
        '''Initialize the Car class with make, model, and year.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def __repr__(self):
        '''Return a string representation of the car.'''
        return f"{self.year} {self.make} {self.model} with {self.odometer_reading} miles."
    
    def read_odometer(self) -> None:
        '''Read the odometer of the car.'''
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage: int) -> None:
        '''Update the odometer of the car.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles: int) -> None:
        '''Increment the odometer of the car.'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
    
    def fill_gas_tank(self) -> None:
        '''Fill the gas tank of the car.'''
        print("The gas tank is now full.")