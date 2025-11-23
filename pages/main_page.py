from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class MainPage(BasePage):

    def open_main_page(self):
        self.open()

    # шапка
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR)

    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    # ингредиенты
    def click_burger_ingredient(self):
        self.click(MainPageLocators.BURGER_INGREDIENT)

    def get_ingredient_counter(self) -> int:
        try:
            text = self.get_text(MainPageLocators.COUNTER_INGREDIENT)
            return int(text) if text else 0
        except (TimeoutException, NoSuchElementException):
            return 0

    def drag_bun_to_constructor(self):#Добавляю булку
        bun = self.wait_visible(MainPageLocators.BUN_INGREDIENT)
        basket = self.driver.find_element(*MainPageLocators.BASKET)
        ActionChains(self.driver).drag_and_drop(bun, basket).perform()

    def drag_filling_to_constructor(self):#добавляю начинку
        filling = self.wait_visible(MainPageLocators.FILLING_INGREDIENT)
        basket = self.driver.find_element(*MainPageLocators.BASKET)
        ActionChains(self.driver).drag_and_drop(filling, basket).perform()

    # модалка ингредиента
    def ingredient_modal_is_open(self) -> bool:
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL)

    def close_ingredient_modal(self):
        self.click(MainPageLocators.CLOSE_INGREDIENT_MODAL)
        self.wait_invisible(MainPageLocators.INGREDIENT_MODAL)

    # оформление заказа    
    def click_arrange_order_button(self):
        # self.wait.until(EC.element_to_be_clickable(MainPageLocators.ARRANGE_ORDER_BUTTON)).click()
        self.click(MainPageLocators.ARRANGE_ORDER_BUTTON, timeout=25)

    def wait_order_started_text(self):
        return self.wait_visible(MainPageLocators.TEXT_WINDOW_ORDER)

    # логин
    def fill_email(self, email: str):
        self.wait_visible(MainPageLocators.EMAIL_FILL).send_keys(email)

    def fill_password(self, password: str):
        self.wait_visible(MainPageLocators.PASSWORD_FILL).send_keys(password)

    def click_place_an_order(self):
        self.click(MainPageLocators.ARRANGE_ORDER_BUTTON)

    def wait_for_order_created(self):
        return self.get_text(MainPageLocators.TEXT_WINDOW_ORDER, timeout=20)