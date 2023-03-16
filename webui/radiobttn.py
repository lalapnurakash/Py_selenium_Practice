import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://demoqa.com/radio-button")
bttns=driver.find_elements(By.XPATH,"//label[@class='custom-control-label']")

bttns[0].click()
bttns[0].is_selected()

select=Select()
