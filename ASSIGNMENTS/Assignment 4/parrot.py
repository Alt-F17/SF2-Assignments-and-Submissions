from Bird import Bird
from Omnivore import Omnivore
from Pet import Pet

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs=4, ears=2):
        super().__init__(legs=legs)
        self.ears = ears

    def __repr__(self) -> str:
        bird_repr = Bird.__repr__(self)
        omnivore_repr = Omnivore.__repr__(self)
        pet_repr = Pet.__repr__(self)
        return f"{bird_repr}\nSpecies: Parrot\n{pet_repr}\n\n{omnivore_repr}"

    def reproduce(self) -> str:
        return Bird.reproduce(self) + "Parrots often take a few days to lay a full clutch of eggs. This can be as many as three to four eggs."

    def eat(self) -> None:
        Omnivore.eat(self)
        print("I eat both plant and animal matter. My natural diet includes a variety of foods like seeds, nuts, fruits, vegetables, flowers, buds, and insects.")

    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb, and even use a unique method called "beakiation" to traverse narrow branches.')

    def sleep(self) -> None:
        print("Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day.")

    def pet(self) -> str:
        Pet.pet(self)