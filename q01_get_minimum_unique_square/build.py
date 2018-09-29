# %load q01_get_minimum_unique_square/build.py
# Default imports

#from math import sqrt

# Write your solution here:

def q01_get_minimum_unique_square(x,y):
    list1 = range(x,y+1)
    square_list = [items for items in list1 if items**0.5 == int(items**0.5) ]
    return len(square_list)
    ''''mylist=list(range(x,y+1))
    srt=min([int(sqrt(x)) for x in mylist if sqrt(x).is_integer()])
    return srt'''
    
q01_get_minimum_unique_square(3,9)
    

q01_get_minimum_unique_square(3,9)


