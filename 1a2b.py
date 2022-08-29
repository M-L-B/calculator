import random
import math
aa=0
ab=0
flag=0
while flag == 0:
  num=[0,0,0,0]
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
    if a != c:
      if a != d:
        if b != c:
          if b != d:
            if c != d:
              flag=1
print('歡迎來到游戲1a2b')
print('你有7次機會來猜出數字')
for n in range(7):
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
  if y > 9999:
    print('別想了，輸入在大也沒有用')
  if y == (15217002379):
    print('恭喜你答對了') 
    quit()
  if ga == a:
    aa=aa+1
  elif ga == b:
    ab=ab+1
  elif ga == c:
    ab=ab+1
  elif ga == d:
    ab=ab+1
  if gb == b:
    aa=aa+1
  elif gb == a:
    ab=ab+1
  elif gb == c:
    ab=ab+1
  elif gb == d:
    ab=ab+1
  if gc == c:
    aa=aa+1
  elif gc == a:
    ab=ab+1
  elif gc == b:
    ab=ab+1
  elif gc == d:
    ab=ab+1
  if gd == d:
    aa=aa+1   
  elif gd == a:
    ab=ab+1
  elif gd == b:
    ab=ab+1
  elif gd == c:
    ab=ab+1
  if aa != 4:
    print(aa,'A',ab,'B')
  if aa ==4:
    print('恭喜你答對了') 
    quit()
print('sorry沒機會了')
print(x)