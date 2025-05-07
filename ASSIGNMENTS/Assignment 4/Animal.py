class Animal:
    def __init__(self, legs=0, fins=0):
        self.fins = fins
        self.legs = legs

    def reproduce(self):
        return "Members of this kingdom reproduce by finding a mate of the same species."

    def __repr__(self):
        return "Kingdom: Animalia"
