from base.base_page import BasePage
from faker import Faker
from random import choice
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import utilities.custom_logger as cl
import logging


class SupplierAttributesWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _cvr_select = "WG_VNDR_ATTRIB_WG_MV_CVR_FLAG$0"
    _excl_frm_select = "WG_VNDR_ATTRIB_WG_MV_EXCL_FLAG$0"
    _mv_mfg_flag = "WG_VNDR_ATTRIB_WG_MV_MFG_FLAG$0"
    _mv_vip_flag = "WG_VNDR_ATTRIB_WG_MV_VIPFLAG$0"
    _type_select = "WG_VNDR_ATTRIB_VENDOR_TYPE$0"
    _private_label = "WG_VNDR_ATTRIB_WG_PRIVATE_LABEL$0"
    _fei_vendor_class = "WG_VNDR_ATTRIB_WG_VENDOR_CLASS_CD$0"
    _url = "WG_VNDR_ATTRIB_WG_TRL_URL$0"
    _ok_button = "#ICSave"
    _cancel_button = "#ICCancel"

    def select_yes_cvr(self):
        cvr_yes = Select(self.driver.find_element(By.ID, self._cvr_select))
        cvr_yes.select_by_value('Y')

    def select_yes_excl_frm(self):
        excl_frm_yes = Select(self.driver.find_element(By.ID, self._excl_frm_select))
        excl_frm_yes.select_by_value('Y')

    def select_yes_mv_mfg_flag(self):
        mv_mfg_flag_yes = Select(self.driver.find_element(By.ID, self._mv_mfg_flag))
        mv_mfg_flag_yes.select_by_value('Y')

    def select_yes_mv_vip_flag(self):
        mv_vip_flag_yes = Select(self.driver.find_element(By.ID, self._mv_vip_flag))
        mv_vip_flag_yes.select_by_value('Y')

    def select_random_type(self):
        supplier_attribute_type = [
            "Lighting",
            "Tool",
            # "PVF",
            # "PLB-R",
            "WSYS",
            "Waterworks",
            "BUILD",
            "H/C",
            "Electric",
            "Irrigation",
            # "MILL",
            "Industrial",
            "Chemicals"
        ]
        self.sendkeys(str(choice(supplier_attribute_type)), self._type_select)

    def select_yes_private_label(self):
        private_label_yes = Select(self.driver.find_element(By.ID, self._private_label))
        private_label_yes.select_by_value('Y')

    def select_fei_vendor_class(self, text):
        vendor_class = Select(self.driver.find_element(By.ID, self._fei_vendor_class))
        vendor_class.select_by_visible_text(text)

    def select_random_fei_vendor_class(self):
        vendor_classes = ["Approved", "PREF", "STRATEGIC", "UnApproved"]
        self.sendkeys(str(choice(vendor_classes)), self._fei_vendor_class)

    def enter_url(self):
        fake_url = Faker()
        fake_url = fake_url.url(schemes=None)

        self.clear_element(self._url)
        self.sendkeys(fake_url, self._url)
        self.util.sleep(2, "the URL, {}, to be recognized by the application.".format(fake_url))

    def click_ok_button(self):
        self.element_click(self._ok_button)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.util.sleep(2, "")
