from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time
import logging
import utilities.custom_logger as cl


class PreviewSupplierAuditWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _help_link = "Help"  # LINK TEXT
    _ok_btn = "TEMPLATE_CLONE_OK_PB"
    _cancel_btn = "TEMPLATE_CLONE_CANCEL"

    def click_ok_button(self):
        self.element_click(self._ok_btn)

    def click_cancel_button(self):
        self.element_click(self._ok_btn)

    """ MODULE CALLED BY TESTS """
    def close_preview_supplier_audit_window_ok(self):
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")))

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.click_ok_button()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

    def close_preview_supplier_audit_window_cancel(self):
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")))

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.click_cancel_button()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)
