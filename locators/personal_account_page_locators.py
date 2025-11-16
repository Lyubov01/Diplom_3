from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    HISTORY_ORDERS = [By.XPATH, '//a[text()="История заказов"]']
    EXIT_BUTTON = [By.XPATH, '//button[text()="Выход"]']
    ENTER_BUTTON = [By.XPATH, '//button[text()="Войти"]']
