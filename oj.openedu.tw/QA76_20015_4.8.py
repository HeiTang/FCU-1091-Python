import json
myDic = json.loads(input()) 
ch = input()  # 要查詢的中文字


for English, Chinese in myDic.items():
    if Chinese == ch:
        print(English)