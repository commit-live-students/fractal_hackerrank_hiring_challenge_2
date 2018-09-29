# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    lst = [num for num in range (x,y+1) if num**(1/2)%1 == 0]
    return len(lst)

q01_get_minimum_unique_square(3,9)



