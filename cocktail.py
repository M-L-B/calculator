def cocktail(num):
    leng=len(num)
    while leng/2-1>0:
      i=1
      j=0
      while j<leng-2*i+1 :
        if(num[i]<num[i-1]):
            num[i],num[i-1]=num[i-1],num[i]
        print(num)
        j+=1
      print('--')
      j=0
      while j<leng-2*i:
        if(num[int(leng-i-1)]<num[leng-i]):
            num[int(leng-i-1)],num[leng-i]=num[leng-i],num[int(leng-i-1)]
        print(num)
        j+=1
      i+=1
    return num
list=input('輸入一個list')
num=list.split()
list1=[]
for x in range (len(num)):
  list1.append(int(num[x]))
cocktail(list1)
print(list1)