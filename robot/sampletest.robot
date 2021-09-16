*** Settings ***
Library           SeleniumLibrary
Library           BuiltIn
Test Setup  Setup Browser

*** Variables ***
${APP URL}      https://google.com
${SEARCH STRING}      Selenium with python

*** Keywords ***
Setup Browser
    Create Webdriver    Chrome    executable_path=./chromedriver.exe
    Go To   ${APP URL}
    Maximize Browser Window

*** Test Cases ***
Google Search
    Input Text  name:q  ${SEARCH STRING}
    Submit Form
    ${ACTUAL_SEARCH}    Get Element Attribute   name:q  value
    should be equal  ${SEARCH STRING}    ${ACTUAL_SEARCH}
    [Teardown]    Close Browser

Open Gmail
    Click Link  xpath://a[text()='Gmail']
    ${TITLE}    Get Title
    should contain   ${TITLE}   Gmail
    [Teardown]    Close Browser
