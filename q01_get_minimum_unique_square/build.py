def q01_get_minimum_unique_square(a,b):
    
    cnt = 0
    
    for i in range(a,b+1):
        x = (i ** (1/2))
        if x.is_integer():
            cnt += 1
    c = cnt
    return c


