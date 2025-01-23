def isDistinct(y: int) -> bool:
    v = set(y)
    return len(v) == 4

ye = int(input("4 Digit Distinct: "))

while not isDistinct(ye):
    ye += 1

print(ye)