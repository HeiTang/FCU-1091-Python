x = eval(input('')) # 此行勿改
i = 12
n = []
while(i <= x):
    if(i % 5 != 0):
        n.append(i)
    i = i+6
if(x >= 6):
    print("6", end="")
for j in n:
    print(", " + str(j), end="")