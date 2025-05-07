from Animal import Animal

class Fish(Animal):
    def __repr__(self):
        return super().__repr__() + "\nClass: Fish"

    def reproduce(self):
        return super().reproduce() + " Fish reproduction varies largely, some give birth to live young while others lay eggs."
