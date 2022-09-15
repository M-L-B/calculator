def cocktail(num):
    leng=len(num)
    i=1
    while leng/2+1>i :
      j=0
      while j < leng-2*i+1:
        if(num[j+i-1]>num[j+i]):
            num[j+i-1],num[j+i]=num[j+i],num[j+i-1]
        j+=1
        print(num,i,j)
        print('--')
      j=0
      while j<leng-2*i:
        if(num[int(leng-j-i-2)]>num[leng-j-i-1]):
            num[int(leng-j-i-2)],num[leng-j-i-1]=num[leng-j-i-1],num[int(leng-j-i-2)]
        j+=1
      i+=1
      print(num,i,j)
    return num
list=input('輸入一個list')
num=list.split()
list1=[]
for x in range (len(num)):
  list1.append(int(num[x]))
print(list1,'last')
cocktail(list1)
print(list1)