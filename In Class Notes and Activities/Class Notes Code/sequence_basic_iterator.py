range(3,10)

print(range(3,10)) # >>> range(3, 10)

print(list(range(3,10))) # >>> [3, 4, 5, 6, 7, 8, 9]

for i in range(3,10):
    print(i) # >>> 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9

class Sequence:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
    
    def __len__(self):
        return self.end - self.start


class SequenceIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
        
class SequenceIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return SequenceIterator(self.start, self.end)

    def __len__(self):
        return self.end - self.start




if __name__ == "__main__":
    s = Sequence
    s(3, 10)
    print(s(3, 10)) # >>> <__main__.Sequence object at 0x7f8c4c0b1d90>
    print(list(s(3, 10))) # >>> [3, 4, 5, 6, 7, 8, 9]
    for i in s(3, 10):
        print(i) # >>> 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9



    seq = SequenceIterable(3, 10)
    print(seq) # >>> <__main__.SequenceIterable object at 0x7f8c4c0b1d90>
    print(list(seq)) # >>> [3, 4, 5, 6, 7, 8, 9]
    for i in seq:
        print(i) # >>> 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9
    print(len(seq)) # >>> 7



