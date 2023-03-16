import os
import shutil
import time
from datetime import date, timedelta
from threading import Thread
from time import sleep

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import fileutils
from fileutils import *

today = date.today()
date = today - timedelta(days=1)
yesterday = date.strftime("%d/%m/%Y")

destination="C://Users//1003633//"+date.strftime("%d-%m-%Y")
curr_dir="C:\\Users\\1003633\\files"
s=fileutils.Handlefiles.file()
s.createfile(curr_dir)
s.createfile(destination)

sleep(2)

#making custom download d
options = webdriver.ChromeOptions()
pref={"download.default_directory": curr_dir}
options.add_experimental_option("prefs",pref)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()
driver.get("https://bdif.amf-france.org/en")
driver.implicitly_wait(20)
sleep(4)

driver.find_element(By.XPATH,'//button[@class="tarteaucitronCTAButton tarteaucitronAllow"]').click()

sleep(3)
driver.find_element(By.XPATH,"(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[1]").click()

li=driver.find_elements(By.XPATH,"//td[@class='mat-calendar-body-cell-container ng-star-inserted']/button")
previousday=(today.day)-1
d=str(previousday)
for each in li:
    tex=each.find_element(By.TAG_NAME,"div").text.strip()
    if tex == d:
      print("selected date from:", tex)
      each.click()
      break
sleep(3)
driver.find_element(By.XPATH,"//div[@class='mat-form-field-suffix ng-tns-c56-2 ng-star-inserted']//button").click()
#driver.find_element(By.XPATH,"(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[2]").click()
li1=driver.find_elements(By.XPATH,"//td[@class='mat-calendar-body-cell-container ng-star-inserted']/button/div[1]")

for each1 in li1:
    tex1 = each1.text.strip()
    if  tex1==d:
        print("selected date to:",tex1)
        each1.click()
        break

sleep(3)

driver.find_element(By.XPATH, "(//span[@class='mat-button-toggle-label-content'])[6]").click()

bttnsearch=driver.find_element(By.XPATH, "//div[@class='col-xs-12 research-button']/button")
action=ActionChains(driver)
#driver.execute_script("arguments[0].scrollIntoView();", bttnsearch)
action.move_to_element(bttnsearch).perform()
bttnsearch.click()
#
sleep(3)
resultlist = driver.find_elements(By.XPATH, '//ul[@class="h_fullWidth ng-star-inserted"]/li')
print(len(resultlist))
i = 0
for each in resultlist:
   i=i+1
   action.move_to_element(each)
   driver.execute_script("window.scrollBy(0, 100)")
   sleep(1)
   each.find_element(By.TAG_NAME,"button").click()
   sleep(1)
   print(i,end=" ")

sleep(4)

for file_name in os.listdir(curr_dir):
        src_path = os.path.join(curr_dir,file_name)
        dst_path = os.path.join(destination,file_name)
        shutil.move(src_path,dst_path)
for f in os.listdir(curr_dir):
      os.remove(os.path.join(curr_dir, f))

