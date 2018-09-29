# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    z=0
    for i in range(x,y+1):
        if (sqrt(i)-int(sqrt(i))==0):
                   z+=1
    return z
    




