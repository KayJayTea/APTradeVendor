from pages.login_page import LoginPage
from pages.navigator_page import NavigatePage
from pages.find_existing_value_page import FindExistingValuePage
from pages.add_new_value_page import SupplierInformationANV
from pages.summary_page import SummaryPage
from pages.identifying_information_page import IdentifyingInformationPage
from pages.address_page import AddressPage
from pages.clean_address_page import CleanAddressPage
from pages.contacts_page import ContactsPage
from pages.location_page import LocationPage
from popup_windows.supplier_xref_window import SupplierXrefWindow
from popup_windows.procurement_options_window import ProcurementOptionsWindow
from utilities.tests_status import TestStatus

import pytest
import unittest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class TestForeignBVMultiLocationsMultiLogons(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.nav = NavigatePage(self.driver)
        self.sup_info_fev = FindExistingValuePage(self.driver)
        self.sup_info_anv = SupplierInformationANV(self.driver)
        self.summary = SummaryPage(self.driver)
        self.id_info = IdentifyingInformationPage(self.driver)
        self.addr = AddressPage(self.driver)
        self.clean_addr = CleanAddressPage(self.driver)
        self.contacts = ContactsPage(self.driver)
        self.loc = LocationPage(self.driver)
        self.procurement = ProcurementOptionsWindow(self.driver)
        self.sup_xref = SupplierXrefWindow(self.driver)

    @pytest.mark.run(order=1)
    # @data((os.environ.get('PSFT_USER_ID'), "wrongpassword"))
    @data(("AUTOTEST3", "wrongpassword"))
    @unpack
    def test_invalid_password(self, username, password):
        self.lp.login(username, password)
        result = self.lp.verify_login_failed()
        self.ts.mark(result, "Login Failed!\n")

    @pytest.mark.run(order=2)
    # @data((os.environ.get('PSFT_USER_ID'), os.environ.get('PSFT_USER_PWD')))
    @data(("AUTOTEST3", "Psoft1234!"))
    @unpack
    def test_foreign_master_and_branch_vendor_creation_multi_loc_multi_logon(self, username, password):
        # Login into PeopleSoft with CREATOR credentials
        self.lp.login(username, password)
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Title is CORRECT")
        self.nav.navigate_to_supplier_info()
        self.sup_info_fev.add_a_new_value()
        self.sup_info_anv.click_add_button()

        """ IDENTIFYING INFORMATION """
        self.id_info.enter_identifying_info()

        """ ADDRESS(ES)"""
        """ FOREIGN CORPORATE INFO ADDRESS """
        self.id_info.click_address_tab()
        self.clean_addr.clean_canadian_address("CANADA", "Corporate Info")
        self.addr.enter_email_id()
        # self.addr.enter_payment_withholding_alt_names()
        self.addr.enter_business_phone()
        self.addr.enter_fax()
        self.addr.enter_trilogie_dm_fax()

        """ FOREIGN REMIT INFORMATION """
        self.addr.click_add_new_address_btn()
        self.clean_addr.clean_brazilian_address("BRAZIL", "Remit")
        self.addr.enter_email_id()
        # self.addr.enter_payment_withholding_alt_names()
        self.addr.enter_business_phone()
        self.addr.enter_fax()
        self.addr.enter_trilogie_dm_fax()

        """ FOREIGN TRILOGIE PO ADDRESS ONE """
        self.addr.click_add_new_address_btn()
        self.clean_addr.clean_singapore_address("SINGAPORE", "Trilogie PO Address")
        self.addr.enter_email_id()
        # self.addr.enter_payment_withholding_alt_names()
        self.addr.enter_business_phone()
        self.addr.enter_fax()
        self.addr.enter_trilogie_dm_fax()

        """ CONTACTS PAGE"""
        self.addr.click_contacts_tab()
        self.contacts.enter_contacts_details("Testing Contacts", "Accountant")

        """ ADD LOCATIONS AND BRANCH VENDORS """
        """ Add a LOC_1 """
        self.addr.click_location_tab()
        self.loc.add_location("LOC_1", "Remit to LOC_1")

        # Add Procurement Options
        self.loc.click_procurement_link()
        self.procurement.change_ordering_address("3")
        self.procurement.change_returning_address("3")
        self.procurement.change_ship_from_address("3")
        self.procurement.select_payment_terms_id("NET30")

        # Add Branch Vendor(s)
        self.loc.click_fei_trilogie_xref_link()
        self.sup_xref.select_two_accounts("HOUSTONWW", "LAHVAC")

        """ Add LOC_2 """
        self.loc.click_add_location_btn()
        self.loc.add_location("LOC_2", "Remit to LOC_2")

        # Add Procurement Options
        self.loc.click_procurement_link()
        self.procurement.select_payment_terms_id("NET60")

        # Add Branch Vendor(s)
        self.loc.click_fei_trilogie_xref_link()
        self.sup_xref.select_two_accounts("OHIOHVAC", "PLYMOUTH")

        """ Add LOC_3 """
        self.loc.click_add_location_btn()
        self.loc.add_location("LOC_3", "Remit to LOC_3")

        # Add Procurement Options
        self.loc.click_procurement_link()
        self.procurement.change_ordering_address("2")
        self.procurement.change_returning_address("2")
        self.procurement.change_ship_from_address("2")
        self.procurement.select_payment_terms_id("NET90")

        # Add Branch Vendor(s)
        self.loc.click_fei_trilogie_xref_link()
        self.sup_xref.select_two_accounts("SACRAMENTO", "SANTAROSAWW")

        """ Save record """
        self.loc.click_save_btn()
        self.loc.click_summary_tab()

        self.summary.get_supplier_id()
        self.summary.search_for_created_supplier()

        result2 = self.summary.verify_supplier_id_created()
        self.ts.mark(result2, "Successfully Created Foreign Master Vendor.\n")

    @pytest.mark.run(order=3)
    def test_sign_out(self):
        self.summary.sign_out_summary_page()

        result = self.lp.verify_title_of_log_out_page()
        self.ts.mark_final("Test Create Master and Branch Vendor", result, "Successfully Signed Out of Application.\n")

    # @pytest.mark.run(order=4)
    # @data(("AUTOTEST4", "Psoft1234!"))
    # @unpack
    # def test_adding_bank_account_data(self, username, password):
    #     self.lp.login(username, password)
    #     result_1 = self.lp.verify_title()
    #     self.ts.mark(result_1, "Title is CORRECT\n")
    #
    #     self.nav.navigate_to_supplier_info()
    #
    #     self.driver.switch_to.frame("ptifrmtgtframe")
    #
    #     self.sup_info_fev.search_for_supplier("0003015044")
    #
    #     self.summary.click_correct_history_btn()
    #     self.summary.click_location_tab()
    #
    #     self.loc.click_payables_link()
    #     self.payable_options.enter_supplier_bank_account_details()
    #
    #     """ Preview Audit, Enter Reason Codes/Comments and Finalize """
    #     self.preview.close_preview_supplier_audit_window_ok()
    #
    #     result_1 = self.lp.verify_title_of_log_out_page()
    #     # self.ts.mark(result_1, "Successfully Signed Out of Application.\n")
    #     self.ts.mark_final("Test Create Master and Branch Vendor", result_1,
    #                        "Successfully added Banking Information to Master Vendor.\n")
