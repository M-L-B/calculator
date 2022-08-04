print('這個功能可以告訴你這是不是一個11的倍數')
wish=float(input('你的數'))
check=wish%11
if check == 0:
  answer=('這是11的倍數')
if check != 0:
  answer=('這不是11的倍數')
print(answer)