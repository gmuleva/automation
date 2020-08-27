from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Firefox()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

xyz=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(xyz)




drp.select_by_visible_text('Morning')
time.sleep(5)
drp.select_by_index(2)
time.sleep(5)

print(len(drp.options))

all_options=drp.options

for option in all_options:
    print(option.text)

driver.close()





