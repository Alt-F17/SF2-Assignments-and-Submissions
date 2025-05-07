from animal import Animal
from __future__ import annotations

# inherit from Animal class

class Fish(Animal):
    def __init__(self):
        '''Initialize the Fish class with a number of fins.'''
        super().__init__(0)
        self.type = "Fish"
        self.color = "Blue"

    def sleep(self):
        '''Simulate the fish swimming.'''
        print("The fish is swimming.")

    def __repr__(self) -> str:
        '''Return a string representation of the fish.'''
        return f"Animal: {self.type} \n Number of Fins: 0 fins \n Color: {self.color}."
    
    def change_color(self, color: str) -> None:
        '''Change the color of the fish.'''
        self.color = color
        print(f"The fish is now {self.color}.")

    def same_color(self, other_fish : Fish) -> bool:
        '''Return the color of the fish.'''
        return self.color == other_fish.color

if __name__ == "__main__": 
    fish= Fish()

    print(fish) # Animal: Fish \n Number of Fins: 0 fins \n Color: Blue.
    print()

    fish.walk() # The animal with 0 legs is walking.
    print()
    fish.sleep() # The fish is swimming.
    print()
    fish.change_color("Red") # The fish is now Red.
    print(fish) # Animal: Fish \n Number of Fins: 0 fins \n Color: Red.
    print()
    fish2= Fish()
    fish2.change_color("Red") # The fish is now Red.
    print(fish.same_color(fish2)) # True
    print()
    fish2.change_color("Blue") # The fish is now Blue.s
    print(fish.same_color(fish2)) # False