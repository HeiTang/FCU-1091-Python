a = int(input('')) # 此行勿改，a 為第一個格子的米數量
sum = t = 0
while(sum <= 10000):
    sum = sum + a
    a = a * 2
    t = t + 1
print (t) # 此行勿改，t 為輸出之答案