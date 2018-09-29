# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    l=list(range(x,y+1))
    c=len([x for x in l if (x**0.5).is_integer()])
    return c
    



