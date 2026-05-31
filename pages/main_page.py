import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Получить ответ на вопрос о стоимости и оплате")
    def get_question1(self):
        self.scroll_to_element(MainPageLocators.QUESTION_1)
        self.click_element(MainPageLocators.QUESTION_1)
        self.wait_for_element(MainPageLocators.ANSWER_1)
        return self.get_text_from_element(MainPageLocators.ANSWER_1)

    @allure.step("Получить ответ на вопрос о нескольких самокатах")
    def get_question2(self):
        self.scroll_to_element(MainPageLocators.QUESTION_2)
        self.click_element(MainPageLocators.QUESTION_2)
        self.wait_for_element(MainPageLocators.ANSWER_2)
        return self.get_text_from_element(MainPageLocators.ANSWER_2)

    @allure.step("Получить ответ на вопрос о расчете времени аренды")
    def get_question3(self):
        self.scroll_to_element(MainPageLocators.QUESTION_3)
        self.click_element(MainPageLocators.QUESTION_3)
        self.wait_for_element(MainPageLocators.ANSWER_3)
        return self.get_text_from_element(MainPageLocators.ANSWER_3)

    @allure.step("Получить ответ на вопрос о заказе самоката на сегодня")
    def get_question4(self):
        self.scroll_to_element(MainPageLocators.QUESTION_4)
        self.click_element(MainPageLocators.QUESTION_4)
        self.wait_for_element(MainPageLocators.ANSWER_4)
        return self.get_text_from_element(MainPageLocators.ANSWER_4)

    @allure.step("Получить ответ на вопрос о продлении и возврате")
    def get_question5(self):
        self.scroll_to_element(MainPageLocators.QUESTION_5)
        self.click_element(MainPageLocators.QUESTION_5)
        self.wait_for_element(MainPageLocators.ANSWER_5)
        return self.get_text_from_element(MainPageLocators.ANSWER_5)

    @allure.step("Получить ответ на вопрос о зарядке")
    def get_question6(self):
        self.scroll_to_element(MainPageLocators.QUESTION_6)
        self.click_element(MainPageLocators.QUESTION_6)
        self.wait_for_element(MainPageLocators.ANSWER_6)
        return self.get_text_from_element(MainPageLocators.ANSWER_6)

    @allure.step("Получить ответ на вопрос об отмене заказа")
    def get_question7(self):
        self.scroll_to_element(MainPageLocators.QUESTION_7)
        self.click_element(MainPageLocators.QUESTION_7)
        self.wait_for_element(MainPageLocators.ANSWER_7)
        return self.get_text_from_element(MainPageLocators.ANSWER_7)

    @allure.step("Получить ответ на вопрос о доставке за МКАД")
    def get_question8(self):
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_element(MainPageLocators.QUESTION_8)
        self.wait_for_element(MainPageLocators.ANSWER_8)
        return self.get_text_from_element(MainPageLocators.ANSWER_8)

    @allure.step("Отображается верхняя кнопка заказа")
    def order_button_upper_displayed(self):
        return self.element_is_displayed(MainPageLocators.ORDER_BUTTON_UP)
    
    @allure.step("Отображается нижняя кнопка заказа")
    def order_button_lower_displayed(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        return self.element_is_displayed(MainPageLocators.ORDER_BUTTON_DOWN)
    
    @allure.step("Заказать через верхнюю кнопку")
    def order_via_upper_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_UP)
        return self.url

    @allure.step("Заказать через нижнюю кнопку")
    def order_via_lower_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        self.click_element(MainPageLocators.ORDER_BUTTON_DOWN)
        return self.url



    
