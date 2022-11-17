from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
selector = Selector(text=response.text)

#get description:
description = selector.css("#product_description ~ p::text").get()
# print(description)

#slice the description by removing the suffix:
suffix = "...more"
if description.endswith(suffix):
    description = description[:-len(suffix)]
print(description)

# response = requests.get("http://books.toscrape.com/")
# selector = Selector(text=response.text)

# #get all prices from first page:
# prices = selector.css(".product_price .price_color::text").re(r"£\d+\.\d{2}")
# # print(prices)




# URL_BASE = "http://books.toscrape.com/catalogue/"

# #testing with first page:
# response = requests.get(URL_BASE + "page-1.html")
# selector = Selector(text=response.text)

# #getting href attribute from first element of the selector:
# href = selector.css(".product_pod h3 a::attr(href)").get()
# detail_page_url = URL_BASE + href


# #get detail page content:
# detail_response = requests.get(detail_page_url)
# detail_selector = Selector(text=detail_response.text)

# #get product description:
# # ~ is sibling tag
# description = detail_selector.css("#product_description ~ p::text").get()
# print(description)
