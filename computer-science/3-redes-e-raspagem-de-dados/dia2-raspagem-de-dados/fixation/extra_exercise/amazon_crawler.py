import requests
from parsel import Selector


URL_BASE = "https://www.amazon.co.uk/s?k=blenders+for+kitchen&crid=DPVTVL2HNS1K&sprefix=blender%2Caps%2C62&ref=nb_sb_ss_ts-doa-p_2_7"

response = requests.get(URL_BASE)
selector = Selector(text=response.text)
product_css = "div.a-section.a-spacing-small.a-spacing-top-small"
products_list = []

for product in selector.css(product_css):
    product_name = product.css("span.a-size-medium.a-color-base.a-text-normal::text").get()
    # product_url = product.css(".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal::attr(href)").get()
    # print(type(product_url))
    price_whole = product.css("span.a-price-whole::text").get()
    price_fraction = product.css("span.a-price-fraction::text").get()
    total_price = f"£{price_whole}.{price_fraction}"
    product = {
        "name": product_name,
        "price": total_price
        # "url": "https://www.amazon.co.uk" + product_url,
    }
    
    products_list.append(product)


print(products_list[-1])

prices = selector.css("span.a-price-whole::text").getall()

# print(prices)