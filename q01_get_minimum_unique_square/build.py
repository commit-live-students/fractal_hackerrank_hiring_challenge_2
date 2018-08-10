# %load q01_get_minimum_unique_square/build.py
# Default imports
import math

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    return math.floor(math.sqrt(y)) - math.ceil(math.sqrt(x)) + 1




