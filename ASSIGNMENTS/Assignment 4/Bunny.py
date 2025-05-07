from Mammal import Mammal
from Herbivore import Herbivore
from Pet import Pet

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs=4, ears=2):
        # NOTE: MRO (Method Resolution Order) determines which __init__ gets called.
        # Here, Mammal's __init__ will be called first.
        super().__init__(legs=legs)
        self.ears = ears

    def __repr__(self) -> str:
        mammal_repr = Mammal.__repr__(self)
        herbivore_repr = Herbivore.__repr__(self)
        pet_repr = Pet.__repr__(self)
        return f"{mammal_repr}\nSpecies: Bunny\n{pet_repr}\n\n{herbivore_repr}"

    def reproduce(self) -> str:
        return Mammal.reproduce(self) + "Bunnies can produce multiple litters per year, potentially having 3-8 kits per litter."

    def eat(self) -> None:
        Herbivore.eat(self)
        print("I mostly eat fresh hay and grass, with some leafy greens and a few pellets. I should only be given fruit and root vegetables, like carrots, as an occasional treat.")

    def move(self) -> None:
        print("I move by hopping and I can see behind me...")

    def sleep(self) -> None:
        print("Bunnies as nocturnal animals, typically sleep around 12 to 14 hours a day in short, intermittent periods.")

    def pet(self) -> str:
        Pet.pet(self)
