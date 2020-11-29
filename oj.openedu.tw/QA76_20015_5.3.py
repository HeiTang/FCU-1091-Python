def AB(s1,s2): # 此行勿改
    
    s1 = str(s1)
    s2 = str(s2)
    a = 0
    b = 0
    for i in range (len(s1)):
        for j in range (len(s2)):
            if (i == j and s1[i] == s2[j]):
                a += 1
                break
            elif (i != j and s1[i] == s2[j]):
                b += 1
                break            
    return a, b
            
# 以下程式勿改
s1,s2 = eval(input())
a, b = AB(s1, s2) 
print (a, b)