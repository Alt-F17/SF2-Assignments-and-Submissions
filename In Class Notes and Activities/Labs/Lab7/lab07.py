'''
Given a dictionary of keys that are strings and/or ints,
values are lists, write a snippet of code tjay returns the total
number of elements in all the lists whose keys are strings in the dictionary.
'''

def total_string_values(d):
    total = 0
    for key in d:
        if type(key) == str:
            total += len(d[key])
    return total

"""
Write a function wordTally that takes an int arg n and reads n words from the user.
Note that the user may enter the same word multiple times. 
Your function should tally up how many times each word was entered and return a dictionary
where the keys are the words and the values are the number of times each word was entered.

You may create only one collection, namely the dictionary of your function.
"""

def wordTally(n):
    tally = {}
    for i in range(n):
        word = input('Enter a word: ')
        if word in tally:
            tally[word] += 1
        else:
            tally[word] = 1
    return tally

print(wordTally(int(input('Enter a total number of Words: '))))


"""
Invert the dictionary:
d = {3: 5, 4: 5, 6:1}
if multiple keys have the same value, the value in the inverted dictionary should be a list of the keys.
"""

def invert_dict(d):
    inverted_dict = {}
    for key in d:
        if d[key] in inverted_dict:
            inverted_dict[d[key]].append(key)
        else:
            inverted_dict[d[key]] = [key]
    return inverted_dict

print(invert_dict({3: 5, 4: 5, 6:1}))

'''
Given a sequence of m words and an int k, find the kth most common word in the sequence.
a word w is the kth most common if exactly k-1 distinct words are more common than w.
'''

def kth_most_common(k):
    words = wordTally(int(input('Enter a total number of Words: ')))
    values = list(words.values())

'''
eg: 
cut: 4
fox: 3
hi: 2
bye: 2
river: 1
stream: 1
brook: 1

k = 1
output: cut

k = 2
output: fox

k = 3
output: [hi, bye]

k = 4
output: 'No kth most common word'
Why?: There are only 3 distinct words that are more common than river, stream, brook
'''
