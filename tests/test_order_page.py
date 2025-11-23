import allure
from helpers import create_order_and_get_infо
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
    def test_create_order_and_get_info(self, driver):
        info = create_order_and_get_infо(driver)
        assert info["order_id"]

    @allure.title('При создании нового заказа увеличивается счётчик "Выполнено за всё время"')
    def test_total_counter_increases_after_new_order(self, driver):
        info = create_order_and_get_infо(driver)
        feed_page = info["feed_page"]
        total_before = info["total_before"]

        with allure.step('Снова открываем ленту заказов'):
            feed_page.open_feed_page()


        with allure.step('Проверяем, что счётчик "Выполнено за все время" увеличился'):
            total_after = feed_page.get_total_done()
            assert total_after > total_before


    @allure.title('При создании нового заказа увеличивается счётчик "Выполнено за сегодня"')
    def test_today_counter_increases_after_new_order(self, driver):
        info = create_order_and_get_infо(driver)
        feed_page = info["feed_page"]
        today_before = info["today_before"]

        with allure.step('Снова открываем ленту заказов'):
            feed_page.open_feed_page()

        with allure.step('Проверяем, что счётчик "Выполнено за сегодня" увеличился'):
            today_after = feed_page.get_today_done()
            assert today_after > today_before


    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_appears_in_ready_list_after_new_order(self, driver):
        info = create_order_and_get_infо(driver)
        feed_page = info["feed_page"]
        in_work_before = set(info["in_work_before"])

        with allure.step('Снова открываем ленту заказов'):
            feed_page.open_feed_page()
            in_work_after = set(feed_page.get_orders_in_work())

        with allure.step('Проверяем, что номер заказа появился в разделе "В работе"/ленте'):
            assert in_work_after - in_work_before