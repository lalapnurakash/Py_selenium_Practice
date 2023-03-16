***Setting***
Library  SeleniumLibrary
*** Variables ***




*** Test Cases ***
clickcheckbox
    Open browser   http://14.99.175.107:17656/3iBank/index.html   Chrome
    Set Selenium Speed    3
    Maximize Browser Window
    Set Browser Implicit Wait    3
    Input Text    id:username    vamsi
    Input Text    id:password    vamsi
    Input Text    id:card    1234
    Click Button    id:login_btn
    Set Browser Implicit Wait    4
    Click Element    xpath://li[@data-slide-to="0"]
    Sleep    1
    Click Element    xpath:(//button[@class="btn btn-primary agree-form"])[1]
    Scroll Element Into View    id:myCheck
    Select Checkbox    myCheck
    Click Button    accept_agree
    Set Browser Implicit Wait    5
    Click Element    xpath:(//input[@name='gender'])[1]
    Close Browser



*** Keywords ***

