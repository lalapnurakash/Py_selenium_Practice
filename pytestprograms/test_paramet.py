import unittest

import pytest
from selenium.webdriver.common.by import By

from pytestprograms.conftest import chrome_driver


# @pytest.mark.usefixtures("chrome_driver")
# class base_chrome_test():
#     pass

# class Testbase(base_chrome_test):
#     @pytest.mark.parametrize("username,password",[("aksh",1133),("akh",123),("ksh",113)])
#     def test_loginto(self,username,password):
#         self.driver.get("http://www.google.com")
#         self.driver.findElement(By.ID,"q").sendKeys(username)

# for AUTOTUNE
class Testbase():
    @pytest.mark.parametrize("username,password",[("aksh",1133),("akh",123),("ksh",113)])
    def test_loginto(self,username,password):
        self.driver.get("http://www.google.com")
        self.driver.findElement(By.ID,"q").sendKeys(username)

