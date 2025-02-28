def new_butterfly(kinds, counts, sighting):
    if sighting not in kinds:
        kinds.append(sighting)
        counts.append(1)
    else:
        counts[kinds.index(sighting)] += 1
    return kinds, counts

kinds = ['Monarch', 'Painted Lady', 'Bronze Copper', 'Orange Sulphur']
counts = [5,2,12,7]

for i in range(len(kinds)):
    print(f"{kinds[i]}: {counts[i]}")

new_butterfly('Black Swallowtail', 3)

# Now using a dictionary:

def new_butterfly_dict(butterfly_dict, sighting):
    if sighting not in butterfly_dict:
        butterfly_dict[sighting] = 1
    else:
        butterfly_dict[sighting] += 1
    return butterfly_dict

butterfly_dict: dict = {'Monarch': 5, 'Painted Lady': 2, 'Bronze Copper': 12, 'Orange Sulphur': 7}

for key in butterfly_dict:
    print(f"{key}: {butterfly_dict[key]}")





# Keys in dictionaries are immutable, so you can't use a list as a key.
# You can use a tuple as a key.

# A few dictionary commands:
# dict.keys() - returns a list of keys
# dict.values() - returns a list of values
# dict.items() - returns a list of tuples of key-value pairs
# dict.get(key) - returns the value associated with the key:
#     if the key is not in the dictionary, returns None:
#     if the key is not in the dictionary, returns the second argument
#     dict.get(key, default) - returns the value associated with the key:
#     if the key is not in the dictionary, returns default


# dict.pop(key) - removes the key-value pair from the dictionary
# dict.popitem() - removes the last key-value pair from the dictionary
# dict.clear() - removes all key-value pairs from the dictionary