from base.selenium_driver import SeleniumDriver
from traceback import print_stack
import logging
import utilities.custom_logger as cl


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits Checkpoint class
        :param driver:
        """
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(" *** VERIFICATION SUCCESSFUL :: + " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error(" *** VERIFICATION FAILED :: + " + result_message)
                    self.screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error(" *** VERIFICATION FAILED :: + " + result_message)
                self.screenshot(result_message)
        except Exception as e:
            self.result_list.append("FAIL")
            self.log.error(" *** EXCEPTION OCCURRED !!! " + str(e))
            self.screenshot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        :param result:
        :param result_message:
        :return:
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        :param test_name:
        :param result:
        :param result_message:
        :return:
        """
        self.set_result(result, result_message)
        # print(str(self.result_list))

        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert True is False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True is True
