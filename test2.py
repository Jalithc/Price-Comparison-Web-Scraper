import requests
from bs4 import BeautifulSoup
import json

url = "https://glomark.lk/coconut/p/11624"
page = requests.get(url).content

soup = BeautifulSoup(page, "html.parser")
price = float(json.loads(soup.find("script", type="application/ld+json").text.strip())["offers"][0]["price"])

print(price)

print('Product at Laughs:', product_name_laughs)
print('Price at Laughs: Rs.', price_laughs)
print('Product at Glomark:', product_name_glomark)
print('Price at Glomark: Rs.', price_glomark)