from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    def open_feed_page(self):
        self.open("/feed")
        self.wait_visible(MainPageLocators.HEADLINE_ORDER_FEED)

    # карточки
    def click_first_order_card(self):
        self.click(OrderFeedPageLocators.ORDER_CARD)

    def get_number_from_first_order_card(self) -> str:
        return self.get_text(OrderFeedPageLocators.NUMBER_ORDER_CARD).strip()

    # модальное окно заказа
    def get_order_id_from_details(self) -> str:
        return self.get_text(OrderFeedPageLocators.ORDER_DETAILS_ID).strip()

    def close_order_details_modal(self):
        self.click(OrderFeedPageLocators.ORDER_DETAILS_CLOSE)

    # счётчики
    def get_total_done(self) -> int:
        txt = self.get_text(OrderFeedPageLocators.COUNTER_ORDERS_FOR_ALL_TIME)
        return int(txt.replace(" ", ""))

    def get_today_done(self) -> int:
        txt = self.get_text(OrderFeedPageLocators.COUNTER_ORDERS_FOR_TODAY)
        return int(txt.replace(" ", ""))

    # поиск номера заказа
    def order_number_is_in_ready_list(self, number: str) -> bool:
        locator = OrderFeedPageLocators.number_our_order(number)
        return self.is_visible(locator)

    def order_card_exists_in_feed(self, number: str) -> bool:
        locator = OrderFeedPageLocators.search_card_order_for_number(number)
        return self.is_visible(locator)

    def is_order_modal_open(self) -> bool:
        return self.is_visible(OrderFeedPageLocators.ORDER_MODAL)