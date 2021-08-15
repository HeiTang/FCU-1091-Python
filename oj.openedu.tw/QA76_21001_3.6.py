def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

v = int(input(''))# 此行勿改
n = 1
while(fib(n) < v):
    n = n + 1

print (n)# 此行勿改。