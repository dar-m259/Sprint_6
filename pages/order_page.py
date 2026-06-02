import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнить формы заказа")
    def fill_ordering_form(self, first_name, last_name, address, metro_station, phone_number, date, rental_period, color, comment):
        self.wait_for_element(OrderPageLocators.FIRST_NAME_FIELD)
        self.send_keys_to_element(OrderPageLocators.FIRST_NAME_FIELD, first_name)
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.scroll_to_element(metro_station)
        self.click_element(metro_station)
        self.send_keys_to_element(OrderPageLocators.PHONE, phone_number)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        self.wait_for_element(OrderPageLocators.WHEN_FIELD)
        self.click_element(OrderPageLocators.WHEN_FIELD)
        self.click_element(date)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.scroll_to_element(rental_period)
        self.click_element(rental_period)
        self.click_element(color)
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Заказать и подтвердить оформление заказа")
    def make_order(self):
        self.wait_for_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Отображается уведомление об успешном заказе")
    def success_order_notification_displayed(self):
        self.wait_for_element(OrderPageLocators.ORDER_SUCCESS)
        return self.element_is_displayed(OrderPageLocators.ORDER_SUCCESS)
    
    @allure.step("Кликнуть по лого Самоката и получить url открывшейся страницы")
    def to_mainpage(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO)
        return self.url
    
    @allure.step("Кликнуть по лого Яндекса и получить url открывшейся страницы")
    def to_yandex_dzen(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO)
        self.switch_to_new_window()
        self.wait_for_page_to_load('dzen')
        return self.url







