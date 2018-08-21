# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt
import numpy as np

# Write your solution here:
def q01_get_minimum_unique_square(x,y):
    ''' Function to get square count between range'''
   
    #convert the number into a array range
    count = 0 
    arr = np.arange(x,y+1)

    for i,v in enumerate(arr):
        if sqrt(v).is_integer(): #check if sqrt is integer
            count+=1

    return count


q01_get_minimum_unique_square(5,8)


