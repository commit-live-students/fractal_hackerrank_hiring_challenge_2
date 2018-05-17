import sys
import math
from math import sqrt

x = 3
y = 9

def q01_get_minimum_unique_square(x,y):
    return (math.floor(math.sqrt(y)) - math.ceil(math.sqrt(x)) + 1)
print(q01_get_minimum_unique_square(x,y))
