from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/home/eden/Development/chromedriver"

# connects selenium code to browser

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# search_bar = driver.find_element_by_id("id-search-field")
# print(search_bar.text)event-widget.last li")
article_count = driver.find_element_by_css_selector("#articlecount a").text
# article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]').text

search_bar = driver.find_element_by_name(name='search')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
print(article_count)
# entire program
# driver.quit()