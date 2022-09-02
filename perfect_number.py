for n in range (10000000000):
  y=0
  for x in range (1,n,1):
    if n%x==0:
      y=y+x
  if n==y:
    print('perfect!!!',n)