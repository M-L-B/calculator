def toh(n,A,B,C):
    if n==1:
      print('Disk 1 from',A,'to',B)
      return
    toh(n-1,A,C,B)
    print('Disk',n,'from',A,'to',B)
    toh(n-1,C,B,A)
toh(3,'A','B','C')