import bisect

'''
lst to work with
num want to insert into the lst
[start,end] interval of the lst to consider (default is the whole lst)

>>> import bisect
>>> num = 7
>>> lst = [1, 2, 7, 7, 7, 8, 10, 11]     # must be sorted
>>> bisect(lst, num, start, end)         # returns the index where num should be inserted to keep lst sorted
> returns 5 (the index where 7 should be inserted to keep lst sorted)
> IF 7 is already in the lst, it returns the index of the rightmost place in the lst where 7 can be inserted

>>> bisect_left(lst, num, start, end)  # returns the index where num should be inserted to keep lst sorted
> returns 2 (the index where 7 should be inserted to keep lst sorted)
> IF 7 is already in the lst, it returns the index of the leftmost place in the lst where 7 can be inserted

>>> bisect_right(lst, num, start, end) # returns the index where num should be inserted to keep lst sorted
> returns 5 (the index where 7 should be inserted to keep lst sorted)
> IF 7 is already in the lst, it returns the index of the rightmost place in the lst where 7 can be inserted

NOTE: bisect_right() == bisect()

'''

lst = [1, 2, 7, 7, 7, 8, 10, 11]     # must be sorted
num = 7

print(bisect.bisect(lst, num))         # returns the index where num should be inserted to keep lst sorted
print(bisect.bisect_left(lst, num))    # returns the index where num should be inserted to keep lst sorted
print(bisect.bisect_right(lst, num))   # returns the index where num should be inserted to keep lst sorted