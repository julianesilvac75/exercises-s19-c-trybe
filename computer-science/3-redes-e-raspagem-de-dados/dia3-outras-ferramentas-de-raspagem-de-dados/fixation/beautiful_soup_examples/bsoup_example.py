import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
page = requests.get(url)
html_content = page.text

# Cria uma instância do objeto Beautiful Soup e usa o parser de HTML nativo
# do Python
soup = BeautifulSoup(html_content, "html.parser")

# acessando a tag "title"
title = soup.title

# retorna o elemento HTML da tag
print(title)

# o tipo de "title" eh tag
print(type(title))

# o nome de "title" eh title
print(title.name)

# acessando a tag "footer"
footer = soup.footer

# acessando o atributo classe da tag footer
print(footer['class'])

# Utiliza o método prettify para melhorar a visualização do conteúdo
# print(soup.prettify())