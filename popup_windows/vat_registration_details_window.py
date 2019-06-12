from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.util import Util
from random import randint

import utilities.custom_logger as cl
import logging


class VATRegistrationDetailsWindows(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # LOCATORS
    _help_link = "Help"  # LINK_TEXT
    _personalize_link = "Personalize"  # LINK_TEXT
    _find_link = "Find"  # LINK_TEXT
    _country = "VNDR_VAT_RGSTRN_COUNTRY$0"
    _vat_registration_id = "VNDR_VAT_RGSTRN_VAT_RGSTRN_ID$0"
    _ok_button = "#ICSave"
    _cancel_button = "#ICCancel"

    def enter_country(self):
        self.sendkeys(("LUX", Keys.TAB), self._country)
        self.util.sleep(2, "the Country to be recognized by the app.")

    def enter_vat_registration_id(self):
        random_number = randint(100000000000000, 999999999999999)
        self.sendkeys(random_number, self._vat_registration_id)
        self.util.sleep(2, "the VAT Registration ID, {}, to be recognized by the application.".format(random_number))

    def click_save_button(self):
        self.element_click(self._ok_button)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

    """ METHOD CALLED FROM IDENTIFYING INFO PAGE """

    def enter_vat_registration_details(self):
        self.enter_country()
        self.enter_vat_registration_id()
        self.click_save_button()
