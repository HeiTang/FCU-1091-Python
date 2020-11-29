import json
health = json.loads(input())
# 以上區塊勿改，使用 health 來設計程式碼

Name = []
BMI = []

for key in health.keys():
    Name.append(key)
    
    a = health.get(key)
    height = a.get("height")
    weight = a.get("weight")

    bmi = weight / pow((height/100),2)
    BMI.append(bmi)

Index = BMI.index(max(BMI))
print(Name[Index])