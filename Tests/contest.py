import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.usefixtures('driver_init')
class base_ch_Test:
  @pytest.fixture()
  def driver_init(self,request):
    ch_driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    request.cls.driver=ch_driver
    ch_driver.maximize_window()
    yield
    ch_driver.close()





