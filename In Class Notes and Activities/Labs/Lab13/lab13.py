'''
Implement a custom iterator class to generate 
even numbers in the interval [start, end]
'''
class EvenNumbers:
    '''Default interval range is [0, 10] inclusive'''
    def __init__(self, start=0, end=10):
        self.__end = end if end % 2 == 0 else end - 1
        self.__current = start if start % 2 == 0 else start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < self.__end:
            result = self.__current
            self.__current += 2
            return result
        else:
            raise StopIteration

'''
Implement a custom iterable class for the Fibonacci
numbers.  This class constructor should take n, 
representing the first n terms of the Fibonacci 
sequence
'''
class Fibonacci:
    '''Default Fibonacci range is [1, 1, 2, 3, 5, 8]'''
    def __init__(self, n=6):
        self.n = n

    def __iter__(self):
        self.__a, self.__b = 0, 1
        return self

    def __next__(self):
        if self.n > 0:
            result = self.__a
            self.__a, self.__b = self.__b, self.__a + self.__b
            self.n -= 1
            return result
        else:
            raise StopIteration

'''
Draw the recursion tree for the computation of 
recSum(10)
'''
class RecSum:
    def __init__(self, n=0):
        self.n = n

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.n > 0:
            print(f"recSum({self.n-1}) + {(self.n)}")
            if self.n != 1:
                print("/‾‾‾‾‾\ ")
            self.n -= 1
        else: 
            raise StopIteration
        return self.n

'''
write a recursive function that determines the
minimum element in a given list of integers. 
'''
def MinElement(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_of_rest = MinElement(lst[1:])
        return lst[0] if lst[0] < min_of_rest else min_of_rest

'''
write a recursive function that converts a string of integers
into its integer counterpart
'''
def str_to_int(s):
    if len(s) == 1:
        return int(s[0])
    else:
        return int(s[0]) * (10 ** (len(s) - 1)) + str_to_int(s[1:])

'''
write a recursive function to determine if a given string
is a palindrome
'''
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

'''
Write a recursive function to count number of vowels in a string
'''
def count_vowels(s):
    if len(s) == 0:
        return 0
    else:
        vowels = 'aeiouAEIOU'
        return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

'''
use recursion to determine if a string has more vowels than consonants. 
'''
def has_more_vowels(s):
    vowel_count = count_vowels(s)
    consonant_count = len(s) - vowel_count
    return vowel_count > consonant_count

# OR using recursion:

def has_more_vowels_recursive(s):
    if len(s) == 0:
        return 0, 0  # (vowel_count, consonant_count)
    else:
        vowels = 'aeiouAEIOU'
        vowel_count, consonant_count = has_more_vowels_recursive(s[1:])
        if s[0] in vowels:
            return vowel_count + 1, consonant_count

        else:
            return vowel_count, consonant_count + 1
vowel, cons = has_more_vowels_recursive("hello I am bob and I really hate not having coffee in the morning")
print(f"Has more vowels?: {vowel > cons}")


'''
Implement an itorator that filters out and gives back the even values form a range iterable.
'''

class EvenFilter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            value = self.iterable[self.index]
            self.index += 1
            if value % 2 == 0:
                return value
        raise StopIteration

'''
Write a recursive function that prints all the subsets of a given set.
'''
# def subsets(s):
#     if len(s) == 0:
#         return [[]]
#     else:
#         first = s[0]
#         rest = subsets(s[1:])
#         return rest + [[first] + subset for subset in rest]
    
# print(subsets({1,2,3,4,5,6,7,8,9}))

for i in EvenNumbers(0, 10):
    print(i, end=' ')