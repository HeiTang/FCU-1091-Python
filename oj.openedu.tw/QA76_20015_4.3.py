names = input().split()
eng = eval(input())
math = eval(input())
phy = eval(input())
# 以上勿改

g_pass = []
for i in range(len(names)):
    ave = (eng[i] + math[i] + phy[i])/3
    if(ave >= 60):
        g_pass.append(names[i]) 

# 以下勿改， g_pass 是有通過的學生的 list
print (' '.join(g_pass)) 