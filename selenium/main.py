from selenium import webdriver
chrome_driver_path = "/home/eden/Development/chromedriver"

# connects selenium code to browser

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://www.python.org/")
# search_bar = driver.find_element_by_id("id-search-field")
# print(search_bar.text)event-widget.last li")

upcoming_events_table = driver.find_elements_by_css_selector(".event-widget li")
upcoming_events = {}
for e in upcoming_events_table:
    index = upcoming_events_table.index(e)
    event = e.find_element_by_tag_name('a').text
    date = e.find_element_by_tag_name('time').text
    upcoming_events[index] = {'time': date, 'name': event}
# Closes one tab
driver.close()
print(upcoming_events)

# entire program
driver.quit()