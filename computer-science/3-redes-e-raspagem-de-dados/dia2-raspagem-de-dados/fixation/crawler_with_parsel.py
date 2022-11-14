import requests
from parsel import Selector

URL = "http://books.toscrape.com/"

response = requests.get(URL)

selector = Selector(text=response.text)
# print(selector.css("img.thumbnail").getall())

for thumbnail in selector.css("img.thumbnail").getall():
    print(thumbnail)
