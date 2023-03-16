import os
import shutil
from datetime import date, timedelta
from time import sleep

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fileutils.Handlefiles import file

today = date.today()
date = today - timedelta(days=1)
yesterday = date.strftime("%d/%m/%Y")

destination="C://Users//1003633//"+date.strftime("%d-%m-%Y")
curr_dir="C:\\Users\\1003633\\files"

def createfile(self, directory):
    # if file exists remove and recreate
    if os.path.exists(directory):
        shutil.rmtree(directory)
        os.makedirs(directory)
    else:
        os.makedirs(directory)
        print("file created")
createfile(curr_dir)
createfile(destination)
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
driver.implicitly_wait(6)
sleep(4)
#driver.get_cookies ()
driver.find_element(By.XPATH,'//button[@class="tarteaucitronCTAButton tarteaucitronAllow"]').click()
# day

driver.find_element(By.XPATH, "//input[@id='dateDebut']").send_keys(yesterday)
driver.find_element(By.ID, 'dateFin').send_keys(yesterday)
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
   driver.execute_script("window.scrollBy(0, 90)")
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

