import math
num=int(input('你想要輸入的正整數'))
num_str=str(num)
num_length=(len(num_str))
d=0
h=0
for x in range (1,num_length+1,2):
    a=num%(10**x)
    b=a/(10**(x-1))
    c=(math.floor(b))
    d=d+c
for x in range (2,num_length+1,2):
    e=num%(10**x)
    f=e/(10**(x-1))
    g=(math.floor(f))
    h=h+g
i=d-h
abs(i)
if i%11 == 0:
    print('這是11的倍數')
else:
    print('這不是11的倍數')