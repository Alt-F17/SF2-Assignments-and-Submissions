class Progression:
    """Iterator producing a generic progression.
    default iterator: ints 1, 2, 3, ...
    """
    def __init__(self, start=0):
        self.current = start

    def __advance(self):
        self.current += 1

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current
            self.__advance()
            return answer
        
    def __iter__(self):
        return self
    
    def printProgression(self, n):
        """Prints the first n values of the progression."""
        for _ in range(n):
            print(self.__next__(), end=' ')
        print()
        return self
    
    

if __name__ == "__main__":
    print("Progression")
    print("")
    Progression().printProgression(6)
    Progression(12).printProgression(11)

    for value in Progression(12):
        print(value, end=' ')