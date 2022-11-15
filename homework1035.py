#n<(1+1/2+1/3+......1+n)
n=float(input('輸入一個整數'))
a=0.0
x=0.0
while a<n:
    x=x+1
    a=a+1/x
print(x)