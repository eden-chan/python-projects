from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/home/eden/Development/chromedriver"

# connects selenium code to browser

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name('fName')
fname.send_keys("Bob")

lname = driver.find_element_by_name('lName')
lname.send_keys('Ross')

email=driver.find_element_by_name('email')
email.send_keys('bobross@gmail.com')

submit = driver.find_element_by_css_selector(".btn-block")
submit.click()

# entire program
# driver.quit()