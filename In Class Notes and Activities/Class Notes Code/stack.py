class Stack:
    def __init__(self):
        self.__data = [1,2,3,4]
    def push(self, item):
        self.__data.append(item)
    def pop(self):
        if len(self.__data) == 0:return None
        else:return self.__data.pop()
    def peek(self):
        if len(self.__data) == 0:return None
        else:return self.__data[-1]
    def is_empty(self):
        return len(self.__data) == 0
    def size(self):
        return len(self.__data)
    def __str__(self):
        return str(self.__data)
    def __repr__(self):
        return ' '.join(list(map(str, self.__data)))
    def __len__(self):
        return len(self.__data)
    def __getitem__(self, index):
        return self.__data[index]
    def __setitem__(self, index, value):
        self.__data[index] = value
    def __delitem__(self, index):
        del self.__data[index]
    def __contains__(self, item):
        return item in self.__data
    

print(Stack()._Stack__data)
print
