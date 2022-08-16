x=int(input('要輸出去第幾個斐波那契數列'))
def fibonacci (n):
  if n==1 or n==2:
    return 1
  else:
    return (fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(x))