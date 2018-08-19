# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt
import math

# Write your solution here:

def q01_get_minimum_unique_square(x=4,y=16):
    'write your solution here'
    count = 0
    for i in range(x,y+1):
        square = sqrt(i)
        if square - math.floor(square) == 0:
            count = count + 1
    return count



