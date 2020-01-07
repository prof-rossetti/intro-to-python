from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# INITIALIZE THE DRIVER
#

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver" # (or wherever yours is installed)

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

#
# NAVIGATE TO GOOGLE.COM...
#

driver.get("https://www.google.com/")
print(driver.title) #> Google
driver.save_screenshot("search_page.png")

#
# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//input[@title="Search"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)

#
# INTERACT WITH THE ELEMENT
#

search_term = "Prof Rossetti GitHub"
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
driver.save_screenshot("search_results.png")

#
# ALWAYS QUIT THE DRIVER
#

driver.quit()
