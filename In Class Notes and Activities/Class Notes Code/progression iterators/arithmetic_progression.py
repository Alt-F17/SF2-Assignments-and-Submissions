from progression import Progression

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression.
    default iterator: ints 1, 2, 3, ...
    """
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self.increment = increment

    def __advance(self):
        self.current += self.increment