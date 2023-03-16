*** Settings ***
Library    SeleniumLibrary
#Library   SeleniumLibrary   plugins=${CURDIR}/MyPlugin.py
#Library   SeleniumLibrary   plugins=plugins.MyPlugin, plugins.MyOtherPlugin

*** Variables ***
${appurl}  http://14.99.175.107:17656/3iBank/index.html
${browname}  Chrome
*** Test Cases ***
keywordstst
    ${pgt}= launchbrowser   ${appurl}  ${browname}
    Log To Console  ${pgt}


*** Keywords ***
launchbrowser
   [Arguments]  ${browurl}  ${browser}
   Open Browser  ${browurl}   ${browser}
   Set Browser Implicit Wait    4
   Maximize Browser Window

    ${title}=Get Title
   [Return]  ${title}



