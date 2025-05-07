from Animal import Animal

class Amphibian(Animal):
    def __repr__(self):
        return super().__repr__() + "\nClass: Amphibian"

    def reproduce(self):
        return super().reproduce() + " Amphibians reproduce by laying soft eggs in the water."