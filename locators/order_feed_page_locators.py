from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_CARD = (By.XPATH,'(//li[contains(@class,"OrderHistory_listItem") and contains(@class,"mb-6")])[1]') # первая карточка заказа в ленте

    # номер заказа внутри первой карточки
    NUMBER_ORDER_CARD = (By.XPATH,'(//li[contains(@class,"OrderHistory_listItem") and contains(@class,"mb-6")])[1]'
        '//p[contains(@class,"text_type_digits-default")]')

    # заголовок вспл окна заказа
    DATA_WINDOW_ORDER = (By.XPATH, '//section[contains(@class,"Modal_modal")]//p[contains(text(),"Состав")]')

    ORDER_MODAL = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]')#модалка деталей в ленте заказов

    #модалка с подтверждением после заказа
    ORDER_DETAILS_MODAL = (
        By.XPATH,
        '//section[contains(@class,"Modal_modal_opened")'
        ' and .//p[text()="идентификатор заказа"]]'
    )
    
    # счётчик выполнено за все время
    COUNTER_ORDERS_FOR_ALL_TIME = (By.XPATH,'//p[text()="Выполнено за все время:"]/following-sibling::p')

    # счётчик за сегодня
    COUNTER_ORDERS_FOR_TODAY = (By.XPATH,'//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    ORDER_DETAILS_ID = (
        By.XPATH,
        '//section[contains(@class,"Modal_modal_opened")'
        ' and .//p[text()="идентификатор заказа"]]'
        '//h2[contains(@class,"text_type_digits-large")]'
    ) #номер заказа после оформления

    ORDER_DETAILS_CLOSE = (
        By.XPATH,
        '//section[contains(@class,"Modal_modal_opened")'
        ' and .//p[text()="идентификатор заказа"]]'
        '//button[contains(@class,"Modal_modal__close")]'
    ) # крестик закрытия заказа в вспл окне

    # номера заказов в колонке "В работе"
    ORDERS_IN_WORK = (
        By.XPATH,
        '//p[text()="В работе:"]/following-sibling::ul[1]'
        '//li[contains(@class,"text_type_digits-default")]'
    )

    @staticmethod
    def number_our_order(number):
        """Номер заказа в списке «Готовы"""
        return (By.XPATH, f'//ul[contains(@class,"OrderFeed_orderList__cBvyi")]'
        f'//li[contains(@class,"text_type_digits-default") and contains(text(), "{number}")]')

    @staticmethod
    def search_card_order_for_number(number):
        """Карточка в ленте, содержащая номер заказа"""
        return (
            By.XPATH,
            '//li[contains(@class,"OrderHistory_listItem__2x95r") '
            'and contains(@class,"mb-6")]'
            f'//p[text()="{number}"]')
