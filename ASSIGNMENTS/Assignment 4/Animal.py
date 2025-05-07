class Animal:
    def __init__(self, legs=0, fins=0, wings=0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    def reproduce(self) -> str:
        return "Members of this kingdom reproduce by finding a mate of the same species."

    def __repr__(self) -> str:
        return "Kingdom: Animalia"
