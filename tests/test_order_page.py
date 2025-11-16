import allure

from data import EMAIL, PASSWORD
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderPage:

    @allure.title('Тест открытия всплыващего окна с деталями заказа')
    def test_order_modal_opens(self, driver):
        feed_page = OrderFeedPage(driver)

        with allure.step('Открываем страницу "Лента заказов"'):
            feed_page.open_feed_page()

        with allure.step('Кликаем по первой карточке заказа'):
            feed_page.click_first_order_card()

        with allure.step('Проверяем, что всплывающее окно с деталями заказа открылось'):
            assert feed_page.is_order_modal_open()
    
    @allure.title('При создании нового заказа увеличиваются счётчики и заказ попадает в ленту')
    def test_counters_and_in_progress_after_new_order(self, driver):
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        with allure.step('Выполняем вход под тестовым пользователем'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем ленту заказов и читаем начальные значения счётчиков'):
            feed_page.open_feed_page()
            total_before = feed_page.get_total_done()
            today_before = feed_page.get_today_done()

        with allure.step('Создаём новый заказ через конструктор'):
            main_page.open_main_page()
            main_page.drag_ingredient_to_constructor()
            main_page.click_arrange_order_button()

        with allure.step('Получаем номер заказа из всплывающего окна'):
            order_id = feed_page.get_order_id_from_details()

        with allure.step('Закрываем всплывающееокно  с деталями заказа'):
            feed_page.close_order_details_modal()

        with allure.step('Снова открываем ленту заказов'):
            feed_page.open_feed_page()

        with allure.step('Проверяем, что счётчик "Выполнено за все время" увеличился'):
            total_after = feed_page.get_total_done()
            assert total_after == total_before + 1

        with allure.step('Проверяем, что счётчик "Выполнено за сегодня" увеличился'):
            today_after = feed_page.get_today_done()
            assert today_after == today_before + 1

        with allure.step('Проверяем, что номер заказа появился в разделе "В работе"/ленте'):
            assert feed_page.order_number_is_in_ready_list(order_id)