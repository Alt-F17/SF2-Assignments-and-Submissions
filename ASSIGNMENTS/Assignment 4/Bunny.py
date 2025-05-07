from Mammal import Mammal
from Herbivore import Herbivore
from Pet import Pet

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs=4, ears=2):
        # NOTE: PRO TIP: MRO (Method Resolution Order) determines which __init__ gets called.
        # Here, use Mammal's __init__ by calling it first.
        super().__init__(legs=legs)
        self.ears = ears

    def __repr__(self):
        mammal_repr = Mammal.__repr__(self)
        herbivore_repr = Herbivore.__repr__(self)
        pet_repr = Pet.__repr__(self)
        return f"{mammal_repr}\nSpecies: Bunny\n{pet_repr}\n\n{herbivore_repr}"

    def reproduce(self):
        return Mammal.reproduce(self) + "Bunnies can produce multiple litters per year, potentially having 3-8 kits per litter."

    def eat(self):
        Herbivore.eat(self)
        print("I mostly eat fresh hay and grass, with some leafy greens and a few pellets. I should only be given fruit and root vegetables, like carrots, as an occasional treat.")

    def move(self):
        print("I move by hopping and I can see behind me...")

    def sleep(self):
        print("Bunnies as nocturnal animals, typically sleep around 12 to 14 hours a day in short, intermittent periods.")

    def pet(self):
        Pet.pet(self)