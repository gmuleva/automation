from selenium import webdriver
from selenium.webdriver.commo

driver=webdriver.Firefox()

driver.get("http://demo.automationtesting.in/Windows.html")

dr
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
driver.quit()


