import math
import random
num=int(input('輸入一個只有1,0組成的八位數'))
num_str=str(num)
num_length=(len(num_str))
d=0
for x in range (1,num_length+1,1):
    a=num%(10**x)
    b=a/(10**(x-1))
    c=(math.floor(b))
    d=d+c
print(d)