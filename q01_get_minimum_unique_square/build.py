# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    a = [ x for x in range(x,y+1) if sqrt(x) % 1 == 0]
    return len(a)
    
    
q01_get_minimum_unique_square(4,100)


