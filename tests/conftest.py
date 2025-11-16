import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome or firefox",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=720")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--window-size=1280,720")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
