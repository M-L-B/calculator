import math
for num in range(0,10000000000):
    num_str=str(num)
    num_length=(len(num_str))
    d=0
    h=0
    for x in range (1,num_length+1,2):
        a=num%(10**x)
        b=a/(10**(x-1))
        c=(math.floor(b))
        d=d+c**num_length
    for x in range (2,num_length+1,2):
        e=num%(10**x)
        f=e/(10**(x-1))
        g=(math.floor(f))
        h=h+g**num_length
    if h+d==num:
        print(num,'是水仙花數')