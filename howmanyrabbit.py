m1,m2,m3=1,0,0
x=int(input('你想要有多少個月'))
for n in range (x-1):
  m3=m3+m2
  m2=m1
  m1=m3
print('有',((m1+m2+m3)*2),'只兔子')