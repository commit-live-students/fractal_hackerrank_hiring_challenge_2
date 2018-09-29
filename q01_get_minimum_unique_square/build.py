# %load q01_get_minimum_unique_square/build.py
# Default imports
import numpy as np
from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    li = list(np.arange(x,y+1))
    final_list = list(filter(lambda x: ((x**0.5)%2 == 0 or (x**0.5)%2 == 1) , li))    
    return len(final_list)
    


