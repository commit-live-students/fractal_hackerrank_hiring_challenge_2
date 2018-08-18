# %load q01_get_minimum_unique_square/build.py
# Default imports

import math

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    count=0
    for i in range(x,y+1):
        if math.sqrt(i)==math.floor(math.sqrt(i)):
            count=count+1
    return (count)

c=q01_get_minimum_unique_square(3,9)
c


