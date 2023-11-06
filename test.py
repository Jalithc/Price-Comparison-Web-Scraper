import requests
from bs4 import BeautifulSoup

base_url = "https://scrape-sm1.github.io/site1/COCONUT%20market1super.html"
base_page = requests.get(base_url).content

soup_1 = BeautifulSoup(base_page, "html.parser")
name = soup_1.find("div", class_="product-name").text.strip()
print(name)


