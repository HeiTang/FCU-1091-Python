# -*- coding: UTF-8 -*-
import requests, json
from bs4 import BeautifulSoup

station = {
    "北屯總站": "0afa3027-e0cd-43a2-902b-c3081efd3b27",
    "舊社": "9396045b-31bb-4135-96ad-0b5040bd4aeb",
    "松竹": "8cbc2661-c30e-417e-bfe5-69c7fd559f77",
    "四維國小": "95ea9819-79c6-4069-bee9-80e09f9ceb75",
    "文心崇德": "080ccba5-84e9-4b23-9800-84a68fa614f7",
    "文心中清": "f911489b-497e-45ef-bafa-2876083b8458",
    "文華高中": "4f85d84b-06d9-40de-a2d3-c9c54f58119a",
    "文心櫻花": "17e62fc0-7e3f-42a8-80ce-c597136e6f99",
    "市政府": "82361949-b015-4435-aab6-75166d4b5681",
    "水安宮": "6f55e961-4add-4b24-82ba-d477d47c771a",
    "文心森林公園": "52c7f0f6-47b2-4341-bcb8-6485aeab0279",
    "南屯": "04daa9f4-d7d2-4099-8b90-a9f77ca7c201",
    "豐樂公園": "c089d378-8398-4d04-9efa-3aeaa73ed5f2",
    "大慶": "a4c466b9-9cca-4b27-8be1-5734134aa4c8",
    "九張犁": "0f61a447-86c5-4bdd-9282-aab066e1acfc",
    "九德": "34b7d9a2-228f-4c84-a969-72a7cfda0a82",
    "烏日": "d2da6396-1db1-484e-8c4e-9eae063dcf88",
    "高鐵臺中站": "6b0c61b9-4b22-4332-8483-db4a0828cedc"
}

# StartSiteName = input("Please Input Start Station：")
# StopSiteName = input("Please Input End Station：")

StartSiteName = "北屯總站"
StopSiteName = "高鐵臺中站"

StartValue = station[StartSiteName]
StopValue = station[StopSiteName]

url = "https://www.tmrt.com.tw/api/public/FareTime/" + StartValue + "?stop=" + StopValue

r = requests.get(url)
r = r.text
r = json.loads(r)

GeneralFare = r['GeneralFare']
ElectronicFare = r['ElectronicFare']
RespectFare = r['RespectFare']
SpendTime = r['SpendTime']

print("起站：{StartSiteName} －> 訖站：{StopSiteName}".format(StartSiteName = StartSiteName , StopSiteName = StopSiteName))
print("單程票票價：{GeneralFare} 元".format(GeneralFare = GeneralFare))
print("電子票證：{ElectronicFare} 元".format(ElectronicFare = ElectronicFare))
print("敬老卡、愛心卡、愛心陪伴卡：{RespectFare} 元".format(RespectFare = RespectFare))
print("乘車時間：{SpendTime} 分鐘".format(SpendTime = SpendTime))
