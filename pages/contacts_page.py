from base.base_page import BasePage
from faker import Faker
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.util import Util

import utilities.custom_logger as cl
import logging

SAM_TYPE = ["ACH Information", "Accounts Payable", "Accounts Receivable", "Alternate Certifier", "Alternate Electric",
            "Alternate Government", "Alternate Government Business", "Alternate Past Performance",
            "Alternate Past Performance", "Certifier", "Corporate Info", "DNB Monitoring", "DNB Parent",
            "Domestic Parent", "E-Business", "E-Business Alternate", "EDI", "Electric", "Eliminations",
            "General Mailing CleanAddressPage", "Global Parent", "Government Business", "Government Parent",
            "Headquaters", "Mailing CleanAddressPage", "Owner", "Parent", "Party Performing Certification",
            "Past Performance", "Previous Business", "Proceedings", "Proceedings Alternate", "Remit", "Sales",
            "Sole Proprietor", "Third Party Performance", "Trilogie Debit Memo CleanAddressPage",
            "Trilogie PO CleanAddressPage"]

TYPE = ["Accounts Payable", "Billing Contact", "Broker", "Cash Forecast", "Commercial Paper Contact",
        "Contract Collaborator", "Executive Management", "External Contact", "General", "Internal Corporate Contact",
        "Investment Pool Contact", "Line of Credit Contact", "Sales Contact", "Service Contact",
        "Warehousing/Shipping Contact"]


class ContactsPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # LOCATORS
    _contacts_tab = "ICTAB_2"
    _description_field = "VNDR_CNTCT_SCR_DESCR$0"
    _sam_type = "VNDR_CNTCT_SCR_CCR_ADDR_TYPE$0"
    _type = "VENDOR_CNTCT_CONTACT_TYPE$0"
    _name_field = "VENDOR_CNTCT_CONTACT_NAME$0"
    _title_field = "VENDOR_CNTCT_CONTACT_TITLE$0"
    _address = "VENDOR_CNTCT_ADDRESS_SEQ_NUM$0"
    _internet_field = "VENDOR_CNTCT_URL$0"
    _email_field = "VENDOR_CNTCT_EMAILID$0"

    """ GET ELEMENTS """
    def get_sam_type(self):
        return self.driver.find_element(By.ID, self._sam_type)

    def get_type(self):
        return self.driver.find_element(By.ID, self._type)

    """ DO SOMETHING WITH ELEMENTS """
    def click_contacts_tab(self):
        self.element_click(self._contacts_tab)
        self.util.sleep(1, "the Contacts page to open.")

    def enter_description(self, description):
        self.sendkeys(description, self._description_field)

    def select_random_sam_type(self):
        self.get_sam_type().send_keys(choice(SAM_TYPE), Keys.TAB)
        self.util.sleep(1, "the SAM Type to be recognized by the app.")

    def select_random_type(self):
        self.get_type().send_keys(choice(TYPE), Keys.TAB)

    def enter_name(self):
        fake_data = Faker()
        fake_name = fake_data.name()
        self.sendkeys(fake_name, self._name_field)

    def enter_title(self, title):
        self.sendkeys(title, self._title_field)

    def enter_address(self):
        address_number = ["1", "2", "3"]
        self.sendkeys(str(choice(address_number)), self._address)
        # self.sendkeys("1", self._address)

    def enter_email(self):
        fake_data = Faker()
        fake_email = fake_data.safe_email()
        self.sendkeys(fake_email, self._email_field)

    """ THESE MODULES ARE CALLED BY THE TEST """
    def enter_contacts_details(self, description, title):
        self.enter_description(description)
        self.select_random_sam_type()
        self.select_random_type()
        self.enter_name()
        self.enter_title(title)
        self.enter_address()
        self.clear_element(self._internet_field)
        self.sendkeys("http://www.google.com", self._internet_field)
        self.enter_email()
        # time.sleep(2)
