# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    range1 = range(x,y+1,1)
    count = 0
    for i in range1: 
        if ((i ** 0.5) - int(i ** 0.5) == 0) : 
            count = count + 1

    return (count)
    



