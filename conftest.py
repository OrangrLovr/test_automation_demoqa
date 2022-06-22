from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="firefox",  # to select a browser, the value must be None
        help="Choose browser: chrome or firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("--browser-name")

    if driver_name == "chrome":
        options = Options()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
    elif driver_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield driver
    driver.quit()
