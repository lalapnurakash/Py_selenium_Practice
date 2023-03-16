from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser():
    def chromeSetup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        s = Service(executable_path="D:\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=s)
        return driver

