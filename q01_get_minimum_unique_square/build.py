# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    z=len(list(filter(lambda x:(sqrt(x)-int(sqrt(x))==0),range(x,y+1))))
    return z
    

q01_get_minimum_unique_square(3,25)


