from Animal import Animal

class Fish(Animal):
    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Fish"

    def reproduce(self) -> str:
        return super().reproduce() + " Fish reproduction varies largely, some give birth to live young while others lay eggs."
