from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"

#testing with first page:
response = requests.get(URL_BASE + "page-1.html")
selector = Selector(text=response.text)

#getting href attribute from first element of the selector:
href = selector.css(".product_pod h3 a::attr(href)").get()
print(href)


#complete url:
print(URL_BASE + href)