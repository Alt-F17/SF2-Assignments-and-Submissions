from Animal import Animal

class Amphibian(Animal):
    def __repr__(self) -> str:
        return f"{super().__repr__()}\nClass: Amphibian"

    def reproduce(self) -> str:
        return super().reproduce() + " Amphibians reproduce by laying soft eggs in the water."
