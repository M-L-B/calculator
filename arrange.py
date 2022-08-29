def bubble(num):
    leng=len(num)
    while leng-1>0:
      i=1
      while i<=leng-1 :
        if(num[i]<num[i-1]):
          num[i],num[i-1]=num[i-1],num[i]
        i+=1
      leng-=1
    return num
list=input('輸入一個list')
num=list.split()
list1=[]
for x in range (len(num)):
  list1.append(int(num[x]))
bubble(list1)
print(list1)