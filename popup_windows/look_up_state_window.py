from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import random


class LookUpStateWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _state_field = "STATE_TBL_STATE"
    _search_result = "SEARCH_RESULT1"
    _look_up_btn = "#ICSearch"

    def select_random_state(self):
        self.util.sleep(1, "for popup window to open")

        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.util.sleep(2, "for states to be counted")

        total_states = len(self.driver.find_elements(By.XPATH, "//a[contains(@name, 'RESULT2$')]"))
        random_state = random.randint(0, total_states)
        state = self.driver.find_element(By.NAME, "RESULT2$" + str(random_state) + "")
        self.util.sleep(2, "state to be selected")
        state.click()
        self.util.sleep(2, "for popup window to close")

        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            # iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            # self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.util.sleep(2, "")

    def select_state(self, state):
        self.driver.switch_to.default_content()

        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptModFrame_')]")
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print(e)

        self.sendkeys(state, self._state_field)
        self.element_click(self._look_up_btn)
        self.util.sleep(2, "for " + str(state) + " to be found.")
        self.element_click(self._search_result)
        self.util.sleep(2, "for popup window to close")
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            # iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            # self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.util.sleep(2, "")

    def select_county(self, county):
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            # iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            # self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.sendkeys(county, self._state_field)
        self.element_click(self._look_up_btn)
        self.util.sleep(2, "for " + str(county) + " to be found.")
        self.element_click(self._search_result)
        self.util.sleep(2, "for popup window to close")
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(ec.visibility_of_element_located((By.ID, "ptifrmtgtframe")))

        try:
            # iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'ptifrmtgtframe')]")
            # self.driver.switch_to.frame(iframe)
            self.driver.switch_to.frame("ptifrmtgtframe")
        except Exception as e:
            print(e)

        self.util.sleep(2, "")
