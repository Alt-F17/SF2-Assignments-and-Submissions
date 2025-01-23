# N = num_villages
# Distinct point straight road: list
# integer position = tuple list ^^
# equally distant = in A & in B
# neighbourhood has a size
# neighbourhood size = rightmost/max()/ - leftmost/min()/
# Goal: find min sized neighourhood
# 
# First input = num of inputs (range for loop)
# 
# Next lines: village coordinates
# 
# All inputs placed in a list, then sorted

input_count = int(input())

villages = []
for _ in range(input_count):
    villages.append(int(input()))
villages.sort()

n_sizes = []
for i in range(1, input_count-1):
    size = (villages[i] - villages[i-1])/2 + (villages[i+1] - villages[i])/2
    n_sizes.append(size)

min_neighbourhood = min(n_sizes)
print(min_neighbourhood)