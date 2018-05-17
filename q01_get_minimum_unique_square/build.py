# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    count = 0
    for i in range(1,x+1):
        if i**2 >= x and i**2 <= y:
            count = count + 1

    return count
