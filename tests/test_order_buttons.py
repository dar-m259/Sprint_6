import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import test_data

class TestOrderButtons:
    @allure.title("Проверка наличия двух кнопок для заказа на главной странице")
    def test_two_order_buttons_on_main_page(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        upper_button = main_page.order_button_upper_displayed()
        lower_button = main_page.order_button_lower_displayed()

        assert upper_button and lower_button

    @allure.title("Проверка отображения уведомления об успешном заказе после заполнения формы и оформления заказа через обе кнопки 'Заказать'")
    @pytest.mark.parametrize('locator,first_name,last_name,address,metro_station,phone_number,date,rental_period,color,comment', test_data)
    def test_order_successfuly_made(self, main_page_driver, locator, first_name, last_name, address, metro_station, phone_number, date, rental_period, color, comment):
        main_page = MainPage(main_page_driver)

        main_page.accept_cookies()
        main_page.click_order_button(locator)

        order_page = OrderPage(main_page_driver)

        order_page.fill_ordering_form(first_name, last_name, address, metro_station, phone_number, date, rental_period, color, comment)
        order_page.make_order()

        assert order_page.success_order_notification_displayed()

    


        

        