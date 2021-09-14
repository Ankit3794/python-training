from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Waiter:
    wait_time = 20
    time_out = 40
    polling_time = 500

    def __init__(self, driver: webdriver):
        self.driver = driver

    def wait_for_element_visibility(self, element):
        return WebDriverWait(self.driver, self.time_out, self.polling_time, ignored_exceptions=None).until(
            expected_conditions.visibility_of(element))
