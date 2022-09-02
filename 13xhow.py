import math
d=0
h=0
n=int(input('你要輸入的數'))
n_str=str(n)
n_len=(len(n_str))
for x in range (3,n_len+3,6):
  a=n%(10**x)
  b=a/(10**(x-3))
  c=(math.floor(b))
  d=d+c
  print(d)
for x in range (6,n_len+3,6):
  e=n%(10**x)
  f=e/(10**(x-3))
  g=(math.floor(f))
  h=h+g
  print(h)
i=d-h
file=open('13xhow.txt',mode='a',encoding='utf-8')
if i%13 == 0: 
  z=(str(n)+'是13的倍數\n')
else:
  z=(str(n)+'不是13的倍數\n')
  
file.write(z)
print(z)

file.close()