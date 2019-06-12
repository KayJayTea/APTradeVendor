from base.base_page import BasePage
from faker import Faker
from random import randint
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.util import Util
from base.selenium_driver import SeleniumDriver
from popup_windows.supplier_attributes_window import SupplierAttributesWindow
from popup_windows.vat_registration_details_window import VATRegistrationDetailsWindows

import utilities.custom_logger as cl
import logging


class IdentifyingInformationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()
        self.wait = SeleniumDriver(self.driver)
        self.vat_reg_details = VATRegistrationDetailsWindows(self.driver)
        self.supplier_attr = SupplierAttributesWindow(self.driver)

    # LOCATORS
    _new_window_link = "New Window"  # LINK_TEXT
    _help_link = "Help"  # LINK_TEXT
    _personalize_page = "Personalize Page"  # LINK_TEXT
    _summary_tab = "//span[contains(text(), 'ummary')]"  # XPATH
    _address_tab = "//span[contains(text(), 'ddress')]"  # XPATH
    _contacts_tab = "//span[contains(text(), 'ontacts')]"  # XPATH
    _location_tab = "//span[contains(text(), 'ocation')]"  # XPATH
    _custom_tab = "//span[contains(text(), 'C')]"  # XPATH
    _supplier_name_txt = "VENDOR_NAME1"
    _supplier_short_name_txt = "VENDOR_VNDR_NAME_SHRT_USR"
    _additional_name = "VENDOR_NAME2"
    _classification_select = "VENDOR_VENDOR_CLASS"
    _withholding_checkbox = "VENDOR_WTHD_SW"
    _open_for_ordering_checkbox = "VENDOR_VNDR_STATUS_PO"
    _vat_registration_checkbox = "VENDOR_VAT_SW"
    _registration_link = "Registration"  # LINK_TEXT
    _collapse_all_button = "VNDR_MAINT_WRK_COLLAPSE_ALL_FLAG"
    _corporate_supplier_checkbox = "VNDR_MAINT_WRK_CORP_VNDR_FLG$21$"
    _corporate_supplier_id_text = "VENDOR_CORPORATE_VENDOR"
    _fei_trl_attributes_link = "FEI TRL Attributes"  # LINK_TEXT
    _additional_id_numbers_arrow = "VNDR_MAINT_WRK_VNDR_ID_PB"
    _additional_reporting_elements_arrow = "VNDR_MAINT_WRK_FPDS_INFO_PB"
    _customer_id = "VENDOR_CUST_ID"
    _id_type = "STD_ID_NUM_QUAL$0"
    _id_type2 = "STD_ID_NUM_QUAL$1"
    _id_type3 = "STD_ID_NUM_QUAL$2"
    _id_number = "STD_ID_NUM$0"
    _id_number2 = "STD_ID_NUM$1"
    _id_number3 = "STD_ID_NUM$2"
    _add_id_number_btn = "BUS_UNIT_IDS_AP$new$0$$0"
    _add_id_number_btn2 = "BUS_UNIT_IDS_AP$new$1$$0"
    _add_id_number_btn3 = "BUS_UNIT_IDS_AP$new$2$$0"
    """ ADDITIONAL REPORTING ELEMENTS """
    _common_parents_tin_text = "VNDR_RPT_ELEM_COMMON_PARENT_TIN$0"
    _type_of_contractor_select = "VNDR_RPT_ELEM_VNDR_TYPE$0"
    _sdb_program_select = "VNDR_RPT_ELEM_SMALL_DISADV$0"
    _other_preference_programs_select = "VNDR_RPT_ELEM_OTHER_PREF_PROG$0"
    _ethnicity_select = "VNDR_RPT_ELEM_ETHNICITY2$0"
    _common_parents_name_text = "VNDR_RPT_ELEM_COMMON_PARENT_NAME$0"
    _hub_zone_program_select = "VNDR_RPT_ELEM_HUBZONE_PROG$0"
    _size_of_small_business_select = "VNDR_RPT_ELEM_SMALL_BUS_SIZE$0"
    _vosb_select = "VNDR_RPT_ELEM_VETERAN_OWNED$0"
    _emerging_small_business_check = "VNDR_RPT_ELEM_EMERGING_SM_BUS$0"
    _woman_owned_business_check = "VNDR_RPT_ELEM_WOMEN_OWNED$0"
    _veteran_check = "VNDR_RPT_ELEM_VETERAN_FLG$0"
    _disabled = "VNDR_RPT_ELEM_DISABLED$0"

    def enter_supplier_name(self):
        fake_data = Faker()
        fake_company = fake_data.company()
        self.sendkeys("TEST_QA_{}".format(fake_company), self._supplier_name_txt)

    def enter_supplier_short_name(self):
        random_num = randint(999, 9999)
        self.sendkeys("QATST_" + (str(random_num)), self._supplier_short_name_txt)
        self.util.sleep(2, "the Supplier's Short Name to be recognized by the app.")

    def click_withholding_checkbox(self):
        self.sendkeys(Keys.TAB, self._supplier_short_name_txt)
        is_checked = self.driver.find_element(By.ID, self._withholding_checkbox).is_selected()
        if is_checked:
            print("Withholding checkbox is already selected")
        else:
            # self.element_click(self._withholding_checkbox, "id")
            # self.driver.find_element(By.ID, self._withholding_checkbox).click()
            self.sendkeys(Keys.SPACE, self._withholding_checkbox)
            print("Withholding checkbox selected")

    def click_open_for_ordering_checkbox(self):
        is_checked = self.driver.find_element(By.ID, self._open_for_ordering_checkbox).is_selected()
        if is_checked:
            print("Open for Ordering is already selected")
        else:
            # self.element_click(self._open_for_ordering_checkbox, "id")
            self.driver.find_element(By.ID, self._open_for_ordering_checkbox).click()
            print("Open for Ordering checkbox selected")

    def uncheck_open_for_ordering_checkbox(self):
        self.sendkeys(Keys.TAB, self._withholding_checkbox)
        is_checked = self.driver.find_element(By.ID, self._open_for_ordering_checkbox).is_selected()
        if is_checked:
            # self.driver.find_element(By.ID, self._open_for_ordering_checkbox).click()
            self.sendkeys(Keys.SPACE, self._open_for_ordering_checkbox)
            print("'Open for Ordering' checkbox UN-selected")
        else:
            print("'Open for Ordering' is already un-selected")

    def click_vat_registration_checkbox(self):
        is_checked = self.driver.find_element(By.ID, self._vat_registration_checkbox).is_selected()
        if is_checked:
            print("VAT Registration is already selected")
        else:
            self.sendkeys(Keys.TAB, self._open_for_ordering_checkbox)
            self.sendkeys(Keys.TAB, self._classification_select)
            self.sendkeys(Keys.SPACE, self._vat_registration_checkbox)
            print("VAT Registration checkbox selected")
        try:
            self.wait.element_presence_check(self._registration_link, "link")
        except Exception as e:
            print(e)

    def click_registration_link(self):
        self.element_click(self._registration_link, locator_type="link")
        self.util.sleep(1, "the active window to be recognized by the app.")
        self.driver.switch_to.default_content()
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

    def click_fei_trl_attr_link(self):
        self.element_click(self._fei_trl_attributes_link, locator_type="link")
        self.util.sleep(1, "the active window to be recognized by the app.")
        self.driver.switch_to.default_content()
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

    def expand_additional_id_numbers(self):
        self.element_click(self._additional_id_numbers_arrow)

    def enter_id_type_dns(self, id_type):
        self.sendkeys(id_type, self._id_type)

    def enter_dns_number(self):
        self.util.sleep(2, "the ID Type to be recognized by the app.")
        random_num = randint(100000000, 999999999)
        self.sendkeys(random_num, self._id_number)

    def enter_dns_info(self):
        self.enter_id_type_dns("DNS")
        self.element_click(self._id_number)
        self.enter_dns_number()

    def enter_id_type_tin(self, id_type):
        self.sendkeys(id_type, self._id_type2)

    def enter_tin_number(self):
        self.util.sleep(2, "the ID Type to be recognized by the app.")
        random_num = randint(100000000, 999999999)
        self.sendkeys(random_num, self._id_number2)

    def enter_tin_info(self):
        self.element_click(self._add_id_number_btn)
        self.enter_id_type_tin("TIN")
        self.element_click(self._id_number2)
        self.enter_tin_number()

    def enter_id_type_ssn(self, id_type):
        self.sendkeys(id_type, self._id_type3)

    def enter_ssn_number(self):
        self.util.sleep(2, "the ID Type to be recognized by the app.")
        random_num = randint(100000000, 999999999)
        self.sendkeys(random_num, self._id_number3)

    def enter_ssn_info(self):
        self.element_click(self._add_id_number_btn2)
        self.enter_id_type_ssn("SSN")
        self.element_click(self._id_number3)
        self.enter_ssn_number()

    def click_address_tab(self):
        self.element_click(self._address_tab, "xpath")
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "VNDR_ADDR_SCROL_DESCR$0")))

    def select_random_type_of_contractor(self):
        type_of_contractor = ["Domestic Contractor Outside US", "Educational Institution", "Foreign Contractor",
                              "Hospital", "JWOD Nonprofit Agency", "Large Business", "Minority Institution",
                              "Nonprofit Organization", "Other Small Business", "Reserved",
                              "Small Disadvantaged Business", "State/Local Government"]
        self.sendkeys(str(choice(type_of_contractor)), self._type_of_contractor_select)
        self.util.sleep(1, "the Type of Contractor to be recognized by PSFT.")

    def select_random_sdb_program(self):
        sdb_programs = ["8(a) Contract Award", "8(a) with HUBZone Priority", "Not Applicable",
                        "SDB Participating Program", "SDB Price Evaluation Adjust", "SDB Set-Aside"]

        self.sendkeys(str(choice(sdb_programs)), self._sdb_program_select)
        self.util.sleep(1, "the SDB Program to be recognized by PSFT.")

    def select_random_other_preference_program(self):
        other_preference_programs = ["Buy Indian", "Directed to JWOD Nonprofit", "No Preference/Not listed",
                                     "Small Business Set-Aside", "Very Small Business Set-Aside"]

        self.sendkeys(str(choice(other_preference_programs)), self._other_preference_programs_select)
        self.util.sleep(1, "the Other Preference Programs to be recognized by PSFT.")

    def select_random_ethnicity(self):
        ethnicities = ["African American", "Asian American", "Hispanic American", "Native American", "Other"]

        self.sendkeys(str(choice(ethnicities)), self._ethnicity_select)
        self.util.sleep(1, "the Ethnicity to be recognized by PSFT.")

    def select_random_hub_zone_program(self):
        hub_zone_programs = ["Combined HUBZone Price Adjust", "HUBZone Price Evaluation Pref", "HUBZone Set-Aside",
                             "HUBZone Sole Source", "Not Applicable"]

        self.sendkeys(str(choice(hub_zone_programs)), self._hub_zone_program_select)
        self.util.sleep(1, "the HUB Zone Program to be recognized by PSFT.")

    def select_random_size_of_small_business(self):
        sizes_of_small_businesses = ["A) 50 or less", "B) 51 - 100", "C) 101 - 250", "D) 251 - 500", "E) 501 - 750",
                                     "F) 751 - 1,000", "G) Over 1,000", "M) 1,000,000 or less",
                                     "N) 1,000,001 - 2,000,000", "P) 2,000,001 - 3,500,000", "R) 3,500,001 - 5,000,000",
                                     "S) 5,000,001 - 10,000,000", "T) 10,000,001 - 17,000,000", "Z) Over 17,000,000"]

        self.sendkeys(str(choice(sizes_of_small_businesses)), self._size_of_small_business_select)
        self.util.sleep(1, "the Size of Small Business to be recognized by PSFT.")

    def select_random_vosb(self):
        vosbs = ["Not Veteran Owned Sm Business", "Other Veteran Owned Sm Bus", "Service Disabled VOSB"]

        self.sendkeys(str(choice(vosbs)), self._vosb_select)
        self.util.sleep(1, "the Veteran Owned Small Business to be recognized by PSFT.")

    def click_women_owned_business_checkbox(self):
        wob_checkbox = self.driver.find_element(By.ID, self._woman_owned_business_check)
        wob_checkbox.click()

    def click_veteran_checkbox(self):
        veteran_checkbox = self.driver.find_element(By.ID, self._veteran_check)
        veteran_checkbox.click()

    """ SUPPLIER RELATIONSHIPS """

    def click_corporate_supplier_checkbox(self):
        self.sendkeys(Keys.TAB, self._collapse_all_button)
        is_checked = self.driver.find_element(By.ID, self._corporate_supplier_checkbox).is_selected()
        if is_checked:
            print("'Corporate Supplier' checkbox is already selected")
        else:
            # self.element_click(self._withholding_checkbox, "id")
            # self.driver.find_element(By.ID, self._withholding_checkbox).click()
            self.sendkeys(Keys.SPACE, self._corporate_supplier_checkbox)
            print("'Corporate Supplier' checkbox selected")

    def enter_parent_supplier(self, parent_id):
        self.click_corporate_supplier_checkbox()
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, self._corporate_supplier_id_text)))
        self.clear_element(self._corporate_supplier_id_text)
        self.sendkeys(parent_id, self._corporate_supplier_id_text)

    """ END SUPPLIER RELATIONSHIPS """

    def enter_additional_reporting_elements(self):
        self.element_click(self._additional_reporting_elements_arrow)
        self.wait.wait_for_element("VNDR_RPT_ELEM_COMMON_PARENT_TIN$0")
        self.select_random_type_of_contractor()
        self.select_random_sdb_program()
        self.select_random_other_preference_program()
        self.select_random_ethnicity()
        self.select_random_hub_zone_program()
        self.select_random_size_of_small_business()
        self.select_random_vosb()
        self.click_women_owned_business_checkbox()
        self.click_veteran_checkbox()

    """ THE MODULE THAT GETS CALLED BY THE TEST """
    def enter_identifying_info(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "VENDOR_NAME1")))
        self.enter_supplier_name()
        self.enter_supplier_short_name()

        # self.click_withholding_checkbox()
        # self.click_open_for_ordering_checkbox()
        # self.click_vat_registration_checkbox()
        # self.uncheck_open_for_ordering_checkbox()

        """ ENTER REGISTRATION INFORMATION """
        # self.click_registration_link()
        # self.vat_reg_details.enter_vat_registration_details()

        """ SELECT FEI Trl Attribute """
        # self.click_fei_trl_attr_link()
        # self.supplier_attr.select_yes_cvr()
        # self.supplier_attr.select_yes_mv_mfg_flag()
        # self.supplier_attr.select_yes_mv_vip_flag()
        # self.supplier_attr.select_random_type()
        # self.supplier_attr.select_yes_private_label()
        # self.supplier_attr.select_random_fei_vendor_class()
        # self.supplier_attr.enter_url()
        # self.supplier_attr.click_ok_button()

        """ SUPPLIER RELATIONSHIPS """
        # self.enter_parent_supplier("0003015038")

        # Expand Additional ID Numbers section
        self.expand_additional_id_numbers()
        self.enter_dns_info()
        # self.enter_tin_info()
        # self.enter_ssn_info()

        # self.enter_additional_reporting_elements()
