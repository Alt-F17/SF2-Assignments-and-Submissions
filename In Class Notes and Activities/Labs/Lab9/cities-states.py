'''
Consider cities and states in the US. Each state is given a two letter abbreviation. 
You are tasked to read n cities and states from the user and determine the number of special pairs.

Here is an example of a special pair: SCRANTON PA and PARKER SC.
This is a special pair since the first two characters of each city gives the abbreviation for the other city's state. 
That is SC PA and PA SC

A pair of cities is special if they meet this property,  and are not in the same state. Your task is to determine 
the number of special pairs and cities in the provided input. Make sure your code is efficient. That is ,
make use of efficient data structures

Input specification:
--> first line is an integer n (n is large), the number of cities
--> Next n lines: one per city. Each line gives the name of the city in uppercase, a space, and its state's abbreviation in uppercase.
Note that the same city name can exist in multiple states but will not appear more than once in the same state.

Output Specification:
output the number of special pairs and cities

sample input:
12 
SCRANTOM PA
MANISTEE MI
NASHUA NH
PARKER SC
LEFAYETTE CO
WASHOUGAL WA
MIDDLEBOROUGH MA
MADISON MI
MILFORD MA
MIDDLETON MA
COVINGTON LA
LAKEWOOD CO

Sample1 output:
9

read 5 different sample input from the user and write this to a file, 
where there is an empty linens between any two sample inputs Then from this file, read each sample input 
and determine (print) the number of special pairs of cities
'''

n = int(input())
