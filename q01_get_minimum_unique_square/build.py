# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt
import math

# Write your solution here:

x = 3
y = 9

def q01_get_minimum_unique_square(x,y):
    return (math.floor(math.sqrt(y)) - math.ceil(math.sqrt(x)) + 1)
q01_get_minimum_unique_square(x,y)



