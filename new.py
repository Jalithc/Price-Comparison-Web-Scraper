import requests
from bs4 import BeautifulSoup

url = "https://scrape-sm1.github.io/site1/COCONUT%20market1super.html"
page = requests.get(url).content

soup = BeautifulSoup(page, "html.parser")
price = float(soup.find("span", class_="regular-price").text.strip()[3:])
print(price)