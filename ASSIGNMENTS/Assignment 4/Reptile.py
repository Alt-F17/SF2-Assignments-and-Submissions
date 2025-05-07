from Animal import Animal

class Reptile(Animal):
    def __repr__(self):
        return super().__repr__() + "\nClass: Reptile"

    def reproduce(self):
        return super().reproduce() + " Reptiles reproduce by laying eggs, typically on land rather than water."
