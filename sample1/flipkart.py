import time

import self
from Tools.scripts.generate_opcode_h import footer
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# driver.maximize_window()
#
driver.get("https://www.globalsqa.com/demo-site/sliders/")
time.sleep(5)
scroll_origin = ScrollOrigin.from_element(header, 0, -50)
ActionChains(driver) \
    .scroll_from_origin(scroll_origin, 0, 200) \
    .perform()
while True:
 i=0
 driver.switch_to.frame(4)

 blueslider=driver.find_element(By.XPATH, '(//span[@tabindex="0"])[1]')
 print(blueslider.location)
 break
 i+=1





