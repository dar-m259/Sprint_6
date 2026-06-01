import allure
import pytest

from pages.order_page import OrderPage
from data import test_data

class TestOrderSuccess:
    @allure.title("Проверка отображения уведомления об успешном заказе после заполнения формы и оформления заказа")
    @pytest.mark.parametrize('first_name,last_name,address,phone_number,comment', test_data)
    def test_order_successfuly_made(self, order_page_driver, first_name, last_name, address, phone_number, comment):
        order_page = OrderPage(order_page_driver)

        order_page.accept_cookies()
        order_page.fill_ordering_form(first_name, last_name, address, phone_number, comment)
        order_page.make_order()

        assert order_page.success_order_notification_displayed()

                