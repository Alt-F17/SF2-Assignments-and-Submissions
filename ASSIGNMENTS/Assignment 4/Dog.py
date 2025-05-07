from Mammal import Mammal
from Omnivore import Omnivore
from Pet import Pet

class Dog(Mammal, Omnivore, Pet):
    def __init__(self, legs=4, ears=2):
        super().__init__(legs=legs)
        self.ears = ears

    def __repr__(self) -> str:
        mammal_repr = Mammal.__repr__(self)
        omnivore_repr = Omnivore.__repr__(self)
        pet_repr = Pet.__repr__(self)
        return f"{mammal_repr}\nSpecies: Dog\n{pet_repr}\n\n{omnivore_repr}"

    def reproduce(self):
        Mammal.reproduce(self)
        print("Dogs can have up to 12 puppies per litter, depending on the breed and size of the dog.")

    def eat(self):
        Omnivore.eat(self)

    def move(self):
        print("I move by running, pretty fast too!")

    def sleep(self):
        print("Dogs, like humans, sleep in cycles and can sometimes dream.")

    def pet(self) -> str:
        Pet.pet(self)