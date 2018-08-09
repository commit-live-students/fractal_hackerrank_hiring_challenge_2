# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    square_array = []
    for num in range(2,int(y+1/2)):
        num_square = num**2
        if(num_square >= int(x) and num_square <= int(y)):
            square_array.append(num)
        if(num_square > y):
            break
    return len(square_array)

q01_get_minimum_unique_square(4,16)

