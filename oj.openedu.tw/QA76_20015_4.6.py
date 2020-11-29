# By HeiTang (Partial Accepted)

c1 = input().split(' ')  # 此行勿改
c2 = input().split(' ')  # 此行勿改
c3 = input().split(' ')  # 此行勿改

cSUM = c1 + c2 + c3
a0 = []
a1 = []
a2 = []
a3 = []

dict = {'s1':0, 's2':0, 's3':0, 's4':0, 's5':0, 's6':0, 's7':0, 's8':0, 's9':0, 's10':0}
for key in cSUM:
    dict[key] = dict.get(key, 0) + 1

for key in dict.keys():
    if(dict.get(key, 0) == 0):
        a0.append(key)
    if(dict.get(key, 0) == 1):
        a1.append(key)
    if(dict.get(key, 0) == 2):
        a2.append(key)
    if(dict.get(key, 0) == 3):
        a3.append(key)

for i in a0,a1,a2,a3:
    if(i): print(' '.join(i))
    else: print("-")

# 奶綠 (Accepted)

c1 = input().split(' ')  # 此行勿改
c2 = input().split(' ')  # 此行勿改
c3 = input().split(' ')  # 此行勿改
c4=[]
# 印出時請注意格式，避免有多餘的空格
# Write Your Code
c4.extend(c1)
c4.extend(c2)
c4.extend(c3)
c5 = set(c4)
total = {"s1","s2","s3","s4","s5","s6","s7","s8","s9","s10"}
tt = total - c5
tt1 = list(tt)
a=[]
b=[]
f=[]
d=[]
for key in c5:
    if c4.count(key) == 1:
        b1= key
        b.append(b1)
        b.sort()
        b.sort(key=lambda ele:len(ele))
    if c4.count(key) == 2:
        f1= key
        f.append(f1)
        f.sort()
        f.sort(key=lambda ele:len(ele))
    if c4.count(key) == 3:
        d1= key
        d.append(d1)
        d.sort()
        d.sort(key=lambda ele:len(ele))
for key2 in tt:
    if tt1.count(key2) == 1:
        a1= key2
        a.append(a1)
        a.sort()
        a.sort(key=lambda ele:len(ele))
if(len(a) == 0):
    a.insert(0,"-")
if(len(b) == 0):
    b.insert(0,"-")
if(len(f) == 0):
    f.insert(0,"-")
if(len(d) == 0):
    d.insert(0,"-")
print (' '.join(a))
print (' '.join(b))
print (' '.join(f))
print (' '.join(d))