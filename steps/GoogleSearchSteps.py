from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.actions import WebDriverActions

driver: webdriver
actions: WebDriverActions


@given(u'User is on Google home page')
def step_impl(context):
    global driver
    global actions
    driver = webdriver.Chrome(ChromeDriverManager().install())
    actions = WebDriverActions(driver)
    driver.maximize_window()
    driver.get("https://www.google.co.in")


@when(u'user enters "{search_string}" as search string')
def step_impl(context, search_string):
    searchField = driver.find_element_by_name("q")
    actions.type(searchField, search_string)
    searchField.submit()


@when(u'submit the form')
def step_impl(context):
    driver.find_element_by_name("q").submit()


@then(u'validate search')
def step_impl(context):
    assert driver.find_element_by_name("q").get_attribute('value') == 'Selenium with Python'


@then(u'close browser')
def step_impl(context):
    driver.close()
    driver.quit()
