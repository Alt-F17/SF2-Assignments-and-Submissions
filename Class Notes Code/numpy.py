# Index 0 is used because when reserving memory, 0 is the offset and all the data is stored after that,
# at distance [index] (eg: 1, 2, 3, ...). So, the first element is at index 0.

# Using numpy to create an array:

import numpy as np

arr = np.array([12 ,33, 77, 72])
# output: array([12, 33, 77, 72])
a1 = np.zeros(10)
# output: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
a2 = np.zeros(10, dtype=int)
# output: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
a3 = np.arrange(0, 10)
# output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
lst = list(range(10))
# output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a4 = np.arrange(0, 10, 3)
# output: array([0, 3, 6, 9])
a5 = np.random.randint(5, 145, 20)
# output: array([6, 92, 53, 66, 14, 72, ........ 20 nums])
a6 = np.empty(4)
# output: array([1.12756537e+093, 2.22525251e+088, 4.08147142e-315, 1.52973828e-308])
a7 = np.ones((3,5), dtype=int)
# output: array([[1, 1, 1, 1, 1], 
#                [1, 1, 1, 1, 1], 
#                [1, 1, 1, 1, 1]])
a8 = np.full((3,5), 7)
# output: array([[7, 7, 7, 7, 7],
#                [7, 7, 7, 7, 7],
#                [7, 7, 7, 7, 7]])
a9 = np.random.randit(5, 135, (3,5))
# output: array([[  6,  92,  53,  66,  14],
#                [ 72,  33,  41,  13,  90],
#                [  3,  30,  84,  78,  61]])
len(a9)
# output: 3


# Arrays work like lists (slicing works the same, fetching as well), 
# but they are more efficient and have more functions.


# Arrays cannot have floats and ints together.
# Floats will be truncated to ints, removing the decimal part.

# ARRAYS MUST HAVE THE SAME DATA TYPE: ALL INTS OR ALL FLOATS OR ALL STRINGS. NO MIX.

# Fetching elements in a 1D array:
arr = np.array([12, 33, 77, 72])
arr[1]
# output: 33
arr[-1]
# output: 72

arr[1:3]
# output: array([33, 77])
arr[1:]
# output: array([33, 77, 72])



# Fetching elements in a 2D array:
arr = np.array([[12, 33, 77, 72], [1, 2, 3, 4]])
arr[1, 2]
# output: 3
arr[1, 1:]
# output: array([2, 3, 4])
arr[1, 1:3]
# output: array([2, 3])





# Adding elements to an array:
arr = np.array([12, 33, 77, 72])
arr + 5
# output: array([17, 38, 82, 77])
arr - 5
# output: array([7, 28, 72, 67])
arr * 5
# output: array([60, 165, 385, 360])
arr / 5
# output: array([2.4, 6.6, 15.4, 14.4])
arr ** 2
# output: array([144, 1089, 5929, 5184])
arr // 5
# output: array([2, 6, 15, 14])
arr % 5
# output: array([2, 3, 2, 2])
arr = np.array([5.12, 4.33, 3.77, 2.72])
arr // 5
# output: array([1.0, 0.0, 0.0, 0.0])


# Comparing arrays:
arr = np.array([12, 33, 77, 72])
arr > 30
# output: array([False,  True,  True,  True])

# NOTE: comparing two arrays of different sizes will return an error.