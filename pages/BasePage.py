from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def do_click(self,  by_locator):
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def fromdateof(self,fromdate,by_locator):
       WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(fromdate)

    def todateof(self, todate, by_locator):
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(todate)

    def clickonindexof(self,list:list[WebElement],chooseindex):
        list.__getitem__(chooseindex).click()

