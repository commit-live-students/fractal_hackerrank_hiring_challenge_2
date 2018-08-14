# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    mylist = list(range(x,y + 1))
    perfect_squares_list = [x for x in mylist if sqrt(x) == int(sqrt(x))]
    return len(perfect_squares_list)
    





