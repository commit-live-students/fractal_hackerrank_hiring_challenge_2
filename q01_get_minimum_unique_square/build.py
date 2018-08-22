# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    prfctsqrt = []
    List = range(x, y+1)
    prfctsqrt = [num for num in List if int(sqrt(num)) * int(sqrt(num)) == num]
#    for num in range(x, y+1):
#        if (num == 1):
#            continue
#        else:
#            sqrtnum = int(sqrt(num))
#            if (sqrtnum * sqrtnum == num):
#                prfctsqrt.append(num)
    return len(prfctsqrt)
q01_get_minimum_unique_square(4, 25)


