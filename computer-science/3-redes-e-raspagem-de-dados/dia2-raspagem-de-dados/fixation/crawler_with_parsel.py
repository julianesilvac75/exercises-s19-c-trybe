import requests
from parsel import Selector


URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = "page-1.html"

while next_page_url:
    #get first page content:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)

    #print products from a specific page:
    for product in selector.css(".product_pod"):
        #get title and price:
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").re(r"£\d+\.\d{2}")
        print(title, price)

        #get product detail url:
        detail_href = product.css("h3 a::attr(href)").get()
        detail_page_url = URL_BASE + detail_href

        #get detail page content:
        detail_response = requests.get(detail_page_url)
        detail_selector = Selector(text=detail_response.text)

        #get product description:
        description = detail_selector.css("#product_description ~ p::text").get()
        suffix = "...more"
        if description.endswith(suffix):
            description = description[:-len(suffix)]
        print(description)

    next_page_url = selector.css(".next a::attr(href)").get()

# URL = "http://books.toscrape.com/"

# response = requests.get(URL)
# selector = Selector(text=response.text)
# thumbnail_url_selector = "div.image_container a::attr(href)"

# for url in selector.css(thumbnail_url_selector).getall():
#     thumbnail_request = requests.get(URL + url)
#     thumbnail_selector = Selector(text=thumbnail_request.text)
#     book_title = thumbnail_selector.css("div.product_main h1")
#     # print(book_title.get())


# next_page_url = selector.css(".next a::attr(href)").get()
# print(next_page_url)

# for thumbnail in selector.css("img.thumbnail").getall():
#     print(thumbnail)
