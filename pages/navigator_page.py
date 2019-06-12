from base.base_page import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class NavigatePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = SeleniumDriver(self.driver)

    # LOCATORS
    _navbar_btn = "PT_NAVBAR"
    _navigator_link = "//*[@id='PTNB$PTNUI_NB_MENU']"  # XPATH
    _suppliers_link = "Suppliers"  # LINK_TEXT
    _supplier_info_link = "Supplier Information"  # LINK_TEXT
    _add_update_link = "Add/Update"  # LINK_TEXT
    _supplier_link = "Supplier"  # LINK_TEXT

    """ code to do stuff """
    def click_navbar_btn(self):
        self.element_click(self._navbar_btn)
        self.util.sleep(2, "the 'NavBar' menu to open.")

    def click_navigator(self):
        self.element_click(self._navigator_link, "xpath")
        self.util.sleep(2, "the 'Navigator' menu to open.")

    def click_suppliers(self):
        self.element_click(self._suppliers_link, "link")

    def click_supplier_info(self):
        self.element_click(self._supplier_info_link, "link")

    def click_add_update(self):
        self.element_click(self._add_update_link, "link")

    def click_supplier(self):
        self.element_click(self._supplier_link, "link")

    def navigate_to_supplier_info(self):
        self.click_navbar_btn()
        self.driver.switch_to.frame("psNavBarIFrame")
        self.util.sleep(2, "the application to focus on the new iFrame")
        self.click_navigator()
        self.click_suppliers()
        self.click_supplier_info()
        self.click_add_update()
        self.click_supplier()
        # self.driver.switch_to.frame("ptifrmtgtframe")
