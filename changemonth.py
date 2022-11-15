num=str(input('你想要輸入的正整數'))
num_length=(len(num))
#n=修改次數
n=0
x=num.split('-')
day=x[1]
day_int=int(day)
month=x[0]
month_int=int(month)
month_int=int(x[0])
month_2=month_int%10
if month_int > 12:
    n=n+1
if month_2==0 or month_2==1 or month_2==2 or month_2==3 or month_2==5 or month_2==7 or month_2==8:
    if day_int > 31:
      n=n+1
if month_2==4 or month_2==6 or month_2==9:
    if day_int > 30:
      n=n+1
print(n)
