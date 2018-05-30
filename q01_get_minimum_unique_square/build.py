# %load q01_get_minimum_unique_square/build.py
# Default imports

import math
import numpy as np

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    return math.floor(np.sqrt(y)) - math.ceil(np.sqrt(x)) + 1

    


