from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import logging
import random
import utilities.custom_logger as cl

""" GLOBAL VARIABLES """
PROCUREMENT_OPTIONS = ["COD", "N10TH", "N15TH", "N20TH", "N25TH", "N30TH", "N5TH", "N7DAY", "NET10", "NET15", "NET20",
                       "NET25", "NET30", "NET45", "NET60", "NET75", "NET90"]


class ProcurementOptionsWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _help_link = "Help"  # LINK TEXT
    _expand_all_button = "VNDR_MAINT_WRK_EXPAND_ALL_FLAG"
    _collapse_all_button = "VNDR_MAINT_WRK_COLLAPSE_ALL_FLAG"
    _ordering_address = "VENDOR_LOC_ADDR_SEQ_NUM_ORDR$17$"
    _returning_address = "VENDOR_LOC_RET_ADDR_SEQ_NUM$32$"
    _ship_from_address = "VENDOR_LOC_ADDR_SEQ_NUM_SHFR$94$"
    _additional_proc_options_arrow = "VNDR_LOC_WRK1_PROC_OPT_PB"
    _payment_terms_id_field = "VENDOR_LOC_PYMNT_TERMS_CD"
    _ok_btn = "#ICSave"

    """ DO SOMETHING WITH ELEMENT """
    def change_ordering_address(self, address_num):
        self.driver.find_element(By.ID, self._ordering_address).clear()
        self.sendkeys((address_num, Keys.TAB), self._ordering_address)
        self.util.sleep(2, "the address number, {}, to be recognized by the application.".format(address_num))

    def change_returning_address(self, address_num):
        self.driver.find_element(By.ID, self._returning_address).clear()
        self.sendkeys((address_num, Keys.TAB), self._returning_address)
        self.util.sleep(2, "the address number, {}, to be recognized by the application.".format(address_num))

    def change_ship_from_address(self, address_num):
        self.driver.find_element(By.ID, self._ship_from_address).clear()
        self.sendkeys((address_num, Keys.TAB), self._ship_from_address)
        self.util.sleep(2, "the address number, {}, to be recognized by the application.".format(address_num))

    def expand_additional_procurement_options(self):
        self.element_click(self._additional_proc_options_arrow)

    def enter_payment_terms_id(self, pmnt_terms):
        self.sendkeys((pmnt_terms, Keys.TAB), self._payment_terms_id_field)

    def click_ok_button(self):
        self.element_click(self._ok_btn)

    """ THIS IS THE MODULE THAT IS CALLED BY THE TEST """
    def select_payment_terms_id(self, pmnt_terms):
        self.expand_additional_procurement_options()
        self.enter_payment_terms_id(pmnt_terms)
        self.click_ok_button()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

    def select_random_payment_terms_id(self):
        number_of_accounts = 1
        random_account = random.choices(population=PROCUREMENT_OPTIONS, k=number_of_accounts)
        self.expand_additional_procurement_options()
        self.sendkeys(random_account, self._payment_terms_id_field)
        self.sendkeys(Keys.TAB, self._payment_terms_id_field)
        self.util.sleep(2, "the account, {}, to be recognized by the application.".format(random_account))
        self.click_ok_button()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)
