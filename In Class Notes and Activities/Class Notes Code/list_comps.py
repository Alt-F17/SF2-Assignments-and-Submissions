def isOdd(x):
    return x % 2 != 0

lu = [5,8,25,837,24,847,95,456,3256,4876,958,265,145,456,958]

print(list(filter(isOdd, lu)))

numbers = [10,23,384,32,54]

print(list(filter(lambda x: x % 2 == 0, numbers)))

l = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81], [85, 91, 89, 89], [93, 92, 80, 87]]

print(map(lambda x: sum(x)/len(x), l))

for i in l:
    for j in i:
        print(j, end = " ")
    print()

# compute average of all elements in l (including sublists)

total = 0
count = 0
for i in l:
    total += sum(i)
    count += len(i)
print(total/count)

t = ('aa', 3, [4,5])
n= t[2]
n[1] = 10
print(t)
