from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    ar1 = list(range(x,y+1))
    output = len(list(filter(lambda x: sqrt(x)-int(sqrt(x))==0, ar1)))
    return output
    
    





