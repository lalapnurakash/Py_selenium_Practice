import calendar
from datetime import date, datetime

import self
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://bdif.amf-france.org/en")
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH,"(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[1]").click()
#FRI 23 DEC 2022
n=datetime.today()
month=datetime.today().strftime("%a %Y %b %d")
tod=list[datetime.today().day, month, datetime.today().year]
act=""
print(month)




