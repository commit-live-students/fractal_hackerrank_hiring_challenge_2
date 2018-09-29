# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    x = len([i for i in list(range(x,y+1)) if(i**0.5).is_integer()])
    return x



