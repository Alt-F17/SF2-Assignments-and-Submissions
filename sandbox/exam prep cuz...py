output2 = []
lst = [11,22,33,44,55,66,77] #len = n
temp = [0 for _ in lst] #len = n
n = len(temp)
while temp[0] != n:
    output2.append([lst[j] for j in temp])
    temp[-1] += 1
    n = len(temp)
    for idx in range(1,n+1):
        if temp[n-idx] == n:
            temp[n-idx] = 0
            temp[n-idx-1] +=1
        if temp[0] == n:
            break

print(output2)
print(len(output2))

"""
input = [1, 2, 3, ...] len = n

output:
[ 
[1, 1, 1, 1, ..., 1] len = n
[1, 1, 1, 1, ..., 2]
[1, 1, 1, 1, ..., 3]
[1, 1, 1, 1, ..., 4]
...
[1, 1, 1, 1, ..., n]

...
[n, n, n, n, ..., n]
]
"""