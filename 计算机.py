from datetime import datetime
from fractions import Fraction
import random
from unicodedata import east_asian_width
print('你想進行什麽運算')
for x in range(5):
  print('1.+,2.-,3.*,4./,5.根號,6.平方,7.立方,8.x的几次方,9.查詢日期,10.一元二次方程')
  print('11.二元一次方程,12.隨機數,13.判斷是否是直角三角形,14算出直角三角形的第三邊')
  print('15.平均值,16.溫度轉換,17.放鬆的金字塔,18.一個數的倍數,19.河内塔,20.斐波那契數列')
  oper=input('21.11的倍數')
  if oper == '1':
    number1=float(input('你想輸入什麽數字'))
    number2=float(input('你想輸入什麽數字'))
    if number1 > 600 or number2 > 600:
      print("你輸入的數過大啦")
      answer=("error")
    else:
      answer=(number1+number2)
  if oper == '2': 
    number1=float(input('你想輸入什麽數字'))
    number2=float(input('你想輸入什麽數字'))
    answer=(number1-number2) 
    if number1 > 600 or number2 > 600:
      print("你輸入的數過大啦")
      answer=("error")
    else:
      answer=(number1+number2)
  if oper == '3':
    number1=float(input('你想輸入"什麽數字'))
    number2=float(input('你想輸入什麽數字'))
    answer=(number1*number2)
    if number1 > 600 or number2 > 600:
      print("你輸入的數過大啦")
      answer=("error")
    else:
      answer=(number1+number2)
  if oper == '4':
    number1=float(input('你想輸入什麽數字'))
    number2=float(input('你想輸入什麽數字'))
    answer=(number1/number2)
    if number1 > 600 or number2 > 600:
      print("你輸入的數過大啦")
      answer=("error")
    else:
      answer=(number1+number2)
  if oper == '5':
    number1=float(input('你想輸入什麽數字'))
    answer=(number1**0.5)
  if oper == '6':
    number1=float(input('你想輸入什麽數字'))
    answer=(number1**2)
  if oper == '7':
    number1=float(input('你想輸入什麽數字'))
    answer=(number1**3)
  if oper == '8':
    number1=float(input('你想輸入什麽數字'))
    number2=float(input('你想輸入什麽數字'))
    answer=(number1**number2)
  if oper == '9':
    userwish=input('從現在到x,x,x還有多少天,請輸入x,x,x')
    nowdate=datetime.now()
    year,month,day=map(int,userwish.split(','))
    date=datetime(year,month,day)
    answer=(date-nowdate)
  if oper == '10':
    print('你可以輸入你的方程式')
    print('如,ax**2 運算方式+bx 運算方式+c=答案')
    a=float(input('你的a等於什麽'))
    b=float(input('你的b等於什麽'))
    c=float(input('你的c等於什麽,如果不要常數項請輸入0'))
    answera=float(input('你的答案等於什麽'))
    sac=4*a*c
    bdpf=b**2
    kghn=bdpf-sac
    kghh=kghn**0.5
    fzj=-b+kghn
    fm=2*a
    answer1=fzj/fm
    fzj=-b-kghn
    answer2=fzj/fm
    answer=(answer1,answer2)
  if oper == '11':
    print('你可以輸入你的方程式')
    print('如,ax 運算方式+by=答案a')
    print('cx  運算方式+dy=答案b')
    a=float(input('你的a等於什麽'))
    b=float(input('你的b等於什麽'))
    answera=float(input('你的答案a等於什麽'))
    c=float(input('你的c等於什麽'))
    d=float(input('你的d等於什麽'))
    answerb=float(input('你的答案b等於什麽'))
    answer1=(a*d-b*c)
    answer2=(answera*d-b*answerb)
    answer3=(a*answerb-answera*c)
    x=Fraction(answer2/answer1)
    y=Fraction(answer3/answer1)
    answer=x , y
  if oper == '12':
    answer=0
    while answer < 40:
      answer=(random.random()*50)
      if answer < 40:
        print("%.2f" % answer)
  if oper == '13':
    a=float(input('你的短邊等於什麽'))
    b=float(input('你的長邊等於什麽'))
    c=float(input('你的斜邊等於什麽'))
    adpf=(a**2)
    bdpf=(b**2)
    cdpf=(c**2)
    ajb=(adpf+bdpf)
    if ajb == cdpf:
      answer=('這是直角三角形')
      print(a*b*0.5,'這是面積')
    if ajb > cdpf:
      answer=('這是銳角三角形')
    if ajb < cdpf:
      answer=('這是鈍角三角形')
  if oper == '14':
    print('warning!')
    print('要執行此程序需要已知直角三角形的兩條邊')
    print('不知道的請輸入0')
    a=float(input('你的短邊等於什麽'))
    b=float(input('你的長邊等於什麽'))
    c=float(input('你的斜邊等於什麽'))
    if a == 0:
      answer=(c**2-b**2)**0.5
    if b == 0:
      answer=(c**2-a**2)**0.5
    if c == 0:
      chl=(a**2+b**2)**0.5
      mj=a*b/2
      print('前面是c的長度後面是面積')
      answer=(chl,mj)
  if oper == '15':
    n=int(input('你有多少個數要輸入'))
    sum=0.0
    for i in range(n):
      x=float(input('輸入你的數字'))
      sum=sum+x
    answer=sum/n 
  if oper == '16':
    want=input('f to c/c to f')
    if want == 'f to c':
      f=float(input('?華氏度'))
      first=f+40
      second=first/1.8
      answer=second-40
    if want == 'c to f':
      c=float(input('?攝氏度'))
      first=c+40
      second=first*1.8
      answer=second-40
  if oper == '17':
    n=4
    for x in range(1,2*n,2):
      for y in range (x):
        print('*',end='')
      print(' ')
    for x in range (2*n-3,-1,-2):
      for y in range (x):  
        print('*',end='')
      print(' ')
  if oper == '18':
    print('這個功能可以告訴你a是不是b的倍數')
    a=float(input('你的a'))
    b=float(input('你的b'))
    check=a%b
    if check == 0:
      answer=(a,'是',b,'的倍數')
    if check != 0:
      answer=(a,'不是',b,'的倍數')
  if oper == '19':
    step=float(input('你想有一個幾層河内塔'))
    n=2**step-1
    f=float(input('你每秒能移動幾個圓盤'))
    t=n/f
    if t > 31536000:
      ht=t/31536000
      print("%.2f" % ht)
      answer=('你需要',ht,'年')
    if t > 2592000:
      ht=t/2592000
      print("%.2f" % ht)
      answer=('你需要',ht,'月')
    if t > 86400:
      ht=t/86400
      print("%.2f" % ht)
      answer=('你需要',ht,'天')
    if t > 3600:
      ht=t/3600
      print("%.2f" % ht)
      answer=('你需要',ht,'小時')
    if t > 60:
      ht=t/60
      print("%.2f" % ht)
      answer=('你需要',ht,'分鐘')
    if t > 1:
      ht=t/1
      print("%.2f" % ht)
      answer=('你需要',ht,'秒')
  if oper == '20':
    n=int(input('要輸出去第幾個斐波那契數列'))
    a,b=1,1
    for x in range (n-2):
      c=a
      a=b
      b=c+b
    answer=b
  if (oper != '17') and (oper != '18') and (oper != '19'):
    print("%.2f" % answer)
  else:
    if oper != '17': 
      print(answer)