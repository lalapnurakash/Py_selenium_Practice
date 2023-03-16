*** Settings ***
Library  SeleniumLibrary
Library    XML





*** Variables ***
${browser}  Chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login



*** Test Cases ***
LoginTest
    #   Create Webdriver      Chrome   executable_path=D:\drivers\chromedriver.exe
   Open Browser   ${url}    ${browser}
   Maximize Browser Window
   Set Browser Implicit Wait    8
   ${"username"}    Set Variable  name:username
   Sleep    3
   Element Should Be Visible  ${"username"}
   Element Should Be Enabled  ${"username"}

   Input Text   ${"username"}   Admin
   Sleep    3
   Clear Element Text   ${"username"}
   Sleep    3
   Input Text   ${"username"}   Admin
   Input Text    name:password   admin123
   Click Button   //button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
   Close Browser




*** Keywords ***
