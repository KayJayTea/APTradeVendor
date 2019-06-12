from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import os
import time


class SeleniumDriver:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def screenshot(self, result_message):
        """
        Takes screenshot of failed test
        :return:
        """
        file_name = result_message + "." + str(round(time.time() + 1000)) + ".png"
        screenshot_directory = "..\\screenshots\\"
        relative_filename = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except Exception as e:
            self.log.error(e)
            print_stack()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found with locator: " + locator + " and  locator_type: " + locator_type)
        except Exception as e:
            self.log.error(e)
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Get List of elements
        :param locator:
        :param locator_type:
        :return:
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator + " and locator type: " + locator_type)
        except Exception as e:
            self.log.error(e)

        return element

    def element_click(self, locator: object = "", locator_type: object = "id", element: object = None) -> object:
        """
        Either provide element or a combination of locator and locator_type
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:  # If locator is NOT empty (defined)
                element = self.get_element(locator, str(locator_type))
            element.click()
            self.log.info("Clicked on element with locator: " + str(locator) + " locator type: " + str(locator_type))
        except Exception as e:
            self.log.info(e)
            print_stack()

        return object

    def clear_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info("Cleared element with locator: " + locator + " locator_type: " + locator_type)
        except Exception as e:
            self.log.error(e)
            print_stack()

    def sendkeys(self, data, locator="", locator_type="id", element=None):
        """
        Either provide element or a combination of locator and locator_type
        :param data:
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locator type: " + locator_type)
        except Exception as e:
            self.log.error(e)
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except Exception as e:
            self.log.error(e)
            print_stack()
            text = None

        return text

    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Either provide element or a combination of locator and locator_type
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " and with locator type: " + locator_type)
                return True
            else:
                self.log.info("Element NOT present with locator: " + locator +
                              " and with locator type: " + locator_type)
                return False
        except Exception as e:
            self.log.error(e)
            print(e)

            return False

    def element_presence_check(self, locator, locator_type="id"):
        try:
            element_list = self.driver.find_elements(locator, locator_type)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except Exception as e:
            self.log.error(e)
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except Exception as e:
            self.log.error(e)
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")
