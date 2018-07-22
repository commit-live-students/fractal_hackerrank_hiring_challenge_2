# %load q01_get_minimum_unique_square/build.py
# Default imports

#THIS PROGRAM IS COMPLETE & WORKING.NO ERROR IN CODE> TESTED ON SPYDER 3

import math
# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    z=[]
    c=0
    for a in range(x,y+1):
        
        if(math.sqrt(a).is_integer()):
            z.append(int(math.sqrt(a)))
            c+=1
    return c



