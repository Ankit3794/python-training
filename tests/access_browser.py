import json

from selenium import webdriver
from utils.CustomLogger import CustomLogger
from webdriver_manager.chrome import ChromeDriverManager

from utils.actions import WebDriverActions
import unittest

data = json.load(open(r"data/settings.json"))


class GoogleSearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.actions = WebDriverActions(self.driver)
        self.driver.maximize_window()
        self.driver.get(data["url"])

    def test_search(self):
        searchField = self.driver.find_element_by_name("q")
        searchString = "Selenium with Python"
        self.actions.type(searchField, searchString)
        searchField.submit()
        CustomLogger().write_message_debug("debug submitted")
        CustomLogger().write_message_info("info submitted")
        CustomLogger().write_message_error("error submitted")
        CustomLogger().write_message_critical("critical submitted")
        CustomLogger().write_message_warning("warning submitted")
        self.assertEqual(self.driver.find_element_by_name("q").get_attribute('value'), searchString)

    def test_gmail(self):
        gmailLink = self.driver.find_element_by_xpath("//a[text()='Gmail']")
        gmailLink.click()
        CustomLogger().write_message_debug("Clicked Gmail Link")
        self.assertTrue('Gmail' in self.driver.title)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
