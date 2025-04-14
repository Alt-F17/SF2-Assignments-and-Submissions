# Trace the following code and determine the output.

data = {
    'group0': {'a','b'},
    'group1': {'b', 'c'},
    'group2': {'b', 'a', 'd'},
    'group3': {'b', 'e', 'a'},
    'group4': {'d', 'c', 'a'}
}

tmp = []
first_group = data['group0']
group0 = first_group.union(data['group1'])
tmp.append(group0.union(data['group0']).intersection(data['group2'])) 
tmp.append(group0.intersection(data['group4'])) 
data['group1'] = data['group4']
tmp.append(data['group2'].intersection(data['group1'])) 

for i in range(len(tmp)):
    tmp[i] = sorted(tmp[i])
tmp.append(data['group3'].intersection(data['group4']))

print(tmp)

tmp2 = tmp[0] + list(tmp[3])

print(len(set(tmp2)))







# Answer:
# >>> [['a', 'b'], ['a', 'c'], ['a', 'd'], {a}]
# >>> 2