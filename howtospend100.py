#soup:2,50;shampoo:15,6;teethbrush:5,20
i=1
for x in range (0,51):
  for y in range (0,7): 
    for z in range(0,21):
      a=(x,y,z)
      total=(x*2+y*15+z*5)
      if total==100:
        print(a,i)
        i=i+1