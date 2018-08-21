# %load q01_get_minimum_unique_square/build.py
# Default imports

from math import sqrt

# Write your solution here:

# def q01_get_minimum_unique_square(x,y):
#     #perfect_squares = [x for x in range(x,y+1) if sqrt(x)==int(sqrt(x))]
#     #return len(perfect_squares)
#     perfect_square=[]
#     for x in range(x,y+1):
#         if sqrt(x)==int(sqrt(x)):
#             return (int(sqrt(x)))
        
def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    perfect_squares = [x for x in range(x,y+1) if sqrt(x)==int(sqrt(x))]
    return len(perfect_squares)

print(q01_get_minimum_unique_square(3,9))


q01_get_minimum_unique_square(3,27)



