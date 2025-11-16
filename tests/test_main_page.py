import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Кликаем по кнопке «Конструктор»'):
            page.click_constructor()

        with allure.step('Проверяем заголовок "Соберите бургер"'):
            assert page.is_visible(MainPageLocators.HEADLINE_ASSEMBLE_BURGER)

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Кликаем по кнопке «Лента заказов»'):
            page.click_order_feed()

        with allure.step('Проверяем заголовок "Лента заказов"'):
            assert page.is_visible(MainPageLocators.HEADLINE_ORDER_FEED)

    @allure.title('Клик по ингредиенту открывает всплфвающие окно с деталями')
    def test_ingredient_modal_open(self, driver):
        page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Кликаем по ингредиенту'):
            page.click_burger_ingredient()

        with allure.step('Проверяем, что всплывающее окно открыто'):
            assert page.ingredient_modal_is_open()

    @allure.title('Всплывающее окно закрывается по клику на крестик')
    def test_ingredient_modal_close(self, driver):
        page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()
            page.click_burger_ingredient()

        with allure.step('Закрываем модальное окно по крестику'):
            page.close_ingredient_modal()

        with allure.step('Проверяем, что модальное окно закрыто'):
            assert not page.ingredient_modal_is_open()

    @allure.title('При добавлении ингредиента в заказ счётчик увеличивается')
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Считываем текущее значение счётчика'):
            start = page.get_ingredient_counter()

        with allure.step('Перетаскиваем ингредиент в конструктор'):
            page.drag_ingredient_to_constructor()

        with allure.step('Считываем новое значение счётчика'):
            new = page.get_ingredient_counter()

        with allure.step('Проверяем, что счётчик увеличился на 1'):
            assert new > start
