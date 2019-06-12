"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
        name = self.util.get_unique_name()
"""
import time
import traceback
import random
import string
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        put the program to wait for specified amount of time
        :param sec:
        :param info:
        :return:
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' second(s) for " + info)
            try:
                time.sleep(sec)
            except InterruptedError:
                traceback.print_stack()

    def get_alphanumeric(self, length, type="letters"):
        """
        Get random string of characters

        :param length: Length of string, number of characters string should have
        :param type: Type of characters should have. Default is letters
        Provide lower/upper/digits for different types
        :return:
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count="10"):
        """
        Get a unique name
        :param char_count:
        :return:
        """
        return self.get_alphanumeric(char_count, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of valid email ids
        :param list_size: Number of email ids. Default is 5
        :param item_length: it should be a list containing number of items equal to the list_size
                            This determines the length of each item in the list
        :return:
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string
        :param actual_text:
        :param expected_text:
        :return:
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info(" ### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info(" ### VERIFICATION DOES NOT CONTAIN !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify text matches
        :param actual_text:
        :param expected_text:
        :return:
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info(" ### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info(" ### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verify_list_match(self, expected_list, actual_list):
        """
        Verify two lists match
        :param expected_list:
        :param actual_list:
        :return:
        """
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
            else:
                return True
