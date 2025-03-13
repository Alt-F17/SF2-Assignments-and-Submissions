"""
Input
First line = 2 ints = N & M
Next n lines contains a single S
all strings are unique
next m sections contain a single int I
followd by T lines, each containing a single string R

Output: A single integer on a single line to answer the question: How many assignments can be completed

Input: 
3 3
chalk
cheese
charger
1
cheese
2
coins
cash
3
charger
chalk
caffiene

Output: 1

USE SETS
"""

frist_line = input()
n, m = frist_line.split()
n = int(n)
m = int(m)
count = 0
needed = []
i = {}
t = {}

for _ in range(n):
    needed.append(input())

for j in range(m):
    i[j] = int(input())
    t[j] = []
    for _ in range(i[j]):
        t[j].append(input())

for j in range(m):
    if all(item in needed for item in t[j]):
        count += 1
print(count)