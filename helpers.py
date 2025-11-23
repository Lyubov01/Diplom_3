import allure

from data import EMAIL, PASSWORD
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


def create_order_and_get_infо(driver):
    account_page = AccountPage(driver)
    main_page = MainPage(driver)
    feed_page = OrderFeedPage(driver)

    with allure.step('Открываем ленту заказов и читаем начальные значения счётчиков'):
        feed_page.open_feed_page()
        total_before = feed_page.get_total_done()
        today_before = feed_page.get_today_done()
        in_work_before = feed_page.get_orders_in_work()
        
    with allure.step('Выполняем вход под тестовым пользователем'):
        account_page.login(EMAIL, PASSWORD)


    with allure.step('Проверяем, что после логина доступно оформление заказа'):
        main_page.open_main_page()
        main_page.click_arrange_order_button()
    

    with allure.step('Создаём новый заказ через конструктор'):
        main_page.open_main_page()
        main_page.drag_bun_to_constructor()
        main_page.drag_filling_to_constructor()
        main_page.click_arrange_order_button()

    with allure.step('Получаем номер заказа из всплывающего окна'):
        order_id = feed_page.get_order_id_from_details()

    with allure.step('Закрываем всплывающееокно  с деталями заказа'):
        feed_page.close_order_details_modal()


    return {
        "feed_page": feed_page,
        "total_before": total_before,
        "today_before": today_before,
        "in_work_before": in_work_before,
        "order_id": order_id}    
