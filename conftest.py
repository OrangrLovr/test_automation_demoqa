from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif driver_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    driver.quit()
