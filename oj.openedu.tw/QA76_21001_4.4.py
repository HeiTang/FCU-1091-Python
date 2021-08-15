names = input().split()
eng = eval(input())
math = eval(input())
phy = eval(input())
# 以上勿改
eng_sum = sum(eng)
math_sum = sum(math)
phy_sum = sum(phy)

g_good = []

eng_ave = eng_sum/len(eng)
math_ave = math_sum/len(eng)
phy_ave = phy_sum/len(eng)


for i in range(len(names)):
    if(eng[i] > eng_ave and math[i] > math_ave and phy[i] > phy_ave):
        g_good.append(names[i]) 

# 以下勿改， g_pass 是有通過的學生的 list
print (' '.join(g_good)) 