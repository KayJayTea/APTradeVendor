from base.base_page import BasePage

import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Unless otherwise noted, locator_type is 'ID' """
    # LOCATORS
    _user_id = "userid"
    _password_field = "pwd"
    _sign_in_button = "Submit"  # By NAME

    def enter_user_id(self, user_id):
        self.sendkeys(user_id, self._user_id)

    def enter_password(self, password):
        self.sendkeys(password, self._password_field)

    def click_sign_in_btn(self):
        self.element_click(self._sign_in_button, locator_type="name")

    def login(self, user_id="", password=""):
        self.enter_user_id(user_id)
        self.enter_password(password)
        self.click_sign_in_btn()

    def verify_login_success(self):
        result = self.is_element_present(
            "//*[@id='PTNUI_LAND_WRK_GROUPBOX14$PIMG']/span[1]", locator_type="xpath")

        return result

    def verify_login_failed(self):
        result = self.is_element_present("//span[@id='login_error']", locator_type="xpath")

        return result

    def verify_title(self):
        return self.verify_page_title("My Homepage")

    def verify_title_of_log_out_page(self):
        return self.verify_page_title("Oracle PeopleSoft Sign-in")
