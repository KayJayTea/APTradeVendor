from base.base_page import BasePage
from base.base_page import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.util import Util

import utilities.custom_logger as cl
import logging


class FindExistingValuePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()
        self.wait = SeleniumDriver(self.driver)

    """ Unless otherwise noted, locator_type is 'ID' """
    # LOCATORS
    _new_window_link = "New Window"  # LINK_TEXT
    _help_link = "Help"  # LINK_TEXT
    _keyword_search_tab = "ICTAB_1"
    _add_new_value_tab = "ICTAB_2"
    _supplier_id_txt = "VENDOR_AP_VW_VENDOR_ID"
    _persistence_select = "VENDOR_AP_VW_VENDOR_PERSISTENCE"
    _short_supplier_name_txt = "VENDOR_AP_VW_VENDOR_NAME_SHORT"
    _our_customer_number_txt = "VENDOR_AP_VW_AR_NUM"
    _supplier_name = "VENDOR_AP_VW_NAME1"
    _search_btn = "#ICSearch"
    _return_to_search_btn = "#ICList"
    _clear_btn = "#ICClear"
    _basic_search_link = "Basic Search"  # LINK_TEXT
    _save_search_criteria_link = "Save Search Criteria"  # LINK_TEXT
    _find_existing_value_link = "Find an Existing Value"  # LINK_TEXT
    _keyword_search_link = "Keyword Search"  # LINK_TEXT
    _add_new_value_link = "Add a New Value"  # LINK_TEXT

    def click_add_new_value_tab(self):
        self.element_click(self._add_new_value_tab)

    def enter_supplier_id(self, supplier_id):
        self.sendkeys(supplier_id, self._supplier_id_txt)

    def click_search_btn(self):
        self.element_click(self._search_btn)
        wait = WebDriverWait(self.driver, 30, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Last Modified By')]")))

    """ MODULES CALLED BY TEST SCRIPTS """
    def add_a_new_value(self):
        self.driver.switch_to.frame("ptifrmtgtframe")
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, self._add_new_value_tab)))
        self.click_add_new_value_tab()

    def search_for_supplier(self, master_vendor_id):
        self.enter_supplier_id(master_vendor_id)
        print("Supplier ID: {}".format(master_vendor_id))

        self.click_search_btn()
