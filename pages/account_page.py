
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators


class AccountPage(BasePage):

    def open_login_page(self):
        self.open("/")
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def login(self, email: str, password: str):
        self.open_login_page()
        self.wait_visible(MainPageLocators.EMAIL_FILL).send_keys(email)
        self.wait_visible(MainPageLocators.PASSWORD_FILL).send_keys(password)
        self.click(PersonalAccountPageLocators.ENTER_BUTTON)
        self.wait_visible(MainPageLocators.ARRANGE_ORDER_BUTTON, timeout=20)
