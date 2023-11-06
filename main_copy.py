import requests
import json

import sys

sys.path.insert(0, 'bs4.zip')
from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price
    html1 = requests.get(product_laughs).content
    laughs_soup = BeautifulSoup(html1, 'html.parser')
    price_laughs = float(laughs_soup.find("span", attrs={"class": "regular-price"}).text.strip()[3:])
    product_name_laughs = laughs_soup.find("div", attrs={"class": "product-name"}).text.strip()
    # TODO: LaughsSuper supermarket website provides the price in a span text.
    html2 = requests.get(product_glomark).content
    glomark_soup = BeautifulSoup(html2, 'html.parser')
    price_glomark = float(
        json.loads(glomark_soup.find("script", attrs={"type": "application/ld+json"}).text.strip())["offers"][0][
            "price"])
    product_name_glomark = json.loads(glomark_soup.find("script", attrs={"type": "application/ld+json"}).text.strip())[
        "name"]

    # TODO: Glomark supermarket website provides the data in jason format in an inline script.
    # You can use the json module to extract only the price

    # TODO: Parse the values as floats, and print them.

    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if (price_laughs > price_glomark):
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif (price_laughs < price_glomark):
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')


product_laughs = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
product_glomark = 'https://glomark.lk/coconut/p/11624'
compare_prices = (product_laughs, product_glomark)
