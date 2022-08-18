import math
num=int(input('你想要輸入的正整數'))
num_str=str(num)
num_length=(len(num_str))
d=0
for x in range (1,num_length+1,2):
    a=num%(10**x)
    b=a/(10**(x-1))
    c=(math.floor(b))
    d=d+c
print(d)