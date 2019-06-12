"""
Base page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
this should not be used by creating object instances

Example:
        Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class

        returns:
            None
        :param driver:
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_to_verify):
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except Exception as e:
            self.log.error("Failed to get page title")
            print(e)
            return False
