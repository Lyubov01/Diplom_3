from selenium.webdriver.common.by import By


class MainPageLocators:
    # шапка
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, '//p[text()="Личный Кабинет"]']
    CONSTRUCTOR = (By.XPATH,'//p[contains(text(),"Конструктор")]')
    ORDER_FEED_BUTTON= [By.XPATH, '//a[contains(@href, "/feed")]']

    # Конструктор, первая булка
    BURGER_INGREDIENT = (By.XPATH,'//p[contains(@class,"BurgerIngredient_ingredient__text") and '
    'text()="Флюоресцентная булка R2-D3"]')
    # крестик закрытия карточки ингредиента
    CLOSE_BURGER_INGREDIENT_CARD = [
        By.XPATH,'//section[contains(@class,"Modal_modal__")]'
        '//button[contains(@class,"Modal_modal__close")]']

    # счётчик выбранной булки
    COUNTER_INGREDIENT = (By.XPATH,'//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    '//p[contains(@class,"counter_counter__num_")]')

    # кнопка «Оформить заказ»
    ARRANGE_ORDER_BUTTON = [By.XPATH,'//button[contains(@class,"button_button__33qZ0") and text()="Оформить заказ"]']

    # корзина (зона конструктора)
    BASKET = (By.XPATH,'//div[contains(@class,"BurgerConstructor_basket__")]')

    # заголовки
    HEADLINE_ASSEMBLE_BURGER = [By.XPATH, '//h1[text()="Соберите бургер"]']
    HEADLINE_ORDER_FEED = [By.XPATH, '//h1[text()="Лента заказов"]']
    HEADLINE_DETAILS_INGREDIENT = [By.XPATH, '//h2[text()="Детали ингредиента"]']

    #логин при оформлении заказа
    EMAIL_FILL = [By.XPATH,'//input[@class="text input__textfield text_type_main-default"]']
    PASSWORD_FILL = [By.XPATH,'//div[@class="input pr-6 pl-6 input_type_password input_size_default"]'
        '//input[@class="text input__textfield text_type_main-default"]']

    # текст в успешном окне заказа
    TEXT_WINDOW_ORDER= [By.XPATH,'//p[text()="Ваш заказ начали готовить"]']

    INGREDIENT_MODAL = (By.XPATH,'//section[contains(@class,"Modal_modal")]'
        '[.//h2[text()="Детали ингредиента"]]')

    CLOSE_INGREDIENT_MODAL = (By.XPATH,'//section[contains(@class,"Modal_modal")]'
        '//button[contains(@class,"Modal_modal__close")]')