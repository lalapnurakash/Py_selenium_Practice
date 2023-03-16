import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]').click()
driver.find_element(By.XPATH,"//input[@class='_3704LK']").send_keys("dell")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='_3704LK']").send_keys(keys.Keys.DOWN,Keys.DOWN,Keys.DOWN)
dire:WebElement=driver.find_element(By.XPATH,'//a[@class="_2XoPFN"]')
driver.execute_script("arguments[0].scrollIntoView()",dire)
ActionChains(driver).scroll_to_element(driver.find_element(By.XPATH,'//a[@class="_2XoPFN"]')).perform()

