h, w = eval(input('')) # 此行勿改。h, w 分別表示身高與體重
BMI = w / pow(h/100, 2)

if(BMI < 18.5):
    r = "underweight"
elif(BMI <= 24):
    r = "normal"
else:
    r = "overweight"
print (r) # 此行勿改，r 為輸出之答案