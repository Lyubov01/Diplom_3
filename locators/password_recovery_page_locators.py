from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    PASSWORD_RECOVERY_BUTTON = [By.XPATH, '//a[text()="Восстановить пароль"]']
    EMAIL_FILL = [By.XPATH,'//input[@class="text input__textfield text_type_main-default"]']
    RECOVERY_BUTTON  = [By.XPATH, '//button[text()="Восстановить"]']
    PASSWORD_ACTION_BUTTON = [By.CSS_SELECTOR, '.input__icon-action']
    PASSWORD_FILL = [By.XPATH, '//input[@name="password"]']
    TEXT_RECOVERY_PASSWORD = [By.XPATH,'//h2[text()="Восстановление пароля"]']
