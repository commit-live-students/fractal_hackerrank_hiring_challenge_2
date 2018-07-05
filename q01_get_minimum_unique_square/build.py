# Default imports

from math import sqrt
import math
# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    "write your solution here"
    return(math.floor(math.sqrt(y)) - math.ceil(math.sqrt(x)) + 1)
