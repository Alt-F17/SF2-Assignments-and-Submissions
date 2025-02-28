"""
n unopened boxes, k toys inside

box cannot be rotated (otherwise figurines will face wrong way)

each figurine is specified by its height. for example, in a given box, figurine from left to right: [4,5,7]

we would like to organize all the toy boxes s.t. they are in a non-decreasing order or fig height from left to right
however, this may not be possible with our given boxes, hense we need to see if such an arrangement is even possible

input: 
first line n:
    for n:
        k {number of toys in box} [space] h1 [space] h2 [space] ... [space] hk {height of each toy}
        each height is >=1

output:
    YES if it is possible to arrange the boxes in non-decreasing order of height
    NO otherwise
"""
# MAIN PROGRAM:

# Read input

boxes = []

n = int(input("Number of boxes: "))
for i in range(n):
    k = int(input(f"Number of toys in box #{i+1}: "))
    heights = [int(input(f"Height of toy #{j+1}: ")) for j in range(k)]
    boxes.append(heights)

# TODO: check if all boxes are already in non-decreasing order
# if not, print NO and exit

intervals = []
for box in boxes:
    if box != sorted(box):
        exit("Result: NO")
    # Get the interval heights of each box (first and last height)
    intervals.append([box[0], box[-1]])

print("Intervals:", intervals)

# TODO: sort the boxes by first interval (i.e. the intervals)

for i in range(len(intervals)):
    for j in range(i+1, len(intervals)):
        if intervals[i][0] > intervals[j][0]:
            intervals[i], intervals[j] = intervals[j], intervals[i]

# TODO: Check if every last interval of a previous box is lower than the first interval of the next box
# if not, print NO and exit

for i in range(len(intervals)-1):
    if intervals[i][1] > intervals[i+1][0]:
        exit("Result: NO")

print("Result: YES")
print("Sorted Boxes:", boxes)