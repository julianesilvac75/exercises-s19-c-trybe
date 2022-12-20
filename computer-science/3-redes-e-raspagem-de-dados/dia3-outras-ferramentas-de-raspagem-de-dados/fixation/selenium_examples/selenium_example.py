from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()

response = firefox.get("https://www.google.com.br")

#search in the open instance for the first occurrence with the name "q"

search_input = firefox.find_element("name", "q")

# write "selenium" inside the search field
search_input.send_keys("selenium")

#press enter to search
search_input.send_keys(Keys.ENTER)