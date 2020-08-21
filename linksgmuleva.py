from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("http://facebook.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    print(link.text)

driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()

driver.close()