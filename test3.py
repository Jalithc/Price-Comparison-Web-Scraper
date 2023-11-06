import requests
from bs4 import BeautifulSoup
import json

url = "https://glomark.lk/coconut/p/11624"
page = requests.get(url).content

soup = BeautifulSoup(page, "html.parser")
name = json.loads(soup.find("script", type="application/ld+json").text.strip())["name"]

print(name)