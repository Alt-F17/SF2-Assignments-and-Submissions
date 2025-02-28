def combine(d1, d2):
    """
    The value associated with each key in 
    """
    for key in d2:
        if key in d1:
            d1[key] += d2[key]
        else:
            d1[key] = d2[key]
    return d1


def combine2(d3, d4):
    """
    if the key is the same, returns the value of the sum of the two values 
    (only applies for lists in sub-dictionaries)
    if the key is different, returns the value of the key
    """
    for key in d4:
        if key in d3:
            for key2 in d4[key]:
                if key2 in d3[key]:
                    d3[key][key2] += d4[key][key2]
                else:
                    d3[key][key2] = d4[key][key2]
        else:
            d3[key] = d4[key]
    return d3

d1 = {1: [2], 4: [5,6]}
d2 = {4: [8]}

d3 = {
    'a': {
        3: [2],
        4: [5,6]
        },

    'b': {
        7: [2,7,9],
        4: [5,6]
        }
    }

d4 = {
    'a': {
        3: [8, 12]
        },

    'b': {
        7: [7, 33]
        }
    }