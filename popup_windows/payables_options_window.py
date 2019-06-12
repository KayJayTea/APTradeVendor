from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.location_page import LocationPage
from popup_windows.preview_supplier_audit_window import PreviewSupplierAuditWindow

import logging
import utilities.custom_logger as cl


class PayablesOptionsWindow(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locationPage = LocationPage(self.driver)
        self.preview = PreviewSupplierAuditWindow(self.driver)

    """ Unless otherwise noted, all locator types are 'ID' """
    # LOCATORS
    _help_link = "Help"  # LINK TEXT
    _expand_all_btn_top = "VNDR_MAINT_WRK_EXPAND_ALL_FLAG"
    _collapse_all_btn_top = "VNDR_MAINT_WRK_COLLAPSE_ALL_FLAG"
    _additional_payables_options = "VNDR_LOC_WRK1_VNDR_PAY_OPT_PB"
    _match_approval_options = "GRP_AP_WRK_MATCH_OPT"
    _electronic_file_options = "VNDR_LOC_WRK1_PRENOTE_REQD"
    _self_billed_invoice_options = "VENDOR_LOC_SBI_DOC_DFLT"
    _supplier_bank_options = "VNDR_LOC_WRK1_BANK_ACCT_PB"
    _supplier_type_options = "VNDR_LOC_WRK1_VNDR_TYPE_PB"
    _hippa_information = "VNDR_LOC_WRK1_HIPAA_PB"
    _debit_memo_options = "VNDR_LOC_WRK1_DBMEMO_PYMNT_PB"
    _payment_notification = "VNDR_LOC_WRK1_NOTIFICATION"
    _enable_email_payment_advice_chbx = "VENDOR_PAY_EMAIL_ADVICE$0"
    _email_id_field = "VENDOR_PAY_EMAILID$0"
    _pmnt_method_list = "EMAIL_PAY_MTHD_PYMNT_METHOD$0"
    _expand_all_btn_bottom = ""
    _collapse_all_btn_bottom = ""
    _ok_btn = "#ICSave"
    _cancel_btn = "#ICCancel"

    def click_ok_button(self):
        self.element_click(self._ok_btn)

    def click_cancel_button(self):
        self.element_click(self._cancel_btn)

    """ SUPPLIER BANK ACCOUNTS """
    _add_row_btn = "VNDR_BANK_ACCT_SCR$new$0$$0"
    _delete_row_btn = "VNDR_BANK_ACCT_SCR$delete$0$$0"
    _default_check_box = "VNDR_BANK_ACCT_DEFAULT_IND$0"
    _description_field = "VNDR_BANK_ACCT_DESCR$0"
    _bank_name_field = "VNDR_BANK_ACCT_BENEFICIARY_BANK$0"
    _branch_name_field = "VNDR_BANK_ACCT_BENEF_BRANCH$0"
    _bank_id_qualifier_field = "VNDR_BANK_ACCT_BANK_ID_QUAL$0"
    _bank_id_field = "VNDR_BANK_ACCT_BNK_ID_NBR$0"
    _branch_id_field = "VNDR_BANK_ACCT_BRANCH_ID$0"
    _bank_account_number_field = "VNDR_BANK_ACCT_BANK_ACCOUNT_NUM$0"
    _dfi_qualifier_field = "VNDR_BANK_ACCT_DFI_ID_QUAL$0"
    _iban_field = "VNDR_BANK_ACCT_IBAN_ID$0"
    _account_type_select = "VNDR_BANK_ACCT_BANK_ACCT_TYPE$0"
    _check_digit_field = "VNDR_BANK_ACCT_CHECK_DIGIT$0"
    _dfi_id_field = "VNDR_BANK_ACCT_DFI_ID_NUM$0"

    def enter_description(self, description):
        self.sendkeys(description, self._description_field)

    def enter_bank_name(self, bank_name):
        self.sendkeys(bank_name, self._bank_name_field)
        self.util.sleep(1, "the Bank Name, '{}', to be entered.".format(bank_name))

    def enter_branch_name(self, branch_name):
        self.sendkeys(branch_name, self._branch_name_field)
        self.util.sleep(1, "the Branch Name, '{}', to be entered.".format(branch_name))

    def enter_bank_id_qualifier(self):
        self.sendkeys(("001", Keys.TAB), self._bank_id_qualifier_field)
        self.util.sleep(1, "the 'Bank ID Qualifier' to be recognized by the app.")

    def enter_bank_id(self, bank_id):
        self.element_click(self._bank_id_field)
        self.sendkeys((bank_id, Keys.TAB), self._bank_id_field)
        self.util.sleep(2, "the Bank ID, '{}', to be entered.".format(bank_id))

    def enter_branch_id(self, branch_id):
        self.sendkeys(branch_id, self._branch_id_field)

    def enter_bank_account_number(self, ban):
        self.element_click(self._bank_account_number_field)
        self.sendkeys((ban, Keys.TAB), self._bank_account_number_field)
        self.util.sleep(1, "the Bank Account Number, '{}', to be entered.".format(ban))

    def enter_dfi_qualifier(self):
        self.sendkeys(("01", Keys.TAB), self._dfi_qualifier_field)
        self.util.sleep(2, "the 'DFI ID Qualifier' to be recognized by the app.")

    def select_account_type_check_account(self):
        sel = Select(self.driver.find_element(By.ID, self._account_type_select))
        sel.select_by_value("03")

    def enter_dfi_id(self, dfi):
        self.sendkeys((dfi, Keys.TAB), self._dfi_id_field)
        self.util.sleep(1, "DFI ID, '{}', to be entered.".format(dfi))

    """ ********************** """

    def enter_payment_notification_details(self, email):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, self._payment_notification)))
        self.element_click(self._payment_notification)
        self.element_click(self._enable_email_payment_advice_chbx)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, self._email_id_field)))
        self.sendkeys((email, Keys.TAB), self._email_id_field)

        self.util.sleep(2, "the email, {}, to be recognized by the application.".format(email))

        pymnt_method_list = self.driver.find_element(By.ID, self._pmnt_method_list)
        sel = Select(pymnt_method_list)
        sel.select_by_visible_text("System Check")

        self.util.sleep(2, "the Payment Method to be recognized by the application.".format(email))

        self.element_click(self._ok_btn)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.util.sleep(2, "")

    def enter_and_save_supplier_bank_account_details(self):
        self.element_click(self._supplier_bank_options)
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, self._description_field)))
        self.enter_description("DESCRIPTION")
        self.enter_bank_name("BANK NAME")
        self.enter_branch_name("BRANCH NAME")
        self.enter_bank_id_qualifier()
        self.enter_bank_id("121000358")
        self.enter_bank_account_number("1234567890DBC")
        self.enter_dfi_qualifier()
        self.select_account_type_check_account()
        self.enter_dfi_id("121000358")

        # self.click_cancel_button()
        self.click_ok_button()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.util.sleep(2, "the 'Location' page to be displayed.")

        # self.driver.find_element(By.ID, "#ICSave").click()
        self.element_click("#ICSave")

        self.util.sleep(2, "the 'Preview Audit, Enter Reason Codes/Comments and Finalize' window to open.")

        """ Preview Audit, Enter Reason Codes/Comments and Finalize """
        self.preview.close_preview_supplier_audit_window_ok()
