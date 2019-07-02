from pages.login_page import LoginPage
from pages.navigator_page import NavigatePage
from pages.find_existing_value_page import FindExistingValuePage
from pages.add_new_value_page import SupplierInformationANV
from pages.summary_page import SummaryPage
from pages.identifying_information_page import IdentifyingInformationPage
from pages.address_page import AddressPage
from pages.clean_address_page import CleanAddressPage
from pages.location_page import LocationPage
from popup_windows.payables_options_window import PayablesOptionsWindow
from popup_windows.procurement_options_window import ProcurementOptionsWindow
from popup_windows.preview_supplier_audit_window import PreviewSupplierAuditWindow
from utilities.tests_status import TestStatus

import pytest
import unittest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class TestCreateForeignMV(unittest.TestCase):

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
        self.loc = LocationPage(self.driver)
        self.payable_options = PayablesOptionsWindow(self.driver)
        self.procurement = ProcurementOptionsWindow(self.driver)
        self.preview = PreviewSupplierAuditWindow(self.driver)

    @pytest.mark.run(order=1)
    # @data((os.environ.get('PSFT_USER_ID'), "wrongpassword"))
    @data(("AUTOTEST3", "wrongpassword"))
    @unpack
    def test_invalid_password(self, username, password):
        self.lp.login(username, password)
        result_1 = self.lp.verify_login_failed()
        self.ts.mark(result_1, "Login Failed!\n")

    @pytest.mark.run(order=2)
    # @data((os.environ.get('PSFT_USER_ID'), os.environ.get('PSFT_USER_PWD')))
    @data(("AUTOTEST3", "Psoft1234!"))
    @unpack
    def test_foreign_master_vendor_creation(self, username, password):

        self.lp.login(username, password)
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Title is CORRECT\n")

        self.nav.navigate_to_supplier_info()
        self.sup_info_fev.add_a_new_value()
        self.sup_info_anv.click_add_button()
        self.id_info.enter_identifying_info()

        """ FOREIGN CORPORATE INFORMATION """
        self.id_info.click_address_tab()
        self.clean_addr.clean_china_address("CHINA", "Corporate Info")
        self.addr.enter_email_id()
        self.addr.enter_all_phone_types()

        # """ FOREIGN REMIT ADDRESS """
        # self.addr.click_add_new_address_btn()
        # self.clean_addr.clean_french_address("FRANCE", "Remit")
        # self.addr.enter_email_id()
        # self.addr.enter_all_phone_types()
        #
        # """ FOREIGN TRILOGIE PO ADDRESS """
        # self.addr.click_add_new_address_btn()
        # self.clean_addr.clean_australian_address("AUSTRALIA", "Trilogie PO Address")
        # self.addr.enter_email_id()
        # self.addr.enter_all_phone_types()

        """ ADD LOCATIONS """
        self.addr.click_location_tab()
        self.loc.add_location("MAIN", "Remit to Main")

        # Add Procurement
        self.loc.click_procurement_link()
        self.procurement.select_random_payment_terms_id()

        """ SAVE RECORD """
        self.loc.click_save_btn()
        self.loc.click_summary_tab()

        self.summary.get_supplier_id()

        self.summary.search_for_created_supplier()

        result_2 = self.summary.verify_supplier_id_created()
        self.ts.mark(result_2, "Successfully Created Foreign Master Vendor.\n")

    @pytest.mark.run(order=3)
    def test_sign_out(self):
        self.summary.sign_out_summary_page()

        result_1 = self.lp.verify_title_of_log_out_page()
        self.ts.mark(result_1, "Successfully Signed Out of Application.\n")

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
    #     self.sup_info_fev.search_for_supplier("0002000006")
    #
    #     self.summary.click_correct_history_btn()
    #     self.summary.click_location_tab()
    #
    #     self.loc.click_payables_link()
    #     self.payable_options.enter_and_save_supplier_bank_account_details()
    #
    #     """ Preview Audit, Enter Reason Codes/Comments and Finalize """
    #     self.preview.close_preview_supplier_audit_window_ok()
    #
    #     result_1 = self.lp.verify_title_of_log_out_page()
    #     # self.ts.mark(result_1, "Successfully Signed Out of Application.\n")
    #     self.ts.mark_final("Test Create Master Vendor", result_1,
    #                        "Successfully added Banking Information to Master Vendor.\n")
