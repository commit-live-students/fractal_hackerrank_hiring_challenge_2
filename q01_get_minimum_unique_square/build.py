# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    x_list=[x for x in range(x,y+1) if x**0.5==int(x**0.5)]
    print(x_list)
    print(len(x_list))
    return len(x_list)

q01_get_minimum_unique_square(9,25)



q01_get_minimum_unique_square(3,9)





