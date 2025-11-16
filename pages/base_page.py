from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path: str = "/"):
        self.driver.get(BASE_URL + path)

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=10):
        self.wait_clickable(locator, timeout).click()

    def get_text(self, locator, timeout=10):
        return self.wait_visible(locator, timeout).text

    def is_visible(self, locator, timeout=10)-> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except Exception:
            return False
    def wait_invisible(self, locator, timeout=10):  #ожидаем элемент исчезн со стр
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))