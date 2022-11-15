from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"

#testing with first page:
response = requests.get(URL_BASE + "page-1.html")
selector = Selector(text=response.text)

#getting href attribute from first element of the selector:
href = selector.css(".product_pod h3 a::attr(href)").get()
detail_page_url = URL_BASE + href


#get detail page content:
detail_response = requests.get(detail_page_url)
detail_selector = Selector(text=detail_response.text)

#get product description:
# ~ is sibling tag
description = detail_selector.css("#product_description ~ p::text").get()
print(description)
