# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(z,y):
    'write your solution here'
    a_list=len([x for x in range(z,y+1) if x**0.5==int(x**0.5)])
    return a_list
q01_get_minimum_unique_square(3,9)
z=3
y=9




