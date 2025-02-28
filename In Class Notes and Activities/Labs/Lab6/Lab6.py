'''
Quetion 1: Create Pascal's Triangle more efficiently than O(n^3)-time and
O(n^2) space. _________________________________________________________________
'''

def binom(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binom(n-1, k-1) + binom(n-1, k)

def pascal_print(n):
    for row in range(n):
        for k in range(row+1):
            print(binom(row, k), end=' ')
        print()

pascal_print(int(input("Enter the number of rows: ")))

'''
Question 2: ToyBoxes __________________________________________________________
'''

"""
n unopened boxes, k toys inside

box cannot be rotated (otherwise figurines will face 
wrong way)

each figurine is specified by its height. for example, 
in a given box, figurine from left to right: [4,5,7]

we would like to organize all the toy boxes s.t. they 
are in a non-decreasing order or fig height from left 
to right
however, this may not be possible with our given boxes, 
hense we need to see if such an arrangement is even possible

input: 
first line n:
    for n:
        k {number of toys in box} [space] h1 [space] h2 [space] ... [space] hk {height of each toy}
        each height is >=1

output:
- YES if it is possible to arrange the boxes in 
non-decreasing order of height
- NO otherwise
"""
# MAIN PROGRAM:

# Read input

boxes = []

n = int(input("Number of boxes: "))
for i in range(n):
    k = int(input(f"Number of toys in box #{i+1}: "))
    heights = [int(input(f"Height of toy #{j+1}: ")) for j in range(k)]
    boxes.append(heights)

# Check if all boxes are already in non-decreasing order
# if not, print NO and exit

intervals = []
for box in boxes:
    if box != sorted(box):
        exit("Result: NO")
    # Get the interval heights of each box (first and last height)
    intervals.append([box[0], box[-1]])

print("Intervals:", intervals)

# Sort the boxes by first interval (i.e. the intervals)

for i in range(len(intervals)):
    for j in range(i+1, len(intervals)):
        if intervals[i][0] > intervals[j][0]:
            intervals[i], intervals[j] = intervals[j], intervals[i]

# Check if every last interval of a previous box is lower than the first interval of the next box
# if not, print NO and exit

for i in range(len(intervals)-1):
    if intervals[i][1] > intervals[i+1][0]:
        exit("Result: NO")

print("Result: YES")
print("Sorted Boxes:", boxes)


'''
Question 3: Baker Bonus _______________________________________________________
problem statement already online
'''
'''
QUESTION 2: BAKER'S BONUS

A bakery has multiple franchises opened and wants to 
congratulate the franchises that have performed well 
throughout the years, as well as congratulate everyone 
for performing well on certain days of the year.  

Congratulations are offered as follows:
--> if in a single day all franchises combined sell an 
amount of baked goods that is equivalent to multiple 
of baker's dozen (i.e. 13), then all franchises will 
receive a bonus
--> if an individual franchise, throughout its entire 
existence, has sold an amount of baked goods that is 
equivalent to a multiple of a baker's dozen (i.e. 13), 
then the franchise will receive a bonus.  

INPUT SPECIFICATION:
--> first line of input contains 2 values: F and D 
separated by a space.  F represents the number of 
franchises that the bakery has and D represents the 
number of days of information
--> on the next D lines, there will be F integers 
separated by spaces, such that the i-th integer online 
j represents the number of baked goods sold by franchise 
i on day j.  

OUTPUT SPECIFICATION:
Determine, for each day (across all franchises) and for 
each franchise (across all days), whether or not the 
number of baked goods sold is a multiple of 13.  If so, 
track how many baker's dozens were sold.  Report the total 
number of baker's dozens as a single integer on its own line.  



Sample Input-1
4 5
4 3 2 4
3 3 2 1
8 2 4 1
2 2 4 3
9 3 2 3

Sample Output-1
4

Sample Input-2
4 2
4 4 4 1
1 1 3 4

Sample Output-2
1


Explanation of Sample Output:

In the first case, the first franchise sold a total of 
26 baked goods (which is 2 baker's dozens), the second 
franchise sold a total of 13 baked goods (which is 1 baker's 
dozen), and finally, all franchises together sold 13 baked 
goods on the first day (which is 1 baker's dozen). 
This totals to 4 baker's dozens.

For the second dataset, no franchises made enough baked 
goods on their own, but there was a single baker's dozen 
created among them all on the first day. 
This totals to 1 baker's dozen.
'''

# Get the input
# Get input for number of franchises and days
F_D = input().split()
F = int(F_D[0])
D = int(F_D[1])

# Initialize data structure
data = []
for _ in range(D):
    line = input().split()
    row = []
    for num in line:
        row.append(int(num))
    data.append(row)

def baker_bonus(data):
    total_bakers_dozens = 0
    
    # Check each day across all franchises
    for day in range(D):
        day_total = 0
        for franchise in range(F):
            day_total += data[day][franchise]
        if day_total % 13 == 0:
            total_bakers_dozens += day_total // 13
    
    # Check each franchise across all days
    for franchise in range(F):
        franchise_total = 0
        for day in range(D):
            franchise_total += data[day][franchise]
        if franchise_total % 13 == 0:
            total_bakers_dozens += franchise_total // 13
    
    return total_bakers_dozens

print("Question 4: Number of Baker's Dozens:", baker_bonus(data))


'''
Question 4: Unique Paths ______________________________________________________
Given a m by n matrix, you are to determine and print the 
number of unique paths starting at the top left corner and
ending at the bottom right corner of the matrix.  The only
possible moves that can be made are either a move to the
right or down. 

Example-1: 

      0  1
[0   [x, x],
 1   [x, x]  ]

path 1: (0, 0) --> (0, 1) --> (1, 1)
path 2: (0, 0) --> (1, 0) --> (1, 1)

=> output: 2


Example-2: 

      0  1  2
[0   [x, x, x],
 1   [x, x, x],
 2   [x, x, x]  ]

path 1: (0, 0) --> (0, 1) --> (0, 2) --> (1, 2)
path 2: (0, 0) --> (0, 1) --> (1, 1) --> (1, 2)
path 3: (0, 0) --> (1, 0) --> (1, 1) --> (1, 2)

=> output: 3
'''

def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m-1, n) + unique_paths(m, n-1)




'''
Question 5: ___________________________________________________________________
Update Pascal's Triangle code so that your algorithm uses only O(1) space.  
'''

print("Question 5: Already Did!")
# %%
