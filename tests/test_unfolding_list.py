import allure

from pages.main_page import MainPage
from data import AnswersFAQ

class TestUnfoldingList:
    @allure.title("Проверить отображение ответа на вопрос о стоимости и оплате")
    def test_unfolding_list_answer1_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question1()
        assert result == AnswersFAQ.FAQ_1

    @allure.title("Проверить отображение ответа на вопрос о нескольких самокатах")
    def test_unfolding_list_answer2_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question2()
        assert result == AnswersFAQ.FAQ_2

    @allure.title("Проверить отображение ответа на вопрос о расчете времени аренды")
    def test_unfolding_list_answer3_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question3()
        assert result == AnswersFAQ.FAQ_3
    
    @allure.title("Проверить отображение ответа на вопрос о заказе самоката на сегодня")
    def test_unfolding_list_answer4_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question4()
        assert result == AnswersFAQ.FAQ_4
    
    @allure.title("Проверить отображение ответа на вопрос о продлении и возврате")
    def test_unfolding_list_answer5_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question5()
        assert result == AnswersFAQ.FAQ_5
    
    @allure.title("Проверить отображение ответа на вопрос о зарядке")
    def test_unfolding_list_answer6_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question6()
        assert result == AnswersFAQ.FAQ_6
    
    @allure.title("Проверить отображение ответа на вопрос об отмене заказа")
    def test_unfolding_list_answer7_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question7()
        assert result == AnswersFAQ.FAQ_7
    
    @allure.title("Проверить отображение ответа на вопрос о доставке за МКАД")
    def test_unfolding_list_answer8_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question8()
        assert result == AnswersFAQ.FAQ_8

