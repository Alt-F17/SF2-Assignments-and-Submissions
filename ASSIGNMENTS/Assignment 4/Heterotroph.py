class Heterotroph:
    def __init__(self, legs=0, fins=0):
        legs = legs
        self.fins = fins

    def __repr__(self) -> str:
        return "This organism is a heterotroph. It is unable to produce its own food, so it eats other organisms."

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food.")
