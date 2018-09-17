# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt
import math

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    return(int(math.sqrt(y)) - int(math.sqrt(x)) + 1)
#int(math.sqrt(9))


