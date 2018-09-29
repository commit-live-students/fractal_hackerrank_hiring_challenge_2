# %load q01_get_minimum_unique_square/build.py
# Default imports
import math
from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(a,b):
    'write your solution here' 
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1) 

q01_get_minimum_unique_square(3,9)



