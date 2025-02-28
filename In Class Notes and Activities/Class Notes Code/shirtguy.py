data = input("[Number of shirts] [Number of Days]: ").split()
total = int(data[0])
clean = total
days = int(data[1])
wash = 0

events = [int(x) for x in input("Enter the days of events: ").split()]

for i in range(1, days + 1):
    if clean == 0:
        clean = total
        wash += 1
    clean -= 1
    if i in events:
        total += 1
        clean += 1
print(wash)