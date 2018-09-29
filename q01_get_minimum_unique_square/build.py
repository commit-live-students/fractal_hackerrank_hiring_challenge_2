#%load q01_get_minimum_unique_square/build.py
from math import sqrt

# write your solution here

def q01_get_minimum_unique_square(x,y):
    lst =[num for num in range (x,y+1) if num**0.5%1 ==0]
    return len(lst)

q01_get_minimum_unique_square(3,9)


