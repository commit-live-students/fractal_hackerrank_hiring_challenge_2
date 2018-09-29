# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    w=list(range(x,y+1))
    p=[  x**0.5 for x  in w  if x**0.5%1==0 ]
    return len(p)

    



