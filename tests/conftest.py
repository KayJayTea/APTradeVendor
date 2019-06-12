import pytest
from base.webdriver_factory import WebDriverFactory


@pytest.yield_fixture()
def setup():
    print("\n Running method level setUp")
    yield
    print("\n Running method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("\n Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    # lp = LoginPage(driver)
    # lp.login("", "")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\n Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
