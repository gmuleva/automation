from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
driver=webdriver.Firefox()
driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(5)
driver.get("https://www.google.com/search?client=ubuntu&channel=fs&q=youtube&ie=utf-8&oe=utf-8")
print(driver.title)
time.sleep(5)