from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

time.sleep(5)

driver.switch_to_alert().dismiss()
driver.find_element

driver.close()