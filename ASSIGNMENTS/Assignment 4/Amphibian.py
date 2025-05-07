from Animal import Animal

class Amphibian(Animal):
    def __repr__(self) -> str:
        return f"{super().__repr__()}\nClass: Amphibian"

    def reproduce(self):
        print("Members of this kingdom reproduce by finding a mate of the same species. Amphibians reproduce by laying soft eggs in the water.")
