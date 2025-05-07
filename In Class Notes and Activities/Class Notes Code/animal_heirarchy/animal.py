class Animal:
    def __init__(self, legs=0):
        '''Initialize the Animal class with a number of legs.'''
        self.legs = legs

    def walk(self):
        '''Simulate the animal walking.'''
        print(f"The animal with {self.legs} legs is walking.")

    def sleep(self):
        '''Simulate the animal sleeping.'''
        print("The animal is sleeping. Different animals have different sleep patterns.")

    def __repr__(self):
        '''Return a string representation of the animal.'''
        return f"Animal: Unknown \n Number of Legs: {self.legs} legs."
    

if __name__ == "__main__": # to prevent the code from running when imported ____________ SUPER IMPORTANT!!!

    anim= Animal(4)
    print(anim) # Animal: Unknown \n Number of Legs: 4 legs.
    print()

    anim.walk() # The animal with 4 legs is walking.
    print()
    anim.sleep() # The animal is sleeping. Different animals have different sleep patterns.
    print()
    anim.sleep(5) # The animal is sleeping. Different animals have different sleep patterns.
    print()