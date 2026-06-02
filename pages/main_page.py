import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Получить ответ на вопрос")
    def get_question(self, locatorquestion, locatoranswer):
        self.scroll_to_element(locatorquestion)
        self.click_element(locatorquestion)
        self.wait_for_element(locatoranswer)
        return self.get_text_from_element(locatoranswer)

    @allure.step("Отображается верхняя кнопка заказа")
    def order_button_upper_displayed(self):
        return self.element_is_displayed(MainPageLocators.ORDER_BUTTON_UP)
    
    @allure.step("Отображается нижняя кнопка заказа")
    def order_button_lower_displayed(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        return self.element_is_displayed(MainPageLocators.ORDER_BUTTON_DOWN)
    
    @allure.step("Принять использование куки")
    def accept_cookies(self):
        self.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_element(locator)






    
