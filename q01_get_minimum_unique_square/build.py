# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    l = [i**.5 for i in range(x,y+1) if int(i**.5) == i**.5 ]
    return len(l)




