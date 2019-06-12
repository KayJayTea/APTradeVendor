from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LookUpCountryWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _country_field = "COUNTRY_TBL_COUNTRY"
    _search_result = "SEARCH_RESULT1"
    _look_up_btn = "#ICSearch"

    def select_country(self, country_code):
        self.driver.switch_to.default_content()
        self.util.sleep(2, "'Look Up Country' window to open.")
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.sendkeys(country_code, self._country_field)
        self.element_click(self._look_up_btn)
        self.util.sleep(2, str(country_code) + " to be found.")
        self.element_click(self._search_result)
        self.util.sleep(2, "popup window to close")
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            # iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            # self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)
