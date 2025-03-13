'''
write a function called combine2 that takes 2 dictionaires d1 and d2
    and combines them together into a new dictionary and returns
    this dictionary.
Here are the details: 
--> d1 and d2 are dictionary of dictionaries.  The inner dictionary
    values are lists of integers
--> if d1 and d2 have the same key, for which the respective inner
    dictionaries both in d1 and d2 also have the same key k, then
    k is added as a key to the  combined dictionary and the value
    is the sum of the values in the respective lists.  

>>> d1 = {'a': {3: [2], 4: [5, 6]}}
>>> d2 = {'a': {3: [8, 12]}}
>>> combine2(d1, d2)
{3: 22}
'''

def combine2(d1, d2):
    combined = {}
    for key in d1:
        if key in d2:
            combined[key] = {}
            for inner_key in d1[key]:
                if inner_key in d2[key]:
                    combined[key][inner_key] = sum(d1[key][inner_key] + d2[key][inner_key])
    return combined

'''
create a file birthdays.py that will do the following:

(a) write a function that reads birthdays of people
    from the user and stores them in a dictionary
    of dictionaries.  Once the user enters 'stop', you 
    will read no more input from the user.  You may
    assume the user will give valid input.

    Sample Input:
    month day name: February 23 Bob
    month day name: May 3 Katie
    month day name: May 8 Paul
    month day name: May 8 Lucy
    month day name: stop

    Sample Ouput (i.e. returned by function)
    { 'February': {'23': ['Bob']},
    'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} }
'''

def get_birthdays():
    input_string = input("month day name: ")
    birthdays = {}
    while input_string != "stop":
        month, day, name = input_string.split()
        if month in birthdays:
            if day in birthdays[month]:
                birthdays[month][day].append(name)
            else:
                birthdays[month][day] = [name]
        else:
            birthdays[month] = {day: [name]}
        input_string = input("month day name: ")
    return birthdays

'''
(b) Write a function called mostCovered that will take 
the dictionary entered by the user in part (a) and
return the month that has the most number of 
birthdays
'''

def mostCovered(birthdays):
    max_month = ""
    max_count = 0
    for month in birthdays:
        count = 0
        for day in birthdays[month]:
            count += len(birthdays[month][day])
        if count > max_count:
            max_count = count
            max_month = month
    return max_month


'''
(c) write a function called invert() that will take
the birthday month dictionary entered by the user in
part(a) and return the equivalent brithday dictionary

Sample Input is the dictionary returned in part (a)

Sample Output:
{'Bob': ('February', '23'), 
'Katie': ('May', '3'),
'Paul': ('May', '8'), 
'Lucy': ('May', '8')}
'''

def invert(birthdays):
    inverted = {}
    for month in birthdays:
        for day in birthdays[month]:
            for name in birthdays[month][day]:
                inverted[name] = (month, day)
    return inverted