from base.base_page import BasePage
from base.selenium_driver import SeleniumDriver
from faker import Faker
from random import randint
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from pages.identifying_information_page import IdentifyingInformationPage
from popup_windows.look_up_state_window import LookUpStateWindow
from popup_windows.look_up_country_window import LookUpCountryWindow
from utilities.util import Util

import utilities.custom_logger as cl
import logging
import time

STATE_ABBR = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE",
              "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY",
              "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC",
              "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR",
              "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VI",
              "VT", "WA", "WI", "WV", "WY"]

GBR_COUNTIES = [
    "ANS", "ANT", "ARD", "ARM", "AYR", "BEDS", "BERKS", "BFS", "BLA", "BLY", "BNB", "BORDER", "BRIST", "BUCKS", "CAMBS",
    "CENT", "CFK", "CGV", "CHES", "CHL IS", "CKT", "CLR", "CLV", "CLWYD", "CNWLL", "CSR", "CUMB", "D&G", "DERBY",
    "DEVON", "DGN", "DORSET", "DOW", "DRY", "DUR", "DYFED", "E YORK", "E.SUSX", "ESSEX", "FER", "FIFE", "GLOUCS",
    "GRAMP", "GT LON", "GT MAN", "GWENT", "GWYND", "HANTS", "HERTS", "HFORD", "HIGHLD", "INV", "IOM", "IOS", "IOW",
    "KENT", "LANCS", "LEICS", "LINCS", "LMV", "LOTH", "LRN", "LSB", "M GLAM", "MDDSX", "MERYSD", "MFT", "MOR", "MYL",
    "N YORK", "NDN", "NHANTS", "NORFLK", "NOTTS", "NTA", "NTHUMB", "NYM", "OMH", "ORK", "OXON", "PER", "POWYS",
    "RUTLND", "S GLAM", "SEL", "SHET", "SHROPS", "SOMER", "STAFFS", "STB", "STI", "STRATH", "SUFFK", "SURREY", "SYORKS",
    "T&W", "TAYS", "W GLAM", "W ISLS", "W SUSX", "WARWKS", "WILTS", "WOR", "WSTMID", "WYORKS"
]


class AddressPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()
        self.check = SeleniumDriver(self.driver)
        self.id_info = IdentifyingInformationPage(self.driver)

    # LOCATORS
    _summary_tab = "//a//span[contains(text(), 'ummary')]"  # XPATH
    _identifying_info_tab = "//a//span[contains(text(), 'dentifying Information')]"  # XPATH
    _contacts_tab = "//a//span[contains(text(), 'ontacts')]"  # XPATH
    _location_tab = "//span[text() = 'ocation']"  # XPATH
    _custom_tab = "//a//span[contains(text(), 'C')]"  # XPATH
    _supplier_name = "VENDOR_NAME1"
    _description_field = "VNDR_ADDR_SCROL_DESCR$0"
    _sam_address_type = "VNDR_ADDR_SCROL_CCR_ADDR_TYPE$0"
    _add_new_address_btn = "$ICField2$new$0$$0"
    _country = "VENDOR_ADDR_COUNTRY$0"
    _address_1 = "VENDOR_ADDR_ADDRESS1$0"
    _address_2 = "VENDOR_ADDR_ADDRESS2$0"
    _address_3 = "VENDOR_ADDR_ADDRESS3$0"
    _address_4 = "VENDOR_ADDR_ADDRESS4$0"
    _number = "VENDOR_ADDR_NUM1$0"
    _door = "VENDOR_ADDR_NUM2$0"
    _city = "VENDOR_ADDR_CITY$0"
    _county = "VENDOR_ADDR_COUNTY$0"
    _state = "VENDOR_ADDR_STATE$0"
    _postal = "VENDOR_ADDR_POSTAL$0"
    _email_id = "VENDOR_ADDR_EMAILID$0"
    _override_address_box = "CLN_OVERRIDE_ADDRESS"
    _expand_alt_names_arrow = "//a[@class='PSHYPERLINK PTEXPAND_ARROW']"  # XPATH
    _collapse_alt_names_arrow = "//a[@class='PSHYPERLINK PTCOLLAPSE_ARROW']"  # XPATH
    _pmnt_alt_name_1 = "VENDOR_ADDR_NAME1$17$$0"
    _pmnt_alt_name_2 = "VENDOR_ADDR_NAME2$0"
    _wh_alt_name_1 = "VENDOR_ADDR_NAME1_WTHD$21$$0"
    _wh_alt_name_2 = "VENDOR_ADDR_NAME2_WTHD$0"
    _phone_type = "VENDOR_ADDR_PHN_PHONE_TYPE$0"
    _telephone_field = "VENDOR_ADDR_PHN_PHONE$0"
    _extension_field = "VENDOR_ADDR_PHN_EXTENSION$0"
    _add_new_row_phone = "VENDOR_ADDR_PHN$new$0$$0"
    _search_for_country = "VENDOR_ADDR_COUNTRY$prompt$0"
    _search_for_state = "VENDOR_ADDR_STATE$prompt$0"
    _effective_date = "VENDOR_ADDR_EFFDT$0"

    """ Get the elements """
    def get_sam_address_type(self):
        return self.driver.find_element(By.ID, self._sam_address_type)

    def get_phone_type(self):
        return self.driver.find_element(By.ID, self._phone_type)

    """ Do something with the elements """
    def click_location_tab(self):
        self.element_click(self._location_tab, "xpath")
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Payables")))

    def click_contacts_tab(self):
        self.element_click(self._contacts_tab, "xpath")
        self.util.sleep(2, "the Contacts page to open.")

    def enter_description(self):
        sup_name = self.driver.find_element(By.ID, "VENDOR_NAME1").text
        self.sendkeys(sup_name, self._description_field)

    def select_sam_address_type(self, sam_type):
        sel = Select(self.get_sam_address_type())
        sel.select_by_visible_text(sam_type)

    def enter_country_code(self, country_code):
        self.clear_element(self._country)
        self.sendkeys(country_code, self._country)
        self.sendkeys(Keys.TAB, self._country)
        self.util.sleep(1, "the country code to be recognized by the app.")

    def click_add_new_address_btn(self):
        self.element_click(self._add_new_address_btn)
        self.util.sleep(1)

    def enter_address_one(self):
        fake_data = Faker()
        fake_street_address = fake_data.street_address()
        self.sendkeys(fake_street_address, self._address_1)

    def enter_address_two(self):
        random_num = randint(1, 10)
        self.sendkeys("Bldg. " + str(random_num), self._address_2)

    def enter_address_three(self):
        self.sendkeys("N/A", self._address_3)

    def enter_city(self):
        fake_data = Faker()
        fake_city = fake_data.city()
        self.sendkeys(fake_city, self._city)

    def enter_postal_code(self):
        fake_data = Faker()
        fake_postal_code = fake_data.postalcode()
        self.sendkeys(fake_postal_code, self._postal)
        self.util.sleep(1, "the postal code to be recognized by the app.")

    def enter_random_state(self):
        self.sendkeys(str(choice(STATE_ABBR)), self._state)
        self.util.sleep(1, "the state to be recognized by the app.")

    def enter_email_id(self):
        fake_data = Faker()
        fake_email = fake_data.safe_email()
        self.sendkeys(fake_email, self._email_id)
        self.util.sleep(1, "the email to be recognized by the app.")

    def click_override_address_verification_chkbx(self):
        self.element_click(self._override_address_box)
        self.util.sleep(1, "the app recognizes the override.")

    def expand_alternate_names(self):
        self.element_click(self._expand_alt_names_arrow, "xpath")

    def collapse_alternate_names(self):
        self.element_click(self._collapse_alt_names_arrow, "xpath")

    def click_add_new_phone_btn(self):
        self.element_click(self._add_new_row_phone)

    def search_for_state(self):
        self.element_click(self._search_for_state)

    def enter_random_gb_county(self):
        self.sendkeys(str(choice(GBR_COUNTIES)), self._state)
        self.util.sleep(2, "the state to be recognized by the app.")

    def enter_pmnt_alt_name_1(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._pmnt_alt_name_1)

    def enter_pmnt_alt_name_2(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._pmnt_alt_name_2)

    def enter_withholding_alt_name_1(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._wh_alt_name_1)

    def enter_withholding_alt_name_2(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._wh_alt_name_2)

    """ THIS IS THE MODULE THAT IS CALLED BY THE TEST """
    def enter_payment_withholding_alt_names(self):
        # expanded = self.check.element_presence_check(self._pmnt_alt_name_1)
        expanded = self.check.is_element_present(self._pmnt_alt_name_1)
        print(expanded)
        if expanded:
            self.enter_pmnt_alt_name_1()
            self.enter_pmnt_alt_name_2()
            self.enter_withholding_alt_name_1()
            self.enter_withholding_alt_name_2()
        else:
            self.expand_alternate_names()
            self.check.wait_for_element(self._pmnt_alt_name_1)
            self.enter_pmnt_alt_name_1()
            self.enter_pmnt_alt_name_2()
            self.enter_withholding_alt_name_1()
            self.enter_withholding_alt_name_2()

    def enter_business_phone(self):
        sel = Select(self.get_phone_type())
        sel.select_by_visible_text("Business Phone")

        fake_data = Faker()
        fake_phone = fake_data.random_int(min=2000000, max=9999999)

        self.sendkeys("555" + str(fake_phone), self._telephone_field)
        self.element_click(self._add_new_row_phone)
        self.util.sleep(2, "the new phone row to be recognized by the app.")

    def enter_fax(self):
        sel = Select(self.get_phone_type())
        sel.select_by_visible_text("FAX")

        fake_data = Faker()
        fake_phone = fake_data.random_int(min=2000000, max=9999999)

        self.sendkeys("555" + str(fake_phone), self._telephone_field)
        self.element_click(self._add_new_row_phone)
        self.util.sleep(2, "the new phone row to be recognized by the app.")

    def enter_trilogie_dm_fax(self):
        sel = Select(self.get_phone_type())
        sel.select_by_visible_text("Trilogie DM Fax Number")

        fake_data = Faker()
        fake_phone = fake_data.random_int(min=2000000, max=9999999)

        self.sendkeys("555" + str(fake_phone), self._telephone_field)
        self.element_click(self._add_new_row_phone)
        self.util.sleep(2, "the new phone row to be recognized by the app.")

    def enter_all_phone_types(self):
        phone_type_list = ['Business Phone', 'FAX', 'Trilogie DM Fax Number']

        for phone_type in phone_type_list:
            sel = Select(self.get_phone_type())
            sel.select_by_visible_text(phone_type)

            fake_data = Faker()
            fake_phone = fake_data.random_int(min=2000000, max=9999999)

            self.sendkeys("555" + str(fake_phone), self._telephone_field)
            self.element_click(self._add_new_row_phone)
            self.util.sleep(2, "the new phone row to be recognized by the app.")

    def enter_domestic_master_vendor_address(self, sam_type):
        self.select_sam_address_type(sam_type)

        result = self.driver.find_element(By.ID, self._override_address_box).is_selected()
        if result:
            print('Checkbox already selected')
        else:
            self.driver.find_element(By.ID, self._override_address_box).click()
            print('Checkbox selected')

        self.enter_address_one()
        self.enter_address_two()
        self.enter_city()
        self.enter_postal_code()
        self.enter_random_state()

    def enter_corporate_info_address_domestic(self):
        self.enter_domestic_master_vendor_address("Corporate Info")
        self.enter_email_id()
        self.enter_business_phone()
        self.enter_fax()
        self.enter_trilogie_dm_fax()

    def enter_remit_address_domestic(self):
        self.enter_domestic_master_vendor_address("Remit")
        self.enter_email_id()
        self.enter_business_phone()
        self.enter_fax()
        self.enter_trilogie_dm_fax()

    def enter_po_address_domestic(self):
        self.enter_domestic_master_vendor_address("Trilogie PO Address")
        self.enter_email_id()
        self.enter_business_phone()
        self.enter_fax()
        self.enter_trilogie_dm_fax()

    def enter_foreign_master_vendor_address(self, sam_type, country_code):
        self.select_sam_address_type(sam_type)
        self.element_click(self._search_for_country)
        country = LookUpCountryWindow(self.driver)
        country.select_country(country_code)
        result = self.driver.find_element(By.ID, self._override_address_box).is_selected()
        if result:
            print('Checkbox already selected')
        else:
            self.driver.find_element(By.ID, self._override_address_box).click()
            print('Checkbox selected')

        self.enter_address_one()
        self.enter_address_two()
        self.enter_city()
        self.enter_postal_code()

        if country_code == "GBR":
            self.search_for_state()
            county = LookUpStateWindow(self.driver)
            county.select_county(str(choice(GBR_COUNTIES)))
        else:
            self.search_for_state()
            state = LookUpStateWindow(self.driver)
            state.select_random_state()
