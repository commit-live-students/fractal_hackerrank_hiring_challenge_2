# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    return len(list(filter(lambda x :sqrt(x).is_integer(),list(range(x,y+1)))))
    

sqrt(7).is_integer()
range(1,9)
ts = list(range(1,9+1))



