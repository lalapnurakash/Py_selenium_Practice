import time

import pandas
import requests
import self
import xlrd
import xlsxwriter
import xlwt as xlwt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(3)
tags =driver.find_elements(By.TAG_NAME,"a")
filename="C:\\Users\\1003633\\PycharmProjects\\selenium_demo\\filesdir\\excelsheet.xlsx"

book=xlsxwriter.Workbook(filename)
sheet = book.add_worksheet("Sheet1")

row=column=0
try:
 for tag in tags:
    link=tag.get_attribute("href")
    print(link)
    sheet.write(row,column,str(link))
    sheet.set_column(column,column)
    row=row+1
    print(row)
    print(requests.get(link))
except Exception as e:
  book.close()
time.sleep(2)
wk=xlrd.open_workbook(filename)
sh=wk.sheet_by_name("Sheet1")
s=sh.cell_value(0,0)
print(s)