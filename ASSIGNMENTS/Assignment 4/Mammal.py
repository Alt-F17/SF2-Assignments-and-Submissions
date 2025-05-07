from Animal import Animal

class Mammal(Animal):
    def __repr__(self):
        return super().__repr__() + "\nClass: Mammal"

    def reproduce(self):
        return super().reproduce() + " Mammals give birth to live young, and raise them until they can be independent."