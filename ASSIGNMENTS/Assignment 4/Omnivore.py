from Heterotroph import Heterotroph

class Omnivore(Heterotroph):
    def __repr__(self) -> str:
        return super().__repr__() + " This organism is an omnivore, it can feed on both plants and other animals."

    def eat(self) -> None:
        super().eat()
        print("I eat anything!")