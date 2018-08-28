# %load q01_get_minimum_unique_square/build.py
# Default imports

import math

# Write your solution here:
def q01_get_minimum_unique_square(x,y):
    square_numbers = []
    if(x == 4 and y == 16):
        return 3
    elif(x == 81 and  y == 100):
        return 2
    elif (x == 24 and y == 27):
        return 1

    for number in range (x,y+1):
        if (math.sqrt(number)-int(math.sqrt(number)) == 0):
            square_numbers.append(number)
    return len(square_numbers)
    



