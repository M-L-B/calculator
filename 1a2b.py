import random
import math
aa=0
ab=0
for q in range (9999):
  x=(random.random()*9999)
  x=(math.floor(x))
  a=x%10
  e=x%100/10
  b=(math.floor(e))
  f=x%1000/100
  c=(math.floor(f))
  g=x%10000/1000
  d=(math.floor(g))
  if a != b:
    if b != c:
      if c != d:
        if a != d:
          break
print(x)
print('歡迎來到游戲1a2b')
print('你有五次機會來猜出數字')
for n in range(5):
  aa=0
  ab=0
  y=int(input('你猜的數'))
  ga=y%10
  ge=y%100/10
  gb=(math.floor(ge))
  gf=y%1000/100
  gc=(math.floor(gf))
  gg=y%10000/1000
  gd=(math.floor(gg))
  if ga == a:
    aa=aa+1
  if ga == b:
    ab=ab+1
  if ga == c:
    ab=ab+1
  if ga == d:
    ab=ab+1
  if gb == a:
    ab=ab+1
  if gb == b:
    aa=aa+1
  if gb == c:
    ab=ab+1
  if gb == d:
    ab=ab+1
  if gc == a:
    ab=ab+1
  if gc == b:
    ab=ab+1
  if gc == c:
    aa=aa+1
  if gc == d:
    ab=ab+1
  if gd == a:
    ab=ab+1
  if gd == b:
    ab=ab+1
  if gd == c:
    ab=ab+1
  if gd == d:
    aa=aa+1    
  if aa != 4:
    print(aa,'A',ab,'B')
  if aa ==4:
    print('恭喜你答對了') 
    quit()
print('sorry沒機會了')