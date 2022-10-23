import math
num=int(input('你想要輸入的正整數'))
num_str=str(num)
num_length=(len(num_str))
d=0
h=0
n=0
g=0
for x in range (1,num_length-2+1,1):
    a=num%(10**x)
    b=a/(10**(x-1))
    c=(math.floor(b))
    c=(c*(10**(x-1)))
    d=d+c
print(d)
for x in range (3,num_length+1,1):
    e=num%(10**x)
    f=e/(10**(x-1))
    g=(math.floor(f))
    g=(g*(10**(x-1)))
    h=h+g
h=h/100
g=g/1000
nd=h-g*10
print(h)
print(nd)
if h > 12:
    n=n+1
print(n)
if nd==0 or nd==1 or nd==2 or nd==3 or nd==5 or nd==7 or nd==8:
    if d > 31:
      n=n+1
print(n)
if nd==4 or nd==6 or nd==9:
    if d > 30:
      n=n+1
print(n)