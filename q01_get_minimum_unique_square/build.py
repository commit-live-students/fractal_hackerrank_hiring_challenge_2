# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    uniq_squares = [x for x in range(x,y+1) if sqrt(x)==int(sqrt(x))]
    #print (uniq_squares)
    return len(uniq_squares)

#q01_get_minimum_unique_square(2,25)


