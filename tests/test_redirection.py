import allure

from pages.order_page import OrderPage
from url import MAIN_URL

class TestRedirection:
    @allure.title("Проверить перенаправление кликом по лого Самоката на главную страницу")
    def test_redirection_scooter_logo_to_main_page(self, order_page_driver):
        order_page = OrderPage(order_page_driver)

        current_url = order_page.to_mainpage()
        assert current_url == MAIN_URL

    @allure.title("Проверить перенаправление кликом по лого Яндекса на страницу Яндекс Дзена")
    def test_redirection_yandex_logo_to_yandex_dzen(self, order_page_driver):
        order_page = OrderPage(order_page_driver)

        current_url = order_page.to_yandex_dzen()
        assert 'dzen' in current_url

        


