import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#@pytest.fixture(autouse=True)
# def chrome_driver(request):
#     ch_driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
#     request.cls.driver=ch_driver
#     yield
#     ch_driver.close()

num=153
temp=num
su=0
while temp>0:
    digit=temp%10
    cube=digit**3
    su+=cube
    temp//=10

if su==num:
    print("armstrong")