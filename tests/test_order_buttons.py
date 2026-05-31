import allure

from pages.main_page import MainPage
from url import ORDER_URL

class TestOrderButtons:
    @allure.title("Проверка наличия двух кнопок для заказа на главной странице")
    def test_two_order_buttons_on_main_page(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        upper_button = main_page.order_button_upper_displayed()
        lower_button = main_page.order_button_lower_displayed()

        assert upper_button and lower_button

    @allure.title("Проверка перенаправления верхней кнопки заказа на страницу заказа")
    def test_upper_order_button_leads_to_order_page(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        order_url = main_page.order_via_upper_button()

        assert order_url == ORDER_URL

    @allure.title("Проверка перенаправления нижней кнопки заказа на страницу заказа")
    def test_lower_order_button_leads_to_order_page(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        order_url = main_page.order_via_lower_button()

        assert order_url == ORDER_URL
        

        