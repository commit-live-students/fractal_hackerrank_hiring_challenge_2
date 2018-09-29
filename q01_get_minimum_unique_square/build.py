#%load q01_get_minimum_unique_square/build.py

def q01_get_minimum_unique_square(a,b):

    #ls=[]
    #ls=list(range(a,b+1,1))

#l1=[items for items  in ls if (items**0.5)==int(items**0.5)]

    l1=[items for items  in list(range(a,b+1)) if (items**0.5) % 1 ==0]

    #print(l1)
    
    return len(l1)


q01_get_minimum_unique_square(1,9)




