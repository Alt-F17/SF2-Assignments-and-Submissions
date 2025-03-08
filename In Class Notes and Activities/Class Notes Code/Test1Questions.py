"""
Question 1: (judged: Too difficult)
Theme: Dictionaries
Difficulty: Medium (Difficult), short answer question

What is the output of the following code snippet?

Trace the code and write the output of the code snippet below.
"""

d1 = {3: 5, 4: 5, 1:5, 11:42, 0.5:12}
d2 = {9: 45, 16:37, 25:1, 11:51, 144:0.25}

output = []
for key in d1:
    if d1[key]**2 in d2 and key == d2[d1[key]**2]:
        output.append(True)
    else:
        output.append(False)

print(output)

# Solution: [False, False, True, False, True]

"""
Question 1.1:
Theme: Dictionaries
Difficulty: Medium, short answer question

Trace the code and write the output of the code snippet below.
"""

d = {(3,4):12, (4,5):9, (10,10):100, (2,2):4, (10,20):200}

param1 = []
for key in d:
    if key[0] * key[1] == d[key]:
        param1.append(True)
    else:
        param1.append(False)

param2 = [key[0] + key[1] == d[key] for key in d]

output = [param1[i] == param2[i] for i in range(len(param1))]

for i in range(len(output)):
    print(output[i], end=" ")

# Solution: False False False True False

"""
Question 2:
Theme: numpy + pandas + matplotlib
Difficulty: Something not overly difficult

Write a function that creates a pandas DataFrame with the following columns:
- 'Number1': a numpy array of 1000 random numbers between 0 and 1
- 'Number2': another numpy array of 1000 random numbers between 0 and 1
- 'Sum': the sum of the corresponding 'x' and 'y' values
- 'Product': the product of the corresponding 'x' and 'y' values

The function should print the first 5 rows of the DataFrame.
The function shuld print the last 5 rows of the DataFrame.
The function should return the 794th row of the DataFrame as a tuple.
"""

# Solution:
import numpy as np
import pandas as pd

def create_dataframe():
    df = pd.DataFrame({
        'Number1': np.random.rand(1000),
        'Number2': np.random.rand(1000)
    })
    df['Sum'] = df['Number1'] + df['Number2']
    df['Product'] = df['Number1'] * df['Number2']
    
    print(df.head())
    print(df.tail())
    
    return tuple(df.iloc[793])

print(create_dataframe())