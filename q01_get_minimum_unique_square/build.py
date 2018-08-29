# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt
import numbers
# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    count = 0
    for t in range(x,(y+1)):
        if (sqrt(t)-int(sqrt(t)))==0:
            count = count+1
    return count




