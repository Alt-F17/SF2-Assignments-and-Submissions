from animal import Animal

# inherit from Animal class

class Cat(Animal):
    def __init__(self):
        '''Initialize the Cat class with a number of legs.'''
        super().__init__(4)
        self.type = "Cat"

    def sleep(self, hours=None) -> None:
        '''Simulate the cat sleeping.'''
        if hours is None:
            print("The cat is sleeping.")
        else:
            print(f"The cat is sleeping for {hours} hours.")

    def __repr__(self) -> str:
        '''Return a string representation of the cat.'''
        return f"Animal: {self.type} \n Number of Legs: {self.legs} legs."


if __name__ == "__main__": 
    cat= Cat()

    print(cat) # Animal: Cat \n Number of Legs: 4 legs.
    print()

    cat.walk() # The animal with 4 legs is walking.
    print()