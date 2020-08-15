'''
@Gourav build first login project
'''
from selenium import webdriver

driver =webdriver.Firefox()

driver.get("https://demo.gyanstream.in")
print(driver.title)
driver.quit()
