from selenium.webdriver.support import expected_conditions as EC
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
        element = self.wait_visible(
            OrderFeedPageLocators.ORDER_DETAILS_ID,
            timeout=25,
        )
        raw = element.text.strip()
        return "".join(ch for ch in raw if ch.isdigit())

    def close_order_details_modal(self):
        self.click(OrderFeedPageLocators.ORDER_DETAILS_CLOSE, timeout=25)
        self.wait_invisible(OrderFeedPageLocators.ORDER_DETAILS_MODAL, timeout=25)

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
        return self.is_visible(locator, timeout=25)

    def order_card_exists_in_feed(self, number: str) -> bool:
        locator = OrderFeedPageLocators.search_card_order_for_number(number)
        return self.is_visible(locator)

    def is_order_modal_open(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_MODAL))
            return True
        except Exception:
            return False
        
    def get_orders_in_work(self) -> list[str]:#Список номеров заказов в работе
        self.wait_visible(OrderFeedPageLocators.ORDERS_IN_WORK, timeout=25)
        elements = self.driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_WORK)
        return [el.text.strip() for el in elements if el.text.strip()]