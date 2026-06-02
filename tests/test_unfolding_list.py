import allure
import pytest

from pages.main_page import MainPage
from data import faq_data

class TestUnfoldingList:
    @allure.title("Проверить отображение ответа на вопрос")
    @pytest.mark.parametrize('locatorquestion, locatoranswer, answertext', faq_data)
    def test_unfolding_list_answer1_text(self, main_page_driver, locatorquestion, locatoranswer, answertext):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question(locatorquestion, locatoranswer)
        assert result == answertext


