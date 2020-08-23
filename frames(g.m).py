




from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
time.sleep(5)

driver.switch_to.frame("packageListFrame")

driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to_default_content()

driver.switch_to.frame("packageFrame")

driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to_default_content()
time.sleep(3)

driver.switch_to_frame("classFrame")

driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()

driver.close()