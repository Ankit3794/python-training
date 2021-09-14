from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from utils.waitutil import Waiter


class WebDriverActions:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = Waiter(driver)

    def type(self, element: WebElement, value):
        self.wait.wait_for_element_visibility(element)
        element.send_keys(value)

    def click(self, element: WebElement):
        self.wait.wait_for_element_visibility(element)
        element.click()

    def _capture_screenshot(self, name):
        self.driver.get_screenshot_as_file(name)