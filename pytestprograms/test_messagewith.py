from time import sleep
from typing import Any

import pywhatkit
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from self import self
from webdriver_manager.chrome import ChromeDriverManager

driver = None

def setUpModule():
    global driver
    options = webdriver.ChromeOptions

    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)
    sleep(4)
    driver.get("https://www.google.com")

def tearDownModule():
    driver.quit()
def test_googletitle():
    assert driver.title=="Google"