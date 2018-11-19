# Default imports

from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    "write your solution here"
    count=0
    while(x<=y):
        if( int(sqrt(x))== sqrt(x)):
            count+=1
        x+=1
    return count
