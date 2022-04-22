import requests
from bs4 import BeautifulSoup
import json


#url = "https://studyinrussia.ru/cn/life-in-russia/discover-russia/towns/"
#
#возвращаем резульат работы метода get библиотеки requests, первый параматер url к окторму мы обращаемся
# передадим заголовки
#
#headers = {
#    "accept": "*/*",
#    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
#}
#
#req = requests.get(url, headers=headers)
#src = req.text
#print(src)
#
# with open("index.html", "w") as file:
#    file.write(src)
count = 1
with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_cities_hrefs = soup.find_all(class_="section-learn-russia__link")

all_cities_dict = {}
for item in all_cities_hrefs:
    item_text = item.text
    item_href = "https://studyinrussia.ru" + item.get("href")
    print(f"{item_text}: {item_href}")

    all_cities_dict[item_text + str(count)] = item_href
    count = count+1

with open("all_cities_dict.json", "w") as file:
    json.dump(all_cities_dict, file, indent=4, ensure_ascii=False)