# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    
    result = [] # empty list for storing square number
    for x in range(x,y+1): 
        if(sqrt(x) == int(sqrt(x))):  #expression to check square number
            result.append(x) # add square number to empty list
            
    return len(result)
q01_get_minimum_unique_square(4,16)
    
sqrt(4) == 'int'
2.1 == 2


