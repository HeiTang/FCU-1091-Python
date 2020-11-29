# Partial Accepted

import math
import json
rank = json.loads(input()) 	# 一群人對一群電影的喜歡程度
p = input()			      # 某人的姓名
# 以上區塊勿改

def recommend(rank, p):
    flag = ""
    result = -1
    tmp = 0

    for i in rank:
        if (i != p):
            tmp = 0
            for j in rank[p]:
                tmp += ( rank[p][j] - rank[i][j] ) ** 2
            tmp = tmp ** 0.5
            if (result > tmp or result == -1):
                result = tmp
                flag = i
    
    result = 0
    key = ""
    for i in rank[flag]:
        if (i not in rank[p]):
            if (result < rank[flag][i]):
                result = rank[flag][i]
                key = i
    return key
            
    # 找出喜好最接近 p 的人，假設為 q
    # 找出 q 喜好的影片列表 like_list，從高到低排序，若喜好程度相同
    #    ，則以電影名字母由小到大排序
    # 從 like_list 中找 p 還沒有評價的電影且評價大於等於4的，假設為 m
    # return m

m = recommend(rank, p)
print (m)