"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        """
        Inits WebDriverFactor class

        Returns:
            None
        :param browser:
        """
        self.browser = browser

    """
    Set chrome driver and iexplorer environment based on OS

    chromedriver = "C:/.../chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    self.driver = webdriver.Chrome(chromedriver)
    PREFERRED: Set the path on the machine where browser will be executed
    """
    def get_webdriver_instance(self):
        """
        Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        # base_url = "http://a06543.sys.ds.wolseley.com:3043/psp/fusdev10/"        # FUSDEV10
        # base_url = "http://a06615.sys.ds.wolseley.com:3052/psc/fustst10/"        # FUSTST10
        # base_url = "http://a06617.sys.ds.wolseley.com:3061/psp/fusuat10/"        # FUSUAT10
        # base_url = "http://a06615.sys.ds.wolseley.com:3050/psp/fustst00/"        # FUSTST00
        base_url = "https://fms-uat-fei.sys.ds.wolseley.com:3460/psp/fusuat00/"  # FUSUAT00

        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)

        return driver
