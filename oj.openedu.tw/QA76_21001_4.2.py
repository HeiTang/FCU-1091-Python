c = input().split() 
city = input().split()
# 以上勿改

hot_city = []
for i in c:
    degree_f = int(i) * 1.8 +32 
    if(degree_f > 100):
        num = c.index(str(i))
        hot_city.append(city[num])

# 以下勿改
for hc in hot_city:
   print(hc)