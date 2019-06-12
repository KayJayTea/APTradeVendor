from pages.login_page import LoginPage
from pages.navigator_page import NavigatePage
from pages.find_existing_value_page import FindExistingValuePage
from pages.add_new_value_page import SupplierInformationANV
from pages.summary_page import SummaryPage
from pages.identifying_information_page import IdentifyingInformationPage
from pages.address_page import AddressPage
from pages.location_page import LocationPage
from popup_windows.procurement_options_window import ProcurementOptionsWindow
from utilities.tests_status import TestStatus
from utilities.get_pass import GetPassWarning

import os
import pytest
import unittest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class TestCreateDomesticMV(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ts = TestStatus(self.driver)
        self.get_pass = GetPassWarning(self.driver)
        self.lp = LoginPage(self.driver)
        self.nav = NavigatePage(self.driver)
        self.sup_info_fev = FindExistingValuePage(self.driver)
        self.sup_info_anv = SupplierInformationANV(self.driver)
        self.summary = SummaryPage(self.driver)
        self.id_info = IdentifyingInformationPage(self.driver)
        self.addr = AddressPage(self.driver)
        self.loc = LocationPage(self.driver)
        self.procurement = ProcurementOptionsWindow(self.driver)

    @pytest.mark.run(order=1)
    @data((os.environ.get('PSFT_USER_ID'), "wrongpassword"))
    # @data(("AUTOTEST3", "wrongpassword"))
    @unpack
    def test_invalid_password(self, username, password):
        self.lp.login(username, password)
        result = self.lp.verify_login_failed()
        self.ts.mark(result, "Login Failed!")

    @pytest.mark.run(order=2)
    @data((os.environ.get('PSFT_USER_ID'), os.environ.get('PSFT_USER_PWD')))
    # @data(("AUTOTEST3", "Psoft1234!"))
    @unpack
    def test_domestic_master_vendor_creation(self, username, password):
        self.lp.login(username, password)
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Title is CORRECT\n")

        self.nav.navigate_to_supplier_info()
        self.sup_info_fev.add_a_new_value()
        self.sup_info_anv.click_add_button()
        self.id_info.enter_identifying_info()

        """ CORPORATE INFO """
        self.id_info.click_address_tab()
        self.addr.enter_domestic_master_vendor_address("Corporate Info")
        self.addr.enter_email_id()
        self.addr.enter_all_phone_types()
        # self.addr.enter_business_phone()
        # self.addr.enter_fax()
        # self.addr.enter_trilogie_dm_fax()

        """ REMIT """
        # self.addr.click_add_new_address_btn()
        # self.addr.enter_domestic_master_vendor_address("Remit")
        # self.addr.enter_email_id()
        # self.addr.enter_business_phone()
        # self.addr.enter_fax()
        # self.addr.enter_trilogie_dm_fax()

        """ TRILOGIE PO ADDRESS """
        # self.addr.click_add_new_address_btn()
        # self.addr.enter_domestic_master_vendor_address("Trilogie PO Address")
        # self.addr.enter_email_id()
        # self.addr.enter_business_phone()
        # self.addr.enter_fax()
        # self.addr.enter_trilogie_dm_fax()

        # Add a location
        self.addr.click_location_tab()
        self.loc.add_location("MAIN", "Remit to Main")

        # Add Procurement
        self.loc.click_procurement_link()
        self.procurement.select_payment_terms_id("110N3")

        # Save record
        self.loc.click_save_btn()
        self.loc.click_summary_tab()

        self.summary.get_supplier_id()

        self.summary.search_for_created_supplier()

        result2 = self.summary.verify_supplier_id_created()
        self.ts.mark(result2, "Successfully Created Domestic Master Vendor.")

    @pytest.mark.run(order=3)
    def test_sign_out(self):
        self.summary.sign_out_summary_page()

        result = self.lp.verify_title_of_log_out_page()
        self.ts.mark_final("Test Create Master and Branch Vendor", result, "Successfully Signed Out of Application.")
