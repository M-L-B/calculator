#找出一次函數式
x=float(input('請輸入你的點x1    '))
y=float(input('請輸入你的點y1    '))
xx=float(input('請輸入你的點x2    '))
yy=float(input('請輸入你的點y2    '))
print('這是你的兩個坐標點')
print('(',x,',',y,')')
print('(',xx,',',yy,')')
k=(yy-y)/(xx-x)
b=y-k*x
print('此一次函數式是','y=',k,'x+',b)