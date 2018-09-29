# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

def q01_get_minimum_unique_square(x,y):
   return len([int(sqrt(i)) for i in range(x,y+1) if sqrt(i).is_integer()])
    

q01_get_minimum_unique_square(24,27)


