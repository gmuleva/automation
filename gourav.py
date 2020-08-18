from selenium import webdriver

driver=webdriver.Firefox()



driver.get("https://www.expedia.com/")

driver.find_element(BY.ID,"/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/figure/div[3]/div/div/div/ul/li[2]/a").click()

time.sleep(2)


driver.close()

