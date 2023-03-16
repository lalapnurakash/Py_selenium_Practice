from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class Homepage(BasePage):

    fromele=(By.XPATH, "//input[@id='dateDebut']")
    toele=(By.ID, 'dateFin')
    docoptions=(By.XPATH, "(//button[@class='mat-button-toggle-button mat-focus-indicator'])")
    searchbttn=(By.XPATH, "//div[@class='col-xs-12 research-button']/button")
    acceptcoockie=(By.XPATH, '//button[@class="tarteaucitronCTAButton tarteaucitronAllow"]')
    listofresults= (By.XPATH, "//li[@class='ng-star-inserted']/descendant::button")
    seemorebtn = (By.XPATH, "//button[@class='more-results']")

    def  __init__(self,driver):
        super(Homepage, self).__init__(driver)
        driver.get("https://bdif.amf-france.org/en")
    def selectfrom(self,fromdate):
         self.fromdateof(fromdate,self.fromele)
    def selectto(self,todate):
        self.todateof(todate,self.toele)





