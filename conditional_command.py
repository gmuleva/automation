from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
driver.get("http://demo.gyanstream.in/")
mail_ele=driver.find_element_by_xpath('//*[@id="basic_email"]')
mail_ele.send_keys('hcmuleva@gmail.com')
pwd_ele=driver.find_element_by_xpath('//*[@id="basic_password"]')
pwd_ele.send_keys('welcome123')
login_ele=driver.find_element_by_xpath('/html/body/div/div/form/div[4]/div/div/div/button').click()
#ele=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/i').click()
l#ogout_ele=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/div/div[1]').click()
#lg_ele=driver.find_element_by_xpath('/html/body/div[9]/div/[1]/div/div[2]/div/div/div/div[4]/div/div[1]').click()





