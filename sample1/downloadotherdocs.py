import os
import shutil
from datetime import date, timedelta

import self
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait
from fileutils.Handlefiles import file

today = date.today()
date = today - timedelta(days=1)
yesterday = date.strftime("%d/%m/%Y")

directory="C://Users//1003633//morefiles"
curr_dir="C:\\Users\\1003633\\files"

s=file()
s.createfile(curr_dir)
s.createfile(directory)

sleep(2)

#making custom download dir

options = webdriver.ChromeOptions()
pref={"download.default_directory": curr_dir}
options.add_experimental_option("prefs",pref)

options.add_experimental_option("detach", True)
s = Service(executable_path="D:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get("https://bdif.amf-france.org/en")
driver.implicitly_wait(20)
sleep(7)
driver.find_element(By.XPATH,'//button[@class="tarteaucitronCTAButton tarteaucitronAllow"]').click()
#ActionChains(driver).move_to_element(coockie).click().perform()
# day

driver.find_element(By.XPATH, "//input[@id='dateDebut']").send_keys(yesterday)
driver.find_element(By.ID, 'dateFin').send_keys(yesterday)

sleep(3)
menuoptns = driver.find_elements(By.XPATH, "(//button[@class='mat-button-toggle-button mat-focus-indicator'])")

for opt in menuoptns[1:5]:
    opt.click()
bttnsearch=driver.find_element(By.XPATH, "//div[@class='col-xs-12 research-button']/button")
action=ActionChains(driver)
action.move_to_element(bttnsearch).perform()
bttnsearch.click()
sleep(4)
#list of results to download
driver.execute_script("window.scrollBy(0, 400)")

results=driver.find_elements(By.XPATH,"//li[@class='ng-star-inserted']/descendant::button")
count=0
def download(nolist,start=0):
  global count
  lastpos=len(nolist)
  print("downloading filesdir")

  for result in nolist[start:lastpos]:
     driver.execute_script("window.scrollBy(0, 100)")
     sleep(1)
     ActionChains(driver).scroll_to_element(result)
     result.click()
     count+=1
     print(count)
     if((driver.find_elements(By.XPATH,"//button[contains(@class,'little-rounded -gray mat-menu')]").__len__())>1):
       downoptn=driver.find_elements(By.XPATH, "//button[contains(@class,'little-rounded -gray mat-menu')]")
       iter(downoptn).__next__().click()
       count += 1
       sleep(2)
       print(count)
       # for eachopt in downoptn:
       #     eachopt.click()
       #     result.click()
       #     sleep(2)
       # if(downoptn.index(eachopt)==len(downoptn)-1):
       ActionChains(driver).move_by_offset(0,0).click()
     else:
      sleep(3)
#starting from 1st recrd to download
download(results)
seemorebtn=driver.find_element(By.XPATH,"//button[@class='more-results']")
#if more records avauilable
if(seemorebtn.is_displayed()):
    seemorebtn.click()
    sleep(4)
    print("seemoreclick")
    pausefrm=len(results)
    results1 = driver.find_elements(By.XPATH, "//li[@class='ng-star-inserted']/descendant::button")
    download(results1,pausefrm)

for file_name in os.listdir(curr_dir):
        src_path = os.path.join(curr_dir,file_name)
        dst_path = os.path.join(directory,file_name)
        shutil.move(src_path,dst_path)

for f in os.listdir(curr_dir):
      os.remove(os.path.join(curr_dir, f))

