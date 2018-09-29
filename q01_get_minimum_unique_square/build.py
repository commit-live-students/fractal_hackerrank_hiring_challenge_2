# %load q01_get_minimum_unique_square/build.py
# Default imports
import numpy as np
from math import sqrt

# Write your solution here:
def q01_get_minimum_unique_square(x,y):
    output=0
    list1=np.arange(x,y+1)
    for num in list1:
        output= output+1 if np.sqrt(num).is_integer() else output+0
    return(output)
    
q01_get_minimum_unique_square(3,9)


