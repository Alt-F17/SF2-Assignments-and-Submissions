from progression import Progression

class geometricProgression(Progression):
    """Iterator producing a geometric progression.
    default iterator: ints 1, 2, 3, ...
    """
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self.base = base

    def __advance(self):
        self.current *= self.base