from base.base_page import BasePage

import utilities.custom_logger as cl
from utilities.util import Util
import logging
import time


class SupplierInformationANV(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    """ Unless otherwise noted, locator type is ID"""
    # LOCATORS
    _new_window_link = "New Window"  # LINK_TEXT
    _help_link = "Help"  # LINK_TEXT
    _find_existing_value_tab = "ICTAB_0"
    _keyword_search_tab = "ICTAB_1"
    _set_id_field = "VENDOR_ADD_VW_SETID"
    _supplier_id_field = "VENDOR_ADD_VW_VENDOR_ID"
    _persistence_select = "VENDOR_ADD_VW_VENDOR_PERSISTENCE"
    _add_button = "#ICSearch"

    def click_add_button(self):
        self.util.sleep(2, "the [Add] button to be visible.")
        self.element_click(self._add_button)
