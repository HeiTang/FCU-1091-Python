tall_list = input().split(',') 
new_tall = eval(input())
new_list = []
# 以上勿改

new_list.extend(tall_list)
new_list = list(map(int, new_list))
new_list.append(new_tall)
new_list.sort()

# 以下勿改
for h in new_list:
  print(h, end=' ')