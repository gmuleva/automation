from selenium import webdriver
import time
def getDriver():
    driver =webdriver.Firefox()
    return driver
def getLoginPage(driver,url):
  driver.get(url)



driver =getDriver()
getLoginPage(driver,"https://demo.gyanstream.in")
time.sleep(5)
print(driver.title)
driver.back()
getLoginPage(driver,"https://www.google.com/search?client=ubuntu&channel=fs&q=facebook&ie=utf-8&oe=utf-8")
time.sleep(5)
print(driver.title)
driver.close()