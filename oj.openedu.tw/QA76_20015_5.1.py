def max(a, b, c):
    meow = []
    meow.append(a)
    meow.append(b)
    meow.append(c)
    meow.sort()
    return meow[-1]

# 以下勿改
x = eval(input())
y = eval(input())
z = eval(input())

r = max(x, y, z) 
print (r)