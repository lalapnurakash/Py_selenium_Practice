***Settings***
Library   SeleniumLibrary

***Variables***


***Test cases***
acceptalerts

   Open Browser   https://demoqa.com/alerts   Chrome
   Delete All Cookies

   Maximize Browser Window

   Set Browser Implicit Wait    5
   Wait Until Page Contains    Alerts
   Click Button   alertButton
   Handle Alert   accept

    Click Button   confirmButton
    Handle Alert  dismiss
    #Input Text Into Alert    text






*** Keywords ***