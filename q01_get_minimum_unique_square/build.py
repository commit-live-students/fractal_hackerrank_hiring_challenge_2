# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    Square_list = [items for items in range(x,y+1) if items**0.5==int(items**0.5)]
    return len(Square_list)

q01_get_minimum_unique_square(3,9)
    




