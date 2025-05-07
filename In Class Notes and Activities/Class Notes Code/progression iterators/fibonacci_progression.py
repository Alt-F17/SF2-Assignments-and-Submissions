from progression import Progression

class FibonacciProgression(Progression):
    """Iterator producing a Fibonacci progression.
    default iterator: ints 1, 2, 3, ...
    """
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self.previous = None
        self.current = second

    def __advance(self):
        self.previous, self.current = self.current, self.previous + self.current