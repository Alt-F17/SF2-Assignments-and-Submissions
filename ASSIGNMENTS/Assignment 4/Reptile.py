from Animal import Animal

class Reptile(Animal):
    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Reptile"

    def reproduce(self) -> str:
        return super().reproduce() + " Reptiles reproduce by laying eggs, typically on land rather than water."
